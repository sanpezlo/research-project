const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 10, 0));
    tests.push(test(f, 25, 10));
    tests.push(test(f, 99, 81));
    tests.push(test(f, 123, 6));
    tests.push(test(f, 405, 0));
    tests.push(test(f, 8917, 504));
    tests.push(test(f, 10000, 0));
    tests.push(test(f, 987654, 60480));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
