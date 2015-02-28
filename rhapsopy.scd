x = CSVFileReader.read("/Users/mike/projects/reddit_data.csv", true).postcs;
x = x.collect(_.collect(_.interpret));

(
SynthDef.new("fuzzer", {
  arg degree = 12;
  var scale = Scale.minor;
  var note1 = DegreeToKey.kr(
      scale.as(LocalBuf),
      degree,
      scale.stepsPerOctave,
      9,
      0
  );

  var sig1 = RLPF.ar(
    Saw.ar([note1, note1],0.1),
    XLine.kr(8000,900,5),
    0.15
  );

  Out.ar(0, sig1);
  Out.ar(1, sig1);
}).add;
)

f = Synth.new("fuzzer");

f.set("degree", 3);
f.set("degree", 9);


f.free;