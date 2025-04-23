const functions = [];

function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, "", ""));
    tests.push(test(f, "aeiou", ""));
    tests.push(test(f, "AEIOU", ""));
    tests.push(test(f, "hello", "hll"));
    tests.push(test(f, "HELLO", "HLL"));
    tests.push(test(f, "JavaScript", "JvScrpt"));
    tests.push(test(f, "HOLA MUNDO", "HL MND"));
    tests.push(test(f, "12345", "12345"));
    tests.push(test(f, "xyz", "xyz"));
    tests.push(test(f, "Vowels: aeiouAEIOU", "Vwls: "));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return JSON.stringify(f(input)) == JSON.stringify(output);
}

all();
