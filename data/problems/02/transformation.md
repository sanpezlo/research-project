---
Write a JavaScript function that returns the sum of the numbers from 1 to N using a "while" loop.
---

```initial
  let sum = 0;
  let i = 1;
```

```initial
  let i = 1;
  let sum = 0;
```

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    sum += n;
    i++;
```

```transformation
    sum -= n;
    i++;
```

```transformation
    sum *= n;
    i++;
```

```transformation
    sum /= n;
    i++;
```

```transformation
    sum -= i;
    i++;
```

```transformation
    sum *= i;
    i++;
```

```transformation
    sum /= i;
    i++;
```

```final
  return sum;
```

```js
function sum(n) {
  while (i <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= i) {
    //
  }
}
```

```js
function sum(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function sum(n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    sum += n;
    i++;
```

```transformation
    sum -= n;
    i++;
```

```transformation
    sum *= n;
    i++;
```

```transformation
    sum /= n;
    i++;
```

```transformation
    sum -= i;
    i++;
```

```transformation
    sum *= i;
    i++;
```

```transformation
    sum /= i;
    i++;
```

```final
  return sum;
```

```js
function sum(n) {
  while (true) {
    //
    if (i > n) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n < i) {
      break;
    }
  }
}
```

===

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    sum += i;
    i++;
```

```transformation
    sum -= i;
    i++;
```

```transformation
    sum *= i;
    i++;
```

```transformation
    sum /= i;
    i++;
```

```transformation
    sum += n;
    i++;
```

```transformation
    sum -= n;
    i++;
```

```transformation
    sum *= n;
    i++;
```

```transformation
    sum /= n;
    i++;
```

```transformation
    sum -= i + 1;
    i++;
```

```transformation
    sum *= i + 1;
    i++;
```

```transformation
    sum /= i + 1;
    i++;
```

```final
  return sum;
```

```js
function sum(n) {
  while (i < n) {
    //
  }
}
```

```js
function sum(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (n > i) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
```

```transformation
    n--;
```

```transformation
    sum -= n;
    n--;
```

```transformation
    sum *= n;
    n--;
```

```transformation
    sum /= n;
    n--;
```

```final
  return sum;
```

```js
function sum(n) {
  while (n) {
    //
  }
}
```

```js
function sum(n) {
  while (n != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < n) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= n - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n < 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n < 1) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n <= 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 > n) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (1 > n) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 >= n) {
      break;
    }
  }
}
```

===

```initial
  let sum = 0;
  let i = n;
```

```initial
  let i = n;
  let sum = 0;
```

```transformation
    i--;
```

```transformation
    sum += n;
    i--;
```

```transformation
    sum -= n;
    i--;
```

```transformation
    sum *= n;
    i--;
```

```transformation
    sum /= n;
    i--;
```

```transformation
    sum -= i;
    i--;
```

```transformation
    sum *= i;
    i--;
```

```transformation
    sum /= i;
    i--;
```

```final
  return sum;
```

```js
function sum(n) {
  while (i) {
    //
  }
}
```

```js
function sum(n) {
  while (i != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < i) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= i - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (i < 1) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (i < 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (i <= 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (1 > i) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 > i) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 >= i) {
      break;
    }
  }
}
```

===

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    i++;
    sum += n;
```

```transformation
    i++;
    sum -= n;
```

```transformation
    i++;
    sum *= n;
```

```transformation
    i++;
    sum /= n;
```

```transformation
    i++;
    sum -= i;
```

```transformation
    i++;
    sum *= i;
```

```transformation
    i++;
    sum /= i;
```

```final
  return sum;
```

```js
function sum(n) {
  while (i < n) {
    //
  }
}
```

```js
function sum(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (n > i) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
  let i = n + 1;
```

```initial
  let i = n + 1;
  let sum = 0;
```

```transformation
    i--;
```

```transformation
    i--;
    sum += n;
```

```transformation
    i--;
    sum -= n;
```

```transformation
    i--;
    sum *= n;
```

```transformation
    i--;
    sum /= n;
```

```transformation
    i--;
    sum -= i;
```

```transformation
    i--;
    sum *= i;
```

```transformation
    i--;
    sum /= i;
```

```final
  return sum;
```

```js
function sum(n) {
  while (i) {
    //
  }
}
```

```js
function sum(n) {
  while (i != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < i) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= i - 1) {
    //
  }
}
```

===

```initial
  let sum = n;
```

```transformation
    n--;
```

```transformation
    n--;
    sum -= n;
```

```transformation
    n--;
    sum *= n;
```

```transformation
    n--;
    sum /= n;
```

```final
  return sum;
```

```js
function sum(n) {
  while (n) {
    //
  }
}
```

```js
function sum(n) {
  while (n != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < n) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= n - 1) {
    //
  }
}
```

======

```initial
  let sum = 0;
  let i = 1;
