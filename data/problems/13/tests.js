const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, false));
    tests.push(test(f, 1, false));
    tests.push(test(f, 2, false));
    tests.push(test(f, 3, false));
    tests.push(test(f, 4, false));
    tests.push(test(f, 5, false));
    tests.push(test(f, 6, true));
    tests.push(test(f, 7, false));
    tests.push(test(f, 27, false));
    tests.push(test(f, 28, true));
    tests.push(test(f, 29, false));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
