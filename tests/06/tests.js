const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, [], null));
    tests.push(test(f, [5], 5));
    tests.push(test(f, [1, 2], 1));
    tests.push(test(f, [1, 2, 3, 4, 5], 1));
    tests.push(test(f, [8, 7, 6, 4, 5, 6], 4));
    tests.push(test(f, [2, 3, 4, 5, 6, 1], 1));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return f(input) == output;
}

all();
