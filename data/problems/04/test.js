function isPrime(num) {
  let count = 0;
  let i = 1;
  while (i <= num) {
    if (num % i == 0) {
      count++;
    }
    i++;
  }
  return count == 2;
}

function test(input, output) {
  return isPrime(input) == output;
}

const tests = [];

tests.push(test(0, false));
tests.push(test(1, false));
tests.push(test(2, true));
tests.push(test(3, true));
tests.push(test(4, false));
tests.push(test(5, true));
tests.push(test(6, false));
tests.push(test(7, true));
tests.push(test(13, true));
tests.push(test(15, false));

if (!tests.every(Boolean)) {
  console.log(tests);
} else {
  console.log("All tests pass");
}
