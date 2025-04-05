const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, false));
    tests.push(test(f, 1, false));
    tests.push(test(f, 2, true));
    tests.push(test(f, 3, true));
    tests.push(test(f, 4, false));
    tests.push(test(f, 5, true));
    tests.push(test(f, 6, false));
    tests.push(test(f, 7, true));
    tests.push(test(f, 13, true));
    tests.push(test(f, 15, false));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return f(input) == output;
}

all();
