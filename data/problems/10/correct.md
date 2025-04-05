---
Write a JavaScript function that returns the reversal of a number with two or more digits using a "while" loop.
---

```js
function reverseNumber(n) {
  if (n < 10) return n;

  let reversed = 0;
  while (n > 0) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n < 10 && n > -10) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n > 0) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9) return n;

  let reversed = 0;
  while (n > 0) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9 && n >= -9) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n > 0) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 0) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 0) {
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 0) {
    reversed *= 10;
    reversed += n % 10;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 0) {
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n < 10) return n;

  let reversed = 0;
  while (n) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n < 10 && n > -10) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9) return n;

  let reversed = 0;
  while (n) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9 && n >= -9) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n) {
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n) {
    reversed *= 10;
    reversed += n % 10;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n) {
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n < 10) return n;

  let reversed = 0;
  while (n >= 1) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n < 10 && n > -10) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n >= 1) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9) return n;

  let reversed = 0;
  while (n >= 1) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9 && n >= -9) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n >= 1) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 1) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 1) {
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 1) {
    reversed *= 10;
    reversed += n % 10;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 1) {
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  if (n < 10) return n;

  let reversed = 0;
  while (n >= 10) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  if (n < 10 && n > -10) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n >= 10) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  reversed = reversed * 10 + n;

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9) return n;

  let reversed = 0;
  while (n >= 10) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  if (n <= 9 && n >= -9) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n >= 10) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  reversed *= 10;
  reversed += n;

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 10) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 10) {
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 10) {
    reversed *= 10;
    reversed += n % 10;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 10) {
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  if (n < 10) return n;

  let reversed = 0;
  while (n > 9) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  if (n < 10 && n > -10) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n > 9) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  reversed = reversed * 10 + n;

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  if (n <= 9) return n;

  let reversed = 0;
  while (n > 9) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  if (n <= 9 && n >= -9) return n;

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);

  while (n > 9) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }

  reversed *= 10;
  reversed += n;

  return isNegative ? -reversed : reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 9) {
    reversed = reversed * 10 + (n % 10);
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 9) {
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 9) {
    reversed *= 10;
    reversed += n % 10;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 9) {
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 0) {
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 0) {
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n) {
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n) {
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 1) {
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 1) {
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 10) {
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n >= 10) {
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 9) {
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(n) {
  let reversed = 0;
  while (n > 9) {
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n / 10);
  }
  return reversed * 10 + n;
}
```

```js
function reverseNumber(N) {
  if (N < 10) return N;

  let result = 0;
  while (N > 0) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N < 10 && N > -10) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N > 0) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9) return N;

  let result = 0;
  while (N > 0) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9 && N >= -9) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N > 0) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 0) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 0) {
    let last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 0) {
    result *= 10;
    result += N % 10;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 0) {
    let last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N < 10) return N;

  let result = 0;
  while (N) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N < 10 && N > -10) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9) return N;

  let result = 0;
  while (N) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9 && N >= -9) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N) {
    let last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N) {
    result *= 10;
    result += N % 10;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N) {
    let last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N < 10) return N;

  let result = 0;
  while (N >= 1) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N < 10 && N > -10) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N >= 1) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9) return N;

  let result = 0;
  while (N >= 1) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9 && N >= -9) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N >= 1) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 1) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 1) {
    let last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 1) {
    result *= 10;
    result += N % 10;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 1) {
    let last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  if (N < 10) return N;

  let result = 0;
  while (N >= 10) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  if (N < 10 && N > -10) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N >= 10) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  result = result * 10 + N;

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9) return N;

  let result = 0;
  while (N >= 10) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  if (N <= 9 && N >= -9) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N >= 10) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  result *= 10;
  result += N;

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 10) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 10) {
    let last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 10) {
    result *= 10;
    result += N % 10;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 10) {
    let last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  if (N < 10) return N;

  let result = 0;
  while (N > 9) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  if (N < 10 && N > -10) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N > 9) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  result = result * 10 + N;

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  if (N <= 9) return N;

  let result = 0;
  while (N > 9) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  if (N <= 9 && N >= -9) return N;

  let result = 0;
  let negative = N < 0;
  N = Math.abs(N);

  while (N > 9) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }

  result *= 10;
  result += N;

  return negative ? -result : result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 9) {
    result = result * 10 + (N % 10);
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 9) {
    let last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 9) {
    result *= 10;
    result += N % 10;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 9) {
    let last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 0) {
    const last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 0) {
    const last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N) {
    const last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N) {
    const last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 1) {
    const last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 1) {
    const last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 10) {
    const last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N >= 10) {
    const last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 9) {
    const last = N % 10;
    result = result * 10 + last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```

```js
function reverseNumber(N) {
  let result = 0;
  while (N > 9) {
    const last = N % 10;
    result *= 10;
    result += last;
    N = Math.floor(N / 10);
  }
  return result * 10 + N;
}
```