```

```initial
  let i = 1;
  let sum = 0;
```

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation

```

```transformation
    sum += n;
```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum -= i;
```

```transformation
    sum *= i;
```

```transformation
    sum /= i;
```

```transformation
    sum += i;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (i <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= i) {
    //
  }
}
```

```js
function sum(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function sum(n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation

```

```transformation
    sum += n;
```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum -= i;
```

```transformation
    sum *= i;
```

```transformation
    sum /= i;
```

```transformation
    sum += i;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (true) {
    //
    if (i > n) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n < i) {
      break;
    }
  }
}
```

===

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation

```

```transformation
    sum += i;
```

```transformation
    sum -= i;
```

```transformation
    sum *= i;
```

```transformation
    sum /= i;
```

```transformation
    sum += n;
```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum -= i + 1;
```

```transformation
    sum *= i + 1;
```

```transformation
    sum /= i + 1;
```

```transformation
    sum += i + 1;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (i < n) {
    //
  }
}
```

```js
function sum(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (n > i) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
```

```transformation

```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum += n;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (n) {
    //
  }
}
```

```js
function sum(n) {
  while (n != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < n) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= n - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n < 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n < 1) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (n <= 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 > n) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (1 > n) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 >= n) {
      break;
    }
  }
}
```

===

```initial
  let sum = 0;
  let i = n;
```

```initial
  let i = n;
  let sum = 0;
```

```transformation

```

```transformation
    sum += n;
```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum -= i;
```

```transformation
    sum *= i;
```

```transformation
    sum /= i;
```

```transformation
    sum += i;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (i) {
    //
  }
}
```

```js
function sum(n) {
  while (i != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < i) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= i - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (i < 1) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (i < 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (i <= 0) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (1 > i) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 > i) {
      break;
    }
  }
}
```

```js
function sum(n) {
  while (true) {
    //
    if (0 >= i) {
      break;
    }
  }
}
```

===

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```transformation

```

```transformation
    sum += n;
```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum -= i;
```

```transformation
    sum *= i;
```

```transformation
    sum /= i;
```

```transformation
    sum += i;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (i < n) {
    //
  }
}
```

```js
function sum(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (n > i) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
  let i = n + 1;
```

```initial
  let i = n + 1;
  let sum = 0;
```

```transformation

```

```transformation
    sum += n;
```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum -= i;
```

```transformation
    sum *= i;
```

```transformation
    sum /= i;
```

```transformation
    sum += i;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (i) {
    //
  }
}
```

```js
function sum(n) {
  while (i != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (i >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < i) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= i) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= i - 1) {
    //
  }
}
```

===

```initial
  let sum = n;
```

```transformation

```

```transformation
    sum -= n;
```

```transformation
    sum *= n;
```

```transformation
    sum /= n;
```

```transformation
    sum += n;
```

```final
  #(ignore-test)
  return sum;
```

```js
function sum(n) {
  while (n) {
    //
  }
}
```

```js
function sum(n) {
  while (n != 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n > 0) {
    //
  }
}
```

```js
function sum(n) {
  while (n >= 1) {
    //
  }
}
```

```js
function sum(n) {
  while (n - 1 >= 0) {
    //
  }
}
```

```js
function sum(n) {
  while (0 != n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 < n) {
    //
  }
}
```

```js
function sum(n) {
  while (1 <= n) {
    //
  }
}
```

```js
function sum(n) {
  while (0 <= n - 1) {
    //
  }
}
```
