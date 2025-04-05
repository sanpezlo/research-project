const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, [], [0, 0, 0]));
    tests.push(test(f, [0], [1, 0, 0]));
    tests.push(test(f, [5], [0, 1, 0]));
    tests.push(test(f, [18], [0, 0, 1]));
    tests.push(test(f, [1, 2, 3, 4], [4, 0, 0]));
    tests.push(test(f, [5, 10, 15, 17], [0, 4, 0]));
    tests.push(test(f, [18, 25, 40, 60], [0, 0, 4]));
    tests.push(test(f, [4, 5, 17, 18], [1, 2, 1]));
    tests.push(test(f, [3, 6, 16, 21, 30, 2, 17, 50], [2, 3, 3]));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
