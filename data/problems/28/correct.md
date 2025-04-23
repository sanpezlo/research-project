---
Write a JavaScript function that returns the sum of two numbers without using the addition operator, instead using bitwise operators and a "while" loop.
---

```transformation
    let carry = a & b;
    a = a ^ b;
    b = carry << 1;
```

```transformation
    let carry = a & b;
    a = (a & ~b) | (b & ~a);
    b = carry << 1;
```

```transformation
    const carry = a & b;
    a = a ^ b;
    b = carry << 1;
```

```transformation
    const carry = a & b;
    a = (a & ~b) | (b & ~a);
    b = carry << 1;
```

```final
  return a;
```

```js
function addWithoutPlus(a, b) {
  while (b) {
    //
  }
}
```

```js
function addWithoutPlus(a, b) {
  while (b != 0) {
    //
  }
}
```

```js
function addWithoutPlus(a, b) {
  while (b > 0 || b < 0) {
    //
  }
}
```

```js
function addWithoutPlus(a, b) {
  while (0 != b) {
    //
  }
}
```

```js
function addWithoutPlus(a, b) {
  while (b < 0 || b > 0) {
    //
  }
}
```
