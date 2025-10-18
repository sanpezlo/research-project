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
    i++;
```

```transformation
    result *= i;
    i++;
```

```transformation
    result += base;
    i++;
```

```transformation
    result -= base;
    i++;
```

```transformation
    result /= base;
    i++;
```

```final
  return result;
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
    i++;
```

```transformation
    result *= i;
    i++;
```

```transformation
    result += base;
    i++;
```

```transformation
    result -= base;
    i++;
```

```transformation
    result /= base;
    i++;
```

```final
  return result;
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
    i--;
```

```transformation
    result *= i;
    i--;
```

```transformation
    result /= base;
    i--;
```

```transformation
    result += base;
    i--;
```

```transformation
    result -= base;
    i--;
```

```final
  return result;
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
    n--;
```

```transformation
    result *= n;
    n--;
```

```transformation
    result += base;
    n--;
```

```transformation
    result -= base;
    n--;
```

```transformation
    result /= base;
    n--;
```

```final
  return result;
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
    n--;
```

```transformation
    result *= n;
    n--;
```

```transformation
    result += base;
    n--;
```

```transformation
    result -= base;
    n--;
```

```transformation
    result /= base;
    n--;
```

```final
  return result;
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
    #(ignore-test)
    result *= base;
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result *= i;
```

```transformation
    #(ignore-test)
    result += base;
```

```transformation
    #(ignore-test)
    result -= base;
```

```transformation
    #(ignore-test)
    result /= base;
```

```final
  return result;
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
    #(ignore-test)
    result *= base;
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result *= i;
```

```transformation
    #(ignore-test)
    result += base;
```

```transformation
    #(ignore-test)
    result -= base;
```

```transformation
    #(ignore-test)
    result /= base;
```

```final
  return result;
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
    #(ignore-test)
    result *= base;
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result *= i;
```

```transformation
    #(ignore-test)
    result /= base;
```

```transformation
    #(ignore-test)
    result += base;
```

```transformation
    #(ignore-test)
    result -= base;
```

```final
  return result;
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
    #(ignore-test)
    result *= base;
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result *= n;
```

```transformation
    #(ignore-test)
    result += base;
```

```transformation
    #(ignore-test)
    result -= base;
```

```transformation
    #(ignore-test)
    result /= base;
```

```final
  return result;
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
    #(ignore-test)
    result *= base;
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result *= n;
```

```transformation
    #(ignore-test)
    result += base;
```

```transformation
    #(ignore-test)
    result -= base;
```

```transformation
    #(ignore-test)
    result /= base;
```

```final
  return result;
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
