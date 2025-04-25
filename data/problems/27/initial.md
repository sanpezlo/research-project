---
Write a JavaScript function that returns the sum of all integers between 1 and N, divisible by 9, using a "while" loop.
---

```initial
  let i = 1;
  let sum = n;
```

```initial
  let sum = n;
  let i = 1;
```

```initial
  let i = 0;
  let sum = n;
```

```initial
  let sum = n;
  let i = 0;
```

```initial
  let i = 1;
  let sum = 1;
```

```initial
  let sum = 1;
  let i = 1;
```

```initial
  let i = 0;
  let sum = 1;
```

```initial
  let sum = 1;
  let i = 0;
```

```transformation
    if (i % 9 == 0) {
      sum += i;
    }
    i++;
```

```final
  return sum;
```

```js
function countAndSumDivisibleBy9(n) {
  while (i <= n) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n >= i) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let i = n;
  let sum = n;
```

```initial
  let sum = n;
  let i = n;
```

```initial
  let i = n;
  let sum = 1;
```

```initial
  let sum = 1;
  let i = n;
```

```transformation
    if (i % 9 == 0) {
      sum += i;
    }
    i--;
```

```final
  return sum;
```

```js
function countAndSumDivisibleBy9(n) {
  while (i >= 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (i + 1 > 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (i > -1) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (i > 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (i >= 1) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 <= i) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 < i + 1) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (-1 < i) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 < i) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (1 <= i) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 <= i - 1) {
    //
  }
}
```

===

```initial
  let sum = n;
```

```initial
  let sum = 1;
```

```transformation
    if (n % 9 == 0) {
      sum += n;
    }
    n--;
```

```final
  return sum;
```

```js
function countAndSumDivisibleBy9(n) {
  while (n >= 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n + 1 > 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n > -1) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n > 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 <= n) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 < n + 1) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (-1 < n) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 < n) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function countAndSumDivisibleBy9(n) {
  while (0 <= n - 1) {
    //
  }
}
```
