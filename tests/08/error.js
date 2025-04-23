const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, []));
    tests.push(test(f, 1, [0]));
    tests.push(test(f, 2, [0, 1]));
    tests.push(test(f, 3, [0, 1, 1]));
    tests.push(test(f, 4, [0, 1, 1, 2]));
    tests.push(test(f, 5, [0, 1, 1, 2, 3]));
    tests.push(test(f, 6, [0, 1, 1, 2, 3, 5]));
    tests.push(test(f, 7, [0, 1, 1, 2, 3, 5, 8]));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) != JSON.stringify(output);
}

all();
