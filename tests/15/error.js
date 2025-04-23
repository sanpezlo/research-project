const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 4, 5, 20));
    tests.push(test(f, 5, 4, 20));
    tests.push(test(f, 6, 8, 24));
    tests.push(test(f, 1, 100, 100));
    tests.push(test(f, 1, 1, 1));
    tests.push(test(f, 0, 5, 0));
    tests.push(test(f, 5, 0, 0));
    tests.push(test(f, 0, 0, 0));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input_1, input_2, output) {
  return JSON.stringify(f(input_1, input_2)) != JSON.stringify(output);
}

all();
