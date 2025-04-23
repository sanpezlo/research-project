const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, true));
    tests.push(test(f, 1, true));
    tests.push(test(f, 9, true));
    tests.push(test(f, 10, false));
    tests.push(test(f, 100, false));
    tests.push(test(f, 153, true));
    tests.push(test(f, 154, false));
    tests.push(test(f, 370, true));
    tests.push(test(f, 371, true));
    tests.push(test(f, 407, true));
    tests.push(test(f, 9473, false));
    tests.push(test(f, 9474, true));
    tests.push(test(f, 9475, false));
    tests.push(test(f, 146511207, false));
    tests.push(test(f, 146511208, true));
    tests.push(test(f, 146511209, false));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
