function average(numbers) {
  let sum = 0;
  let i = 1;
  while (i <= numbers.length) {
    sum += numbers[i - 1] / numbers.length;
    i++;
  }
  return sum;
}

function test(input, output) {
  return average(input) == output;
}

const tests = [];

tests.push(test([], 0));
tests.push(test([5], 5));
tests.push(test([1, 2], 1.5));
tests.push(test([1, 2, 3, 4, 5], 3));
tests.push(test([1, 1, 1, 1, 1], 1));
tests.push(test([1, 2, 3, 4, 5, 6], 3.5));
tests.push(test([1, 2, 3, 4, 5, 6, 7], 4));
tests.push(test([1, 2, 3, 4, 5, 6, 7, 8], 4.5));

if (!tests.every(Boolean)) {
  console.log(tests);
} else {
  console.log("All tests pass");
}
