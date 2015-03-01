x = CSVFileReader.read("/Users/mike/projects/rhapso.py/reddit_to_music.csv", true).postcs;
x = x.collect(_.collect(_.interpret));

x.postln;
(
var scale = Scale.minor.ratios;

var notes = Pseq(x.collect{
  arg subarray;
  subarray[1].postln;
  scale[subarray[1]] * 200
});

//var durations = Pseq([2, 1, 0.5, 0.5], 1);

var durations = Pseq(x.collect{
  arg subarray;
  subarray[2] / 4;
});

SynthDef.new("fuzzer", { | freq = 440 |
  var sig1 = RLPF.ar(
    SinOsc.ar(freq, 0.1, XLine.kr(1, 0.01, 1, doneAction: 2)),
    XLine.kr(8000,900,5),
    0.15,
    1,
    XLine.kr(1, 0.01, 1, doneAction: 2)
  );

  Out.ar(0, sig1);
  Out.ar(1, sig1);
}).add;

/*
r = Task({
  var delta;
  while {
    delta = notes.next;
    delta.notNil
  } {
    Synth("fuzzer", ["note", 200]);
    delta.yield;
  }
}).play(quant: TempoClock.default.beats + 1.0);
*/

p = Pbind(
        // the name of the SynthDef to use for each note
    \instrument, \fuzzer,
        // MIDI note numbers -- converted automatically to Hz
    \freq, notes,
        // rhythmic values
    \dur, durations
).play;
)



(
  var note = Scale.minor.ratios[0] * 100;
  note.postln;

  f = Synth.new("fuzzer", ["note", note]);
)

f.free;

s.freeAll;

s.boot;
s.quit;