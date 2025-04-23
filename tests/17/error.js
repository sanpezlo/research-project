const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(
      test(f, [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
      ])
    );

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, output) {
  return JSON.stringify(f()) != JSON.stringify(output);
}

all();
