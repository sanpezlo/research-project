const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, 0));
    tests.push(test(f, 1, 1));
    tests.push(test(f, 2, 2));
    tests.push(test(f, 9, 9));
    tests.push(test(f, 10, 1));
    tests.push(test(f, 10000, 1));
    tests.push(test(f, 123456, 654321));
    tests.push(test(f, 1234560, 654321));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
