const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, "hello", "olleh"));
    tests.push(test(f, "world", "dlrow"));
    tests.push(test(f, "", ""));
    tests.push(test(f, "a", "a"));
    tests.push(test(f, "racecar", "racecar"));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
