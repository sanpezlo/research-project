const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 2, 3, 5));
    tests.push(test(f, 10, 5, 15));
    tests.push(test(f, -1, 1, 0));
    tests.push(test(f, 0, 0, 0));
    tests.push(test(f, -5, -3, -8));
    tests.push(test(f, 7, -2, 5));
    tests.push(test(f, 100, 200, 300));
    tests.push(test(f, 232, 100, 332));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input_1, input_2, output) {
  return JSON.stringify(f(input_1, input_2)) == JSON.stringify(output);
}

all();
