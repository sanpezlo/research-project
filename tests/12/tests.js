const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, 2, 0));
    tests.push(test(f, 1, 4, 1));
    tests.push(test(f, 2, 3, 8));
    tests.push(test(f, 3, 5, 243));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input_1, input_2, output) {
  return JSON.stringify(f(input_1, input_2)) == JSON.stringify(output);
}

all();
