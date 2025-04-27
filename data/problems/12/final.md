---
Write a JavaScript function that returns the power of a given base raised to a given exponent using a "while" loop.
---

```initial
  let result = 1;
  let i = 0;
```

```initial
  let i = 0;
  let result = 1;
```

```initial
  let result = base;
  let i = 1;
```

```initial
  let i = 1;
  let result = base;
```

```transformation
    result *= base;
    i++;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```final
  return i;
```

```js
function power(base, n) {
  while (i < n) {
    //
  }
}
```

```js
function power(base, n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = 1;
```

```initial
  let i = 1;
  let result = 1;
```

```initial
  let result = base;
  let i = 2;
```

```initial
  let i = 2;
  let result = base;
```

```transformation
    result *= base;
    i++;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```final
  return i;
```

```js
function power(base, n) {
  while (i <= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function power(base, n) {
  while (n >= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = n;
```

```initial
  let i = n;
  let result = 1;
```

```initial
  let result = base;
  let i = n - 1;
```

```initial
  let i = n - 1;
  let result = base;
```

```transformation
    result *= base;
    i--;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```final
  return i;
```

```js
function power(base, n) {
  while (i > 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (i >= 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 < i) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 <= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 <= i - 1) {
    //
  }
}
```

===

```initial
  let result = 1;
```

```transformation
    result *= base;
    n--;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```js
function power(base, n) {
  while (n) {
    //
  }
}
```

```js
function power(base, n) {
  while (n != 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (n >= 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 != n) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 < n) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 <= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 <= n - 1) {
    //
  }
}
```

===

```initial
  let result = base;
```

```transformation
    result *= base;
    n--;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```js
function power(base, n) {
  while (n - 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n != 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 >= 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n >= 2) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 != n) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 < n) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 <= n - 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (2 <= n) {
    //
  }
}
```

======

```initial
  let result = 1;
  let i = 0;
```

```initial
  let i = 0;
  let result = 1;
```

```initial
  let result = base;
  let i = 1;
```

```initial
  let i = 1;
  let result = base;
```

```transformation
    result *= base;
    i++;
```

```final
  return result;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```final
  return i;
```

```js
function power(base, n) {
  while (i <= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (i < n - 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i + 1 < n) {
    //
  }
}
```

```js
function power(base, n) {
  while (n >= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 > i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > i + 1) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = 1;
```

```initial
  let i = 1;
  let result = 1;
```

```initial
  let result = base;
  let i = 2;
```

```initial
  let i = 2;
  let result = base;
```

```transformation
    result *= base;
    i++;
```

```final
  return result;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```final
  return i;
```

```js
function power(base, n) {
  while (i < n) {
    //
  }
}
```

```js
function power(base, n) {
  while (i <= n + 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i - 1 <= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n + 1 >= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n >= i - 1) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = n;
```

```initial
  let i = n;
  let result = 1;
```

```initial
  let result = base;
  let i = n - 1;
```

```initial
  let i = n - 1;
  let result = base;
```

```transformation
    result *= base;
    i--;
```

```final
  return result;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```final
  return i;
```

```js
function power(base, n) {
  while (i >= 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (i > 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i - 1 > 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 <= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 < i) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 < i - 1) {
    //
  }
}
```

===

```initial
  let result = 1;
```

```transformation
    result *= base;
    n--;
```

```final
  return result;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```js
function power(base, n) {
  while (n >= 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 > 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 <= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 < n) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 < n - 1) {
    //
  }
}
```

===

```initial
  let result = base;
```

```transformation
    result *= base;
    n--;
```

```final
  return result;
```

```final

```

```final
  return base;
```

```final
  return n;
```

```js
function power(base, n) {
  while (n >= 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 > 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n > 2) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 <= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 < n - 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (2 < n) {
    //
  }
}
```

======

```initial
  let result = 1;
  let i = 0;
```

```initial
  let i = 0;
  let result = 1;
```

```initial
  let result = base;
  let i = 1;
```

```initial
  let i = 1;
  let result = base;
```

```transformation
    result *= base;
    i++;
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return base;
```

```final
  #(ignore-test)
  return n;
```

```final
  #(ignore-test)
  return i;
```

```js
function power(base, n) {
  while (i > n) {
    //
  }
}
```

```js
function power(base, n) {
  while (i >= n - 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i + 1 >= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (n < i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 <= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n <= i + 1) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = 1;
```

```initial
  let i = 1;
  let result = 1;
```

```initial
  let result = base;
  let i = 2;
```

```initial
  let i = 2;
  let result = base;
```

```transformation
    result *= base;
    i++;
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return base;
```

```final
  #(ignore-test)
  return n;
```

```final
  #(ignore-test)
  return i;
```

```js
function power(base, n) {
  while (i >= n) {
    //
  }
}
```

```js
function power(base, n) {
  while (i > n + 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i - 1 > n) {
    //
  }
}
```

```js
function power(base, n) {
  while (n <= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n + 1 < i) {
    //
  }
}
```

```js
function power(base, n) {
  while (n < i - 1) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = n;
```

```initial
  let i = n;
  let result = 1;
```

```initial
  let result = base;
  let i = n - 1;
```

```initial
  let i = n - 1;
  let result = base;
```

```transformation
    result *= base;
    i--;
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return base;
```

```final
  #(ignore-test)
  return n;
```

```final
  #(ignore-test)
  return i;
```

```js
function power(base, n) {
  while (i < 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (i <= 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (i - 1 <= 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 > i) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 >= i) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 >= i - 1) {
    //
  }
}
```

===

```initial
  let result = 1;
```

```transformation
    result *= base;
    n--;
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return base;
```

```final
  #(ignore-test)
  return n;
```

```js
function power(base, n) {
  while (n < 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (n <= 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 <= 0) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 > n) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 > n) {
    //
  }
}
```

```js
function power(base, n) {
  while (0 > n - 1) {
    //
  }
}
```

===

```initial
  let result = base;
```

```transformation
    result *= base;
    n--;
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return base;
```

```final
  #(ignore-test)
  return n;
```

```js
function power(base, n) {
  while (n < 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n - 1 <= 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (n <= 2) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 > n) {
    //
  }
}
```

```js
function power(base, n) {
  while (1 >= n - 1) {
    //
  }
}
```

```js
function power(base, n) {
  while (2 >= n) {
    //
  }
}
```
