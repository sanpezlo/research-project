function count(n) {
  let numbers = [];
  let i = 0;
  while (i <= n - 1) {
    i++;
    numbers.push(i);
  }
  return numbers;
}

function test(input, output) {
  return JSON.stringify(count(input)) == JSON.stringify(output);
}

const tests = [];

tests.push(test(0, []));
tests.push(test(1, [1]));
tests.push(test(2, [1, 2]));
tests.push(test(3, [1, 2, 3]));
tests.push(test(4, [1, 2, 3, 4]));
tests.push(test(5, [1, 2, 3, 4, 5]));

if (!tests.every(Boolean)) {
  console.log(tests);
} else {
  console.log("All tests pass");
}
