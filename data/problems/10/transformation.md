---
Write a JavaScript function that returns the reversal of a number with two or more digits using a "while" loop.
---

```initial
  if (n < 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n <= 9) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n + 1 <= 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 > n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (9 >= n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 >= n + 1) {
    return n;
  }

  let reversed = 0;
```

```initial
  let reversed = 0;
```

```transformation
    n = Math.floor(n / 10);
```

```transformation
    reversed = n % 10;
    n = Math.floor(n / 10);
```

```transformation
    let remainder = n % 10;
    reversed = remainder;
    n = Math.floor(n / 10);
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10;
    n = Math.floor(n / 10);
```

```transformation
    reversed *= 10;
    n = Math.floor(n / 10);
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
    n = Math.floor(n / 10);
```

```transformation
    const remainder = n % 10;
    reversed += remainder;
    n = Math.floor(n / 10);
```

```final
  return reversed;
```

```js
function reverseNumber(n) {
  while (n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n != 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 != n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 <= n - 1) {
    //
  }
}
```

===

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```transformation
    n = Math.floor(n / 10);
```

```transformation
    let remainder = n % 10;
    reversed = reversed * 10;
    n = Math.floor(n / 10);
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10;
    n = Math.floor(n / 10);
```

```transformation
    reversed *= 10;
    n = Math.floor(n / 10);
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
    n = Math.floor(n / 10);
```

```transformation
    const remainder = n % 10;
    reversed *= 10;
    n = Math.floor(n / 10);
```

```final
  return isNegative ? -reversed : reversed;
```

```js
function reverseNumber(n) {
  while (n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n != 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 != n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 <= n - 1) {
    //
  }
}
```

===

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```transformation
    n = Math.floor(n % 10);
```

```transformation
    reversed = reversed * 10 + (n / 10);
    n = Math.floor(n % 10);
```

```transformation
    let remainder = n / 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n % 10);
```

```transformation
    const remainder = n / 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n % 10);
```

```transformation
    reversed *= 10;
    reversed += n / 10;
    n = Math.floor(n % 10);
```

```transformation
    let remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n % 10);
```

```transformation
    const remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n % 10);
```

```final
  reversed = reversed * 10 + n;
  return isNegative ? -reversed : reversed;
```

```final
  reversed *= 10;
  reversed += n;
  return isNegative ? -reversed : reversed;
```

```js
function reverseNumber(n) {
  while (n >= 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 9) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n + 1 > 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (9 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 < n + 1) {
    //
  }
}
```

===

```initial
  if (n < 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n <= 9) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n + 1 <= 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 > n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (9 >= n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 >= n + 1) {
    return n;
  }

  let reversed = 0;
```

```initial
  let reversed = 0;
```

```transformation
    n = Math.floor(n % 10);
```

```transformation
    reversed = reversed * 10 + (n / 10);
    n = Math.floor(n % 10);
```

```transformation
    let remainder = n / 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n % 10);
```

```transformation
    const remainder = n / 10;
    reversed = reversed * 10 + remainder;
    n = Math.floor(n % 10);
```

```transformation
    reversed *= 10;
    reversed += n / 10;
    n = Math.floor(n % 10);
```

```transformation
    let remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n % 10);
```

```transformation
    const remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
    n = Math.floor(n % 10);
```

```final
  return reversed * 10 + n;
```

```js
function reverseNumber(n) {
  while (n >= 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 9) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n + 1 > 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (9 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 < n + 1) {
    //
  }
}
```

======

```initial
  if (n < 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n <= 9) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n + 1 <= 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 > n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (9 >= n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 >= n + 1) {
    return n;
  }

  let reversed = 0;
```

```initial
  let reversed = 0;
```

```transformation
    reversed = reversed * 10 + (n % 10);
```

```transformation
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    reversed *= 10;
    reversed += n % 10;
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation

```

```transformation
    reversed = n % 10;
```

```transformation
    let remainder = n % 10;
    reversed = remainder;
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10;
```

```transformation
    reversed *= 10;
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
```

```transformation
    const remainder = n % 10;
    reversed += remainder;
```

```final
  #(ignore-test)
  return reversed;
```

```js
function reverseNumber(n) {
  while (n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n != 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 != n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 <= n - 1) {
    //
  }
}
```

===

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```transformation
    reversed = reversed * 10 + (n % 10);
```

```transformation
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    reversed *= 10;
    reversed += n % 10;
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation

```

```transformation
    let remainder = n % 10;
    reversed = reversed * 10;
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10;
```

```transformation
    reversed *= 10;
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
```

```transformation
    const remainder = n % 10;
    reversed *= 10;
```

```final
  #(ignore-test)
  return isNegative ? -reversed : reversed;
```

```js
function reverseNumber(n) {
  while (n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n != 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 != n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (0 <= n - 1) {
    //
  }
}
```

===

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n <= 9 && n >= -9) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (n < 10 && n > -10) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-9 <= n && 9 >= n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  let reversed = 0;
  let isNegative = n < 0;
  n = Math.abs(n);
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let isNegative = n < 0;
  let reversed = 0;
```

```initial
  if (-10 < n && 10 > n) {
    return n;
  }

  n = Math.abs(n);
  let reversed = 0;
  let isNegative = n < 0;
```

```transformation
    reversed = reversed * 10 + (n % 10);
```

```transformation
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    reversed *= 10;
    reversed += n % 10;
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation

```

```transformation
    reversed = reversed * 10 + (n / 10);
```

```transformation
    let remainder = n / 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    const remainder = n / 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    reversed *= 10;
    reversed += n / 10;
```

```transformation
    let remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation
    const remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
```

```final
  #(ignore-test)
  reversed = reversed * 10 + n;
  return isNegative ? -reversed : reversed;
```

```final
  #(ignore-test)
  reversed *= 10;
  reversed += n;
  return isNegative ? -reversed : reversed;
```

```js
function reverseNumber(n) {
  while (n >= 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 9) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n + 1 > 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (9 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 < n + 1) {
    //
  }
}
```

===

```initial
  if (n < 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n <= 9) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (n + 1 <= 10) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 > n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (9 >= n) {
    return n;
  }

  let reversed = 0;
```

```initial
  if (10 >= n + 1) {
    return n;
  }

  let reversed = 0;
```

```initial
  let reversed = 0;
```

```transformation
    reversed = reversed * 10 + (n % 10);
```

```transformation
    let remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    const remainder = n % 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    reversed *= 10;
    reversed += n % 10;
```

```transformation
    let remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation
    const remainder = n % 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation

```

```transformation
    reversed = reversed * 10 + (n / 10);
```

```transformation
    let remainder = n / 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    const remainder = n / 10;
    reversed = reversed * 10 + remainder;
```

```transformation
    reversed *= 10;
    reversed += n / 10;
```

```transformation
    let remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
```

```transformation
    const remainder = n / 10;
    reversed *= 10;
    reversed += remainder;
```

```final
  #(ignore-test)
  return reversed * 10 + n;
```

```js
function reverseNumber(n) {
  while (n >= 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n > 9) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (n + 1 > 10) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 <= n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (9 < n) {
    //
  }
}
```

```js
function reverseNumber(n) {
  while (10 < n + 1) {
    //
  }
}
```
