const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, []));
    tests.push(test(f, 1, []));
    tests.push(test(f, 2, [2]));
    tests.push(test(f, 3, [2]));
    tests.push(test(f, 4, [2, 4]));
    tests.push(test(f, 5, [2, 4]));
    tests.push(test(f, 6, [2, 4, 6]));
    tests.push(test(f, 7, [2, 4, 6]));
    tests.push(test(f, 8, [2, 4, 6, 8]));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
