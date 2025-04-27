---
Write a JavaScript function that returns the greatest common divisor of two numbers using a "while" loop.
---

```transformation
    let temp = b;
    b = a % b;
    a = temp;
```

```transformation
    const temp = b;
    b = a % b;
    a = temp;
```

```transformation
    let temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
```

```transformation
    const temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
```

```final

```

```final
  return b;
```

```js
function gcd(a, b) {
  while (b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b != 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b > 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b >= 1) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b - 1 >= 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 != b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 < b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (1 <= b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 <= b - 1) {
    //
  }
}
```

===

```initial
  if (Math.min(a, b) == 0) {
    return Math.max(a, b);
  }
```

```initial
  if (0 == Math.min(a, b)) {
    return Math.max(a, b);
  }
```

```transformation
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
```

```transformation
    if (b < a) {
      a -= b;
    } else {
      b -= a;
    }
```

```transformation
    if (b >= a) {
      b -= a;
    } else {
      a -= b;
    }
```

```final

```

```final
  return b;
```

```js
function gcd(a, b) {
  while (b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b != 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b > 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b >= 1) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b - 1 >= 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 != b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 < b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (1 <= b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 <= b - 1) {
    //
  }
}
```

===

```initial
  let result = Math.max(a, b);
  let i = 1;
```

```initial
  let result = Math.max(a, b);
  let i = 0;
```

```initial
  let result = a;
  if (b > a) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = a;
  if (a < b) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = b;
  if (b < a) {
    result = a;
  }

  let i = 1;
```

```initial
  let result = b;
  if (a > b) {
    result = a;
  }

  let i = 1;
```

```transformation
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
```

```transformation
    if (b % i == 0 && a % i == 0) {
      result = i;
    }
    i++;
```

```final

```

```final
  return a;
```

```final
  return b;
```

```js
function gcd(a, b) {
  while (i <= a && i <= b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (i <= b && i <= a) {
    //
  }
}
```

======

```transformation
    let temp = b;
    b = a % b;
    a = temp;
```

```transformation
    const temp = b;
    b = a % b;
    a = temp;
```

```transformation
    let temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
```

```transformation
    const temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
```

```final
  return a;
```

```final

```

```final
  return b;
```

```js
function gcd(a, b) {
  while (b >= 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b > 1) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b - 1 > 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 <= b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (1 < b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 < b - 1) {
    //
  }
}
```

===

```initial
  if (Math.min(a, b) == 0) {
    return Math.max(a, b);
  }
```

```initial
  if (0 == Math.min(a, b)) {
    return Math.max(a, b);
  }
```

```transformation
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
```

```transformation
    if (b < a) {
      a -= b;
    } else {
      b -= a;
    }
```

```transformation
    if (b >= a) {
      b -= a;
    } else {
      a -= b;
    }
```

```final
  return a;
```

```final

```

```final
  return b;
```

```js
function gcd(a, b) {
  while (b - 1 > 1) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b > 2) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b - 1 >= 2) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (1 < b - 1) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (2 < b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (2 <= b - 1) {
    //
  }
}
```

===

```initial
  let result = Math.max(a, b);
  let i = 1;
```

```initial
  let result = Math.max(a, b);
  let i = 0;
```

```initial
  let result = a;
  if (b > a) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = a;
  if (a < b) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = b;
  if (b < a) {
    result = a;
  }

  let i = 1;
```

```initial
  let result = b;
  if (a > b) {
    result = a;
  }

  let i = 1;
```

```transformation
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
```

```transformation
    if (b % i == 0 && a % i == 0) {
      result = i;
    }
    i++;
```

```final
  return result;
```

```final

```

```final
  return a;
```

```final
  return b;
```

```js
function gcd(a, b) {
  while (i < a && i < b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (i < b && i < a) {
    //
  }
}
```

======

```transformation
    let temp = b;
    b = a % b;
    a = temp;
```

```transformation
    const temp = b;
    b = a % b;
    a = temp;
```

```transformation
    let temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
```

```transformation
    const temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
```

```final
  #(ignore-test)
  return a;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return b;
```

```js
function gcd(a, b) {
  while (b == 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b < 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b <= 1) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b - 1 <= 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 == b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 > b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (1 >= b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 >= b - 1) {
    //
  }
}
```

===

```initial
  if (Math.min(a, b) == 0) {
    return Math.max(a, b);
  }
```

```initial
  if (0 == Math.min(a, b)) {
    return Math.max(a, b);
  }
```

```transformation
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
```

```transformation
    if (b < a) {
      a -= b;
    } else {
      b -= a;
    }
```

```transformation
    if (b >= a) {
      b -= a;
    } else {
      a -= b;
    }
```

```final
  #(ignore-test)
  return a;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return b;
```

```js
function gcd(a, b) {
  while (b == 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b < 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b <= 1) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (b - 1 <= 0) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 == b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 > b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (1 >= b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (0 >= b - 1) {
    //
  }
}
```

===

```initial
  let result = Math.max(a, b);
  let i = 1;
```

```initial
  let result = Math.max(a, b);
  let i = 0;
```

```initial
  let result = a;
  if (b > a) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = a;
  if (a < b) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = b;
  if (b < a) {
    result = a;
  }

  let i = 1;
```

```initial
  let result = b;
  if (a > b) {
    result = a;
  }

  let i = 1;
```

```transformation
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
```

```transformation
    if (b % i == 0 && a % i == 0) {
      result = i;
    }
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
  return a;
```

```final
  #(ignore-test)
  return b;
```

```js
function gcd(a, b) {
  while (i >= a && i >= b) {
    //
  }
}
```

```js
function gcd(a, b) {
  while (i >= b && i >= a) {
    //
  }
}
```
