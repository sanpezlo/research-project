const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, "", ""));
    tests.push(test(f, "a", "A"));
    tests.push(test(f, "abc", "ABC"));
    tests.push(test(f, "Hello", "HELLO"));
    tests.push(test(f, "JavaScript", "JAVASCRIPT"));
    tests.push(test(f, "hello world!", "HELLO WORLD!"));
    tests.push(test(f, "123abc", "123ABC"));
    tests.push(test(f, "MiXeD CaSe", "MIXED CASE"));

    if (!tests.some(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) != JSON.stringify(output);
}

all();
