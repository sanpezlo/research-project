const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, 0));
    tests.push(test(f, 1, 0));
    tests.push(test(f, 9, 9));
    tests.push(test(f, 10, 9));
    tests.push(test(f, 18, 27));
    tests.push(test(f, 20, 27));
    tests.push(test(f, 27, 54));
    tests.push(test(f, 50, 135));
    tests.push(test(f, 100, 594));
    tests.push(test(f, 200, 2277));
    tests.push(test(f, -10, 0));
    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
