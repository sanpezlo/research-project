const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, []));
    tests.push(test(f, 1, [1]));
    tests.push(test(f, 2, [1, 2]));
    tests.push(test(f, 3, [1, 3]));
    tests.push(test(f, 4, [1, 2, 4]));
    tests.push(test(f, 6, [1, 2, 3, 6]));
    tests.push(test(f, 9, [1, 3, 9]));
    tests.push(test(f, 10, [1, 2, 5, 10]));
    tests.push(test(f, 12, [1, 2, 3, 4, 6, 12]));
    tests.push(test(f, 25, [1, 5, 25]));
    tests.push(test(f, 100, [1, 2, 4, 5, 10, 20, 25, 50, 100]));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) != JSON.stringify(output);
}

all();
