---
Write a JavaScript function that returns the square, cube and square root of all numbers from 1 to N using a "while" loop.
---

```initial
  let result = [];
  let i = 1;
```

```initial
  let i = 1;
  let result = [];
```

```initial
  const result = [];
  let i = 1;
```

```initial
  let i = 1;
  const result = [];
```

```transformation
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
```

```transformation
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
```

```transformation
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
```

```final
  return result;
```

```js
function calculatePowers(n) {
  while (i <= n) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (n >= i) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let i = 0;
```

```initial
  let i = 0;
  let result = [];
```

```initial
  const result = [];
  let i = 0;
```

```initial
  let i = 0;
  const result = [];
```

```transformation
    result.push({
      number: i + 1,
      square: (i + 1) ** 2,
      cube: (i + 1) ** 3,
      squareRoot: Math.sqrt(i + 1),
    });
    i++;
```

```transformation
    result.push({
      number: i + 1,
      square: Math.pow(i + 1, 2),
      cube: Math.pow(i + 1, 3),
      squareRoot: Math.pow(i + 1, 1 / 2),
    });
    i++;
```

```transformation
    result.push({
      number: i + 1,
      square: (i + 1) * (i + 1),
      cube: (i + 1) * (i + 1) * (i + 1),
      squareRoot: (i + 1) ** 0.5,
    });
    i++;
```

```final
  return result;
```

```js
function calculatePowers(n) {
  while (i < n) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (n > i) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function calculatePowers(n) {
  while (n >= i + 1) {
    //
  }
}
```
