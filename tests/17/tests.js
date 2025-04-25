const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0));
    tests.push(test(f, 1));
    tests.push(test(f, 2));
    tests.push(test(f, 3));
    tests.push(test(f, 4));
    tests.push(test(f, 5));
    tests.push(test(f, 6));
    tests.push(test(f, 7));
    tests.push(test(f, 8));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function calculatePowers(n) {
  let result = [];
  let i = 1;
  while (i <= n) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}

function test(f, input) {
  return JSON.stringify(f(input)) == JSON.stringify(calculatePowers(input));
}

all();
