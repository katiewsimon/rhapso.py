x = CSVFileReader.read("/Users/mike/projects/reddit_data.csv", true).postcs;
x = x.collect(_.collect(_.interpret));

(


var notes;
notes = Pseq([1, 1, 1, 1]).asStream;

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
)
(
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
    \midinote, Pseq([60, 72, 71, 67, 69, 71, 72, 60, 69, 67], 1),
        // rhythmic values
    \dur, Pseq([2, 2, 1, 0.5, 0.5, 1, 1, 2, 2, 3], 1)
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