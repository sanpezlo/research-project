---
Write a JavaScript function that returns the least common multiple of two numbers using a "while" loop.
---

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
```

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
```

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = Math.max(a, b);
```

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = Math.max(a, b);
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = Math.max(a, b);
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = Math.max(a, b);
```

```transformation
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result += max;
```

```transformation
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result++;
```

```transformation
    if (result % b == 0 && result % a == 0) {
      return result;
    }
    result++;
```

```final
  return result;
```

```js
function lcm(a, b) {
  while (true) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (result) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (result != 0) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (result > 0) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (result >= 1) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (result - 1 >= 0) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (result >= 0) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (0 != result) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (0 < result) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (1 <= result) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (0 <= result - 1) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (0 <= result) {
    //
  }
}
```

===

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
```

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
```

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = Math.max(a, b);
```

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = Math.max(a, b);
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = max;
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = max;
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let max = Math.max(a, b);
  let result = Math.max(a, b);
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  const max = Math.max(a, b);
  let result = Math.max(a, b);
```

```transformation
    result += max;
```

```final
  return result;
```

```js
function lcm(a, b) {
  while (result % a != 0 || result % b != 0) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (result % b != 0 || result % a != 0) {
    //
  }
}
```

===

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let result = Math.max(a, b);
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let result = Math.max(a, b);
```

```transformation
    if (result % a == 0 && result % b == 0) {
      return result;
    }
    result++;
```

```transformation
    if (result % b == 0 && result % a == 0) {
      return result;
    }
    result++;
```

```js
function lcm(a, b) {
  while (true) {
    //
  }
}
```

===

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let result = a;
  let temp = b;
```

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let temp = b;
  let result = a;
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let result = a;
  let temp = b;
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let temp = b;
  let result = a;
```

```transformation
    if (result < temp) {
      result += a;
    } else {
      temp += b;
    }
```

```final
  return result;
```

```js
function lcm(a, b) {
  while (result != temp) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (temp != result) {
    //
  }
}
```

===

```initial
  if (a == 0 || b == 0) {
    return 0;
  }

  let result = a;
```

```initial
  if (b == 0 || a == 0) {
    return 0;
  }

  let result = a;
```

```transformation
    result += a;
```

```final
  return result;
```

```js
function lcm(a, b) {
  while (result % b != 0) {
    //
  }
}
```

```js
function lcm(a, b) {
  while (0 != result % b) {
    //
  }
}
```
