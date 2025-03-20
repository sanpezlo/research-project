function min(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let min = Number.MAX_VALUE;
  let i = 0;
  while (i < numbers.length) {
    if (numbers[i] < min) {
      min = numbers[i];
    }
    i++;
  }
  return min;
}

function test(input, output) {
  return min(input) == output;
}

const tests = [];

tests.push(test([], null));
tests.push(test([5], 5));
tests.push(test([1, 2], 1));
tests.push(test([1, 2, 3, 4, 5], 1));
tests.push(test([8, 7, 6, 4, 5, 6], 4));
tests.push(test([2, 3, 4, 5, 6, 1], 1));

if (!tests.every(Boolean)) {
  console.log(tests);
} else {
  console.log("All tests pass");
}
