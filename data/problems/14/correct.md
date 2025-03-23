---
Write a JavaScript function that returns the greatest common divisor of two numbers using a "while" loop.
---

```js
function gcd(a, b) {
  while (b != 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b != 0) {
    let temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b >= 1) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b >= 1) {
    let temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b > 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b > 0) {
    let temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b) {
    let temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b) {
    let temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  let result = Math.max(a, b);
  let i = 1;
  while (i <= a && i <= b) {
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
  }
  return result;
}
```

```js
function gcd(a, b) {
  let result = Math.max(a, b);
  let i = 0;
  while (i <= a && i <= b) {
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
  }
  return result;
}
```

```js
function gcd(a, b) {
  let result = a;
  if (b > a) {
    result = b;
  }

  let i = 1;
  while (i <= a && i <= b) {
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
  }
  return result;
}
```

```js
function gcd(a, b) {
  let result = a;
  if (a < b) {
    result = b;
  }

  let i = 1;
  while (i <= a && i <= b) {
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
  }
  return result;
}
```

```js
function gcd(a, b) {
  let result = b;
  if (b < a) {
    result = a;
  }

  let i = 1;
  while (i <= a && i <= b) {
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
  }
  return result;
}
```

```js
function gcd(a, b) {
  let result = b;
  if (a > b) {
    result = a;
  }

  let i = 1;
  while (i <= a && i <= b) {
    if (a % i == 0 && b % i == 0) {
      result = i;
    }
    i++;
  }
  return result;
}
```

```js
function gcd(a, b) {
  if (Math.min(a, b) == 0) {
    return Math.max(a, b);
  }

  while (b != 0) {
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
  return a;
}
```

```js
function gcd(a, b) {
  if (Math.min(a, b) == 0) {
    return Math.max(a, b);
  }

  while (b >= 1) {
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
  return a;
}
```

```js
function gcd(a, b) {
  if (Math.min(a, b) == 0) {
    return Math.max(a, b);
  }

  while (b > 0) {
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
  return a;
}
```

```js
function gcd(a, b) {
  if (Math.min(a, b) == 0) {
    return Math.max(a, b);
  }

  while (b) {
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b != 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b != 0) {
    const temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b >= 1) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b >= 1) {
    const temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b > 0) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b > 0) {
    const temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b) {
    const temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}
```

```js
function gcd(a, b) {
  while (b) {
    const temp = b;
    b = a - b * Math.floor(a / b);
    a = temp;
  }
  return a;
}
```

```js
function gcd(n1, n2) {
  while (n2 != 0) {
    let t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 != 0) {
    let t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 >= 1) {
    let t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 >= 1) {
    let t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 > 0) {
    let t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 > 0) {
    let t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2) {
    let t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2) {
    let t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  let x = Math.max(n1, n2);
  let count = 1;
  while (count <= n1 && count <= n2) {
    if (n1 % count == 0 && n2 % count == 0) {
      x = count;
    }
    count++;
  }
  return x;
}
```

```js
function gcd(n1, n2) {
  let x = Math.max(n1, n2);
  let count = 0;
  while (count <= n1 && count <= n2) {
    if (n1 % count == 0 && n2 % count == 0) {
      x = count;
    }
    count++;
  }
  return x;
}
```

```js
function gcd(n1, n2) {
  let x = n1;
  if (n2 > n1) {
    x = n2;
  }

  let count = 1;
  while (count <= n1 && count <= n2) {
    if (n1 % count == 0 && n2 % count == 0) {
      x = count;
    }
    count++;
  }
  return x;
}
```

```js
function gcd(n1, n2) {
  let x = n1;
  if (n1 < n2) {
    x = n2;
  }

  let count = 1;
  while (count <= n1 && count <= n2) {
    if (n1 % count == 0 && n2 % count == 0) {
      x = count;
    }
    count++;
  }
  return x;
}
```

```js
function gcd(n1, n2) {
  let x = n2;
  if (n2 < n1) {
    x = n1;
  }

  let count = 1;
  while (count <= n1 && count <= n2) {
    if (n1 % count == 0 && n2 % count == 0) {
      x = count;
    }
    count++;
  }
  return x;
}
```

```js
function gcd(n1, n2) {
  let x = n2;
  if (n1 > n2) {
    x = n1;
  }

  let count = 1;
  while (count <= n1 && count <= n2) {
    if (n1 % count == 0 && n2 % count == 0) {
      x = count;
    }
    count++;
  }
  return x;
}
```

```js
function gcd(n1, n2) {
  if (Math.min(n1, n2) == 0) {
    return Math.max(n1, n2);
  }

  while (n2 != 0) {
    if (n1 > n2) {
      n1 -= n2;
    } else {
      n2 -= n1;
    }
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  if (Math.min(n1, n2) == 0) {
    return Math.max(n1, n2);
  }

  while (n2 >= 1) {
    if (n1 > n2) {
      n1 -= n2;
    } else {
      n2 -= n1;
    }
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  if (Math.min(n1, n2) == 0) {
    return Math.max(n1, n2);
  }

  while (n2 > 0) {
    if (n1 > n2) {
      n1 -= n2;
    } else {
      n2 -= n1;
    }
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  if (Math.min(n1, n2) == 0) {
    return Math.max(n1, n2);
  }

  while (n2) {
    if (n1 > n2) {
      n1 -= n2;
    } else {
      n2 -= n1;
    }
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 != 0) {
    const t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 != 0) {
    const t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 >= 1) {
    const t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 >= 1) {
    const t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 > 0) {
    const t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2 > 0) {
    const t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2) {
    const t = n2;
    n2 = n1 % n2;
    n1 = t;
  }
  return n1;
}
```

```js
function gcd(n1, n2) {
  while (n2) {
    const t = n2;
    n2 = n1 - n2 * Math.floor(n1 / n2);
    n1 = t;
  }
  return n1;
}
```
