const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]));
    tests.push(test(f, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
    tests.push(test(f, 2, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]));
    tests.push(test(f, 3, [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]));
    tests.push(test(f, 9, [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]));
    tests.push(test(f, 11, [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]));
    tests.push(test(f, 12, [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]));
    tests.push(test(f, 13, [13, 26, 39, 52, 65, 78, 91, 104, 117, 130]));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
