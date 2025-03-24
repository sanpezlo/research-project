---
Write a JavaScript function that returns the least common multiple of two numbers using a "while" loop.
---

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
  while (result) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
  while (result > 0) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
  while (result >= 0) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
  while (result >= 1) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
  while (result % a != 0 || result % b != 0) {
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = Math.max(a, b);
  while (true) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
  while (result) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
  while (result > 0) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
  while (result >= 0) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
  while (result >= 1) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
  while (result % a != 0 || result % b != 0) {
    result += max;
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = Math.max(a, b);
  while (true) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
  }
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let result = Math.max(a, b);
  while (true) {
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result++;
  }
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let result = a;
  let temp = b;
  while (result != temp) {
    if (result < temp) {
      result += a;
    } else {
      temp += b;
    }
  }
  return result;
}
```

```js
function lcm(a, b) {
  if (a == 0 || b == 0) {
    return 0;
  }

  let result = a;
  while (result % b != 0) {
    result += a;
  }
  return result;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let m = Math.max(num1, num2);
  let r = m;
  while (r) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let m = Math.max(num1, num2);
  let r = m;
  while (r > 0) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let m = Math.max(num1, num2);
  let r = m;
  while (r >= 0) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let m = Math.max(num1, num2);
  let r = m;
  while (r >= 1) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let m = Math.max(num1, num2);
  let r = m;
  while (r % num1 != 0 || r % num2 != 0) {
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let m = Math.max(num1, num2);
  let r = Math.max(num1, num2);
  while (true) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  const m = Math.max(num1, num2);
  let r = m;
  while (r) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  const m = Math.max(num1, num2);
  let r = m;
  while (r > 0) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  const m = Math.max(num1, num2);
  let r = m;
  while (r >= 0) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  const m = Math.max(num1, num2);
  let r = m;
  while (r >= 1) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  const m = Math.max(num1, num2);
  let r = m;
  while (r % num1 != 0 || r % num2 != 0) {
    r += m;
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  const m = Math.max(num1, num2);
  let r = Math.max(num1, num2);
  while (true) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r += m;
  }
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let r = Math.max(num1, num2);
  while (true) {
    if (r % num1 == 0 && r % num2 == 0) {
      return r;
    }
    r++;
  }
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let r = num1;
  let t = num2;
  while (r != t) {
    if (r < t) {
      r += num1;
    } else {
      t += num2;
    }
  }
  return r;
}
```

```js
function lcm(num1, num2) {
  if (num1 == 0 || num2 == 0) {
    return 0;
  }

  let r = num1;
  while (r % num2 != 0) {
    r += num1;
  }
  return r;
}
```
