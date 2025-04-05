const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, []));
    tests.push(test(f, 1, [1]));
    tests.push(test(f, 2, [1]));
    tests.push(test(f, 3, [1, 3]));
    tests.push(test(f, 4, [1, 3]));
    tests.push(test(f, 5, [1, 3, 5]));
    tests.push(test(f, 6, [1, 3, 5]));
    tests.push(test(f, 7, [1, 3, 5, 7]));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
