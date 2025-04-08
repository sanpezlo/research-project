---
Write a JavaScript function that returns the factorial of a number using a "while" loop.
---

```initial
  let result = 1;
  let i = 1;
```

```initial
  let i = 1;
  let result = 1;
```

```initial
  let result = 1;
  let i = 2;
```

```initial
  let i = 2;
  let result = 1;
```

```transformation
    result *= i;
    i++;
```

```final
  return i;
```

```final
  return n;
```

```final

```

```js
function factorial(n) {
  while (i <= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n >= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function factorial(n) {
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

```transformation
    result *= i;
    i--;
```

```final
  return i;
```

```final
  return n;
```

```final

```

```js
function factorial(n) {
  while (i > 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (i >= 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 < i) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 <= i - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 <= i) {
    //
  }
}
```

===

```initial
  let result = 1;
```

```transformation
    result *= n;
    n--;
```

```final
  return n;
```

```final

```

```js
function factorial(n) {
  while (n > 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (n > 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 < n) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 < n) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 <= n - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 <= n) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = 0;
```

```initial
  let i = 0;
  let result = 1;
```

```transformation
    result *= i + 1;
    i++;
```

```final
  return i;
```

```final
  return n;
```

```final

```

```js
function factorial(n) {
  while (i < n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n > i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n >= i + 1) {
    //
  }
}
```

======

```initial
  let result = 1;
  let i = 1;
```

```initial
  let i = 1;
  let result = 1;
```

```initial
  let result = 1;
  let i = 2;
```

```initial
  let i = 2;
  let result = 1;
```

```transformation
    result *= i;
    i++;
```

```final

```

```final
  return result;
```

```final
  return i;
```

```final
  return n;
```

```js
function factorial(n) {
  while (i < n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i <= n + 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i - 1 <= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n > i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n + 1 >= i) {
    //
  }
}
```

```js
function factorial(n) {
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

```transformation
    result *= i;
    i--;
```

```final

```

```final
  return result;
```

```final
  return i;
```

```final
  return n;
```

```js
function factorial(n) {
  while (i >= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 <= i) {
    //
  }
}
```

===

```initial
  let result = 1;
```

```transformation
    result *= n;
    n--;
```

```final

```

```final
  return result;
```

```final
  return n;
```

```js
function factorial(n) {
  while (n >= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 <= n) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = 0;
```

```initial
  let i = 0;
  let result = 1;
```

```transformation
    result *= i + 1;
    i++;
```

```final

```

```final
  return result;
```

```final
  return n;
```

```final
  return i;
```

```js
function factorial(n) {
  while (i <= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i < n - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i + 1 < n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n >= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n - 1 > i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n > i + 1) {
    //
  }
}
```

======

```initial
  let result = 1;
  let i = 1;
```

```initial
  let i = 1;
  let result = 1;
```

```initial
  let result = 1;
  let i = 2;
```

```initial
  let i = 2;
  let result = 1;
```

```transformation
    result *= i;
    i++;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
  return i;
```

```final
  #(ignore-test)
  return n;
```

```js
function factorial(n) {
  while (i >= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i > n + 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i - 1 > n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n <= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n + 1 < i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n < i - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i > n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i >= n + 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i - 1 >= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n < i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n + 1 <= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n <= i - 1) {
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

```transformation
    result *= i;
    i--;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
  return i;
```

```final
  #(ignore-test)
  return n;
```

```js
function factorial(n) {
  while (i < 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (i - 1 <= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (i <= 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 > i) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 >= i - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 >= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (i <= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (i - 1 < 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (i < 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 >= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 > i - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 > i) {
    //
  }
}
```

===

```initial
  let result = 1;
```

```transformation
    result *= n;
    n--;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
  return n;
```

```js
function factorial(n) {
  while (n < 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (n < 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (n - 1 <= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (n <= 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 > n) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 > n) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 >= n - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 >= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n <= 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (n <= 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (n - 1 < 0) {
    //
  }
}
```

```js
function factorial(n) {
  while (n < 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 >= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 >= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (0 > n - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (1 > n) {
    //
  }
}
```

===

```initial
  let result = 1;
  let i = 0;
```

```initial
  let i = 0;
  let result = 1;
```

```transformation
    result *= i + 1;
    i++;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
  return i;
```

```final
  #(ignore-test)
  return n;
```

```js
function factorial(n) {
  while (i > n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i >= n - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i + 1 >= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n < i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n - 1 <= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n <= i + 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i >= n) {
    //
  }
}
```

```js
function factorial(n) {
  while (i > n - 1) {
    //
  }
}
```

```js
function factorial(n) {
  while (i + 1 > n) {
    //
  }
}
```

```js
function factorial(n) {
  while (n <= i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n - 1 < i) {
    //
  }
}
```

```js
function factorial(n) {
  while (n < i + 1) {
    //
  }
}
```
