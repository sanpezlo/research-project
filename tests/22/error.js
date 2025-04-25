const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, 1));
    tests.push(test(f, 1, 1));
    tests.push(test(f, 5, 1));
    tests.push(test(f, 9, 1));
    tests.push(test(f, 10, 2));
    tests.push(test(f, 100, 3));
    tests.push(test(f, 123, 3));
    tests.push(test(f, 1000, 4));
    tests.push(test(f, 9999, 4));
    tests.push(test(f, 12.34, 2));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) != JSON.stringify(output);
}

all();
