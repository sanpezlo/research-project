const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, 0));
    tests.push(test(f, 1, 1));
    tests.push(test(f, 2, 3));
    tests.push(test(f, 3, 6));
    tests.push(test(f, 4, 10));
    tests.push(test(f, 100, 5050));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) != JSON.stringify(output);
}

all();
