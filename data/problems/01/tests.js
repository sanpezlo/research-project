const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 5, 120));
    tests.push(test(f, 6, 720));
    tests.push(test(f, 0, 1));
    tests.push(test(f, 1, 1));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return f(input) == output;
}

all();
