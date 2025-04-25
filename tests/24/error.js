const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, 0));
    tests.push(test(f, 1, 1));
    tests.push(test(f, 10, 2));
    tests.push(test(f, 11, 3));
    tests.push(test(f, 100, 4));
    tests.push(test(f, 101, 5));
    tests.push(test(f, 110, 6));
    tests.push(test(f, 111, 7));
    tests.push(test(f, 1000, 8));
    tests.push(test(f, 1010, 10));
    tests.push(test(f, 1111, 15));
    tests.push(test(f, 10000, 16));
    tests.push(test(f, 11001, 25));
    tests.push(test(f, 11111111, 255));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) != JSON.stringify(output);
}

all();
