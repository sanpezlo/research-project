const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, [], null));
    tests.push(test(f, [0], 0));
    tests.push(test(f, [5], 5));
    tests.push(test(f, [1, 2], 2));
    tests.push(test(f, [5, 1, 2, 3], 5));
    tests.push(test(f, [8, 7, 6, 10, 5, 6], 10));
    tests.push(test(f, [2, 3, 4, 5, 6, 100], 100));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return f(input) != output;
}

all();
