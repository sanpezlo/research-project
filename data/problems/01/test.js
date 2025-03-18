function factorial(n) {
  let result = 1;
  let i = 0;
  while (i < n) {
    result = result * (i + 1);
    i = i + 1;
  }
  return result;
}

function test(input, output) {
  return factorial(input) === output;
}

const tests = [];

tests.push(test(5, 120));
tests.push(test(6, 720));
tests.push(test(0, 1));
tests.push(test(1, 1));

if (!tests.every(Boolean)) {
  console.log(tests);
} else {
  console.log("All tests pass");
}
