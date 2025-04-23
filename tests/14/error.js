const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 48, 18, 6));
    tests.push(test(f, 18, 48, 6));
    tests.push(test(f, 101, 103, 1));
    tests.push(test(f, 54, 24, 6));
    tests.push(test(f, 0, 7, 7));
    tests.push(test(f, 7, 0, 7));
    tests.push(test(f, 7, 14, 7));
    tests.push(test(f, 0, 0, 0));
    tests.push(test(f, 1, 1, 1));
    tests.push(test(f, 123456, 789012, 12));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input_1, input_2, output) {
  return JSON.stringify(f(input_1, input_2)) != JSON.stringify(output);
}

all();
