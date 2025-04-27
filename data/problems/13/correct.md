---
Write a JavaScript function that returns whether a number is perfect using a "while" loop.
---

```initial
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (n <= 0) {
    return false;
  }

  let i = 0;
  let sum = 0;
```

```initial
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (n <= 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
```

```initial
  if (0 >= n) {
    return false;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (0 >= n) {
    return false;
  }

  let i = 0;
  let sum = 0;
```

```initial
  if (0 >= n) {
    return false;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (0 >= n) {
    return false;
  }

  let i = 1;
  let sum = 0;
```

```initial
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (n < 1) {
    return false;
  }

  let i = 0;
  let sum = 0;
```

```initial
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (n < 1) {
    return false;
  }

  let i = 1;
  let sum = 0;
```

```initial
  if (1 > n) {
    return false;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (1 > n) {
    return false;
  }

  let i = 0;
  let sum = 0;
```

```initial
  if (1 > n) {
    return false;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (1 > n) {
    return false;
  }

  let i = 1;
  let sum = 0;
```

```initial
  if (n - 1 < 0) {
    return false;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (n - 1 < 0) {
    return false;
  }

  let i = 0;
  let sum = 0;
```

```initial
  if (n - 1 < 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (n - 1 < 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
```

```initial
  if (0 > n - 1) {
    return false;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (0 > n - 1) {
    return false;
  }

  let i = 0;
  let sum = 0;
```

```initial
  if (0 > n - 1) {
    return false;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (0 > n - 1) {
    return false;
  }

  let i = 1;
  let sum = 0;
```

```initial
  if (n < 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
```

```initial
  if (n < 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
```

```initial
  if (2 > n) {
    return false;
  }

  let sum = 1;
  let i = 2;
```

```initial
  if (2 > n) {
    return false;
  }

  let i = 2;
  let sum = 1;
```

```initial
  if (n <= 1) {
    return false;
  }

  let sum = 1;
  let i = 2;
```

```initial
  if (n <= 1) {
    return false;
  }

  let i = 2;
  let sum = 1;
```

```initial
  if (1 >= n) {
    return false;
  }

  let sum = 1;
  let i = 2;
```

```initial
  if (1 >= n) {
    return false;
  }

  let i = 2;
  let sum = 1;
```

```initial
  if (n - 1 <= 0) {
    return false;
  }

  let sum = 1;
  let i = 2;
```

```initial
  if (n - 1 <= 0) {
    return false;
  }

  let i = 2;
  let sum = 1;
```

```initial
  if (0 >= n - 1) {
    return false;
  }

  let sum = 1;
  let i = 2;
```

```initial
  if (0 >= n - 1) {
    return false;
  }

  let i = 2;
  let sum = 1;
```

```transformation
    if (n % i == 0) {
      sum += i;
    }
    i++;
```

```final
  return sum == n;
```

```final
  return n == sum;
```

```js
function isPerfect(n) {
  while (i < n) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (i <= n * 0.5) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (i <= n / 2) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n > i) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n * 0.5 >= i) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n / 2 >= i) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (n <= 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
```

```transformation
    if (n % i == 0) {
      sum += i;
      if (i != n / i) {
        sum += n / i;
      }
    }
    i++;
```

```final
  return sum - n == n;
```

```final
  return n == sum - n;
```

```js
function isPerfect(n) {
  while (i <= n ** 0.5) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (i <= Math.pow(n, 0.5)) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (i <= Math.sqrt(n)) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n ** 0.5 >= i) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (Math.pow(n, 0.5) >= i) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (Math.sqrt(n) >= i) {
    //
  }
}
```

===

```initial
  if (n < 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
```

```initial
  if (n < 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
```

```transformation
    if (n % i == 0) {
      sum += i;
      if (i != n / i) {
        sum += n / i;
      }
    }
    i++;
```

```final
  return sum == n;
```

```final
  return n == sum;
```

```js
function isPerfect(n) {
  while (i * i <= n) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (i ** 2 <= n) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (Math.pow(i, 2) <= n) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n >= i * i) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n >= i ** 2) {
    //
  }
}
```

```js
function isPerfect(n) {
  while (n >= Math.pow(i, 2)) {
    //
  }
}
```
