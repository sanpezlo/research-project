const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 10, [1, 0]));
    tests.push(test(f, 25, [2, 5]));
    tests.push(test(f, 99, [9, 9]));
    tests.push(test(f, 123, [1, 3]));
    tests.push(test(f, 405, [4, 5]));
    tests.push(test(f, 8907, [8, 7]));
    tests.push(test(f, 10000, [1, 0]));
    tests.push(test(f, 987654, [9, 4]));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) != JSON.stringify(output);
}

all();
