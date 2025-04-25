---
Write a JavaScript function that returns in an array the first N numbers of the sequence: a(N) = a^N + a (N-1) + N using a "while" loop.
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
    let value = a ** i + a * (i - 1) + i;
    result.push(value);
    i++;
```

```transformation
    let value = a ** i + a * (i - 1) + i;
    i++;
    result.push(value);
```

```transformation
    result.push(a ** i + a * (i - 1) + i);
    i++;
```

```transformation
    let value = Math.pow(a, i) + a * (i - 1) + i;
    result.push(value);
    i++;
```

```transformation
    let value = Math.pow(a, i) + a * (i - 1) + i;
    i++;
    result.push(value);
```

```transformation
    result.push(Math.pow(a, i) + a * (i - 1) + i);
    i++;
```

```final
  return result;
```

```js
function sequence(a, n) {
  while (i <= n) {
    //
  }
}
```

```js
function sequence(a, n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function sequence(a, n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function sequence(a, n) {
  while (n >= i) {
    //
  }
}
```

```js
function sequence(a, n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function sequence(a, n) {
  while (n > i - 1) {
    //
  }
}
```
