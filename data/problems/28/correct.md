---
Write a JavaScript function that returns the sum of two numbers without using the addition operator, instead using bitwise operators and a "while" loop.
---

```js
function addWithoutPlus(a, b) {
  while (b != 0) {
    let carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(a, b) {
  while (b) {
    let carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(a, b) {
  while (b != 0) {
    let carry = a & b;
    a = (a & ~b) | (b & ~a);
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(a, b) {
  while (b) {
    let carry = a & b;
    a = (a & ~b) | (b & ~a);
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(a, b) {
  while (b != 0) {
    const carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(a, b) {
  while (b) {
    const carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(a, b) {
  while (b != 0) {
    const carry = a & b;
    a = (a & ~b) | (b & ~a);
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(a, b) {
  while (b) {
    const carry = a & b;
    a = (a & ~b) | (b & ~a);
    b = carry << 1;
  }
  return a;
}
```

```js
function addWithoutPlus(x, y) {
  while (x != 0) {
    let temp = y & x;
    y = y ^ x;
    x = temp << 1;
  }
  return y;
}
```

```js
function addWithoutPlus(x, y) {
  while (x) {
    let temp = y & x;
    y = y ^ x;
    x = temp << 1;
  }
  return y;
}
```

```js
function addWithoutPlus(x, y) {
  while (x != 0) {
    let temp = y & x;
    y = (y & ~x) | (x & ~y);
    x = temp << 1;
  }
  return y;
}
```

```js
function addWithoutPlus(x, y) {
  while (x) {
    let temp = y & x;
    y = (y & ~x) | (x & ~y);
    x = temp << 1;
  }
  return y;
}
```

```js
function addWithoutPlus(x, y) {
  while (x != 0) {
    const temp = y & x;
    y = y ^ x;
    x = temp << 1;
  }
  return y;
}
```

```js
function addWithoutPlus(x, y) {
  while (x) {
    const temp = y & x;
    y = y ^ x;
    x = temp << 1;
  }
  return y;
}
```

```js
function addWithoutPlus(x, y) {
  while (x != 0) {
    const temp = y & x;
    y = (y & ~x) | (x & ~y);
    x = temp << 1;
  }
  return y;
}
```

```js
function addWithoutPlus(x, y) {
  while (x) {
    const temp = y & x;
    y = (y & ~x) | (x & ~y);
    x = temp << 1;
  }
  return y;
}
```
