const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, []));
    tests.push(test(f, 1, [1]));
    tests.push(test(f, 2, [1, 2]));
    tests.push(test(f, 3, [1, 2, 3]));
    tests.push(test(f, 4, [1, 2, 3, 4]));
    tests.push(test(f, 5, [1, 2, 3, 4, 5]));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
