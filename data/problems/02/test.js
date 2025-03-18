function sum(n) {
  let sum = n;
  while (n >= 1) {
    n--;
    sum += n;
  }
  return sum;
}

function test(input, output) {
  return sum(input) === output;
}

const tests = [];

tests.push(test(0, 0));
tests.push(test(1, 1));
tests.push(test(2, 3));
tests.push(test(3, 6));
tests.push(test(4, 10));
tests.push(test(100, 5050));

if (!tests.every(Boolean)) {
  console.log(tests);
} else {
  console.log("All tests pass");
}
