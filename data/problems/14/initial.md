---
Write a JavaScript function that returns the greatest common divisor of two numbers using a "while" loop.
---

===

```initial
  if (Math.min(a, b) == 0) {
    return a;
  }
```

```initial
  if (0 == Math.min(a, b)) {
    return a;
  }
```

```initial
  if (Math.min(a, b) == 0) {
    return b;
  }
```

```initial
  if (0 == Math.min(a, b)) {
    return b;
  }
```

```initial
  #(ignore-test)
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
  let result = a;
  let i = 1;
```

```initial
  let result = a;
  let i = 0;
```

```initial
  let result = b;
  let i = 1;
```

```initial
  let result = b;
  let i = 0;
```

```initial
  let result = b;
  if (b > a) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = b;
  if (a < b) {
    result = b;
  }

  let i = 1;
```

```initial
  let result = a;
  if (b < a) {
    result = a;
  }

  let i = 1;
```

```initial
  let result = a;
  if (a > b) {
    result = a;
  }

  let i = 1;
```

```initial
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

```js
function gcd(a, b) {
  while (i <= a && i <= b) {
    //
  }
}
```
