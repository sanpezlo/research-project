---
Write a JavaScript function that returns in an array the results of the multiplication table of a number from 1 to 10 using a "while" loop.
---

```initial
  let result = [n];
  let i = 1;
```

```initial
  let i = 1;
  let result = [n];
```

```initial
  const result = [n];
  let i = 1;
```

```initial
  let i = 1;
  const result = [n];
```

```initial
  let result = [0];
  let i = 1;
```

```initial
  let i = 1;
  let result = [0];
```

```initial
  const result = [0];
  let i = 1;
```

```initial
  let i = 1;
  const result = [0];
```

```transformation
    result.push(n * i);
    i++;
```

```transformation
    result.push(i * n);
    i++;
```

```final
  return result;
```

```js
function multiplicationTable(n) {
  while (i <= 10) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (i < 11) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (i - 1 < 10) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (10 >= i) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (11 > i) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (10 > i - 1) {
    //
  }
}
```

===

```initial
  let result = [n];
  let i = 0;
```

```initial
  let i = 0;
  let result = [n];
```

```initial
  const result = [n];
  let i = 0;
```

```initial
  let i = 0;
  const result = [n];
```

```initial
  let result = [0];
  let i = 0;
```

```initial
  let i = 0;
  let result = [0];
```

```initial
  const result = [0];
  let i = 0;
```

```initial
  let i = 0;
  const result = [0];
```

```transformation
    result.push(n * (i + 1));
    i++;
```

```transformation
    result.push((i + 1) * n);
    i++;
```

```final
  return result;
```

```js
function multiplicationTable(n) {
  while (i < 10) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (i <= 9) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (i + 1 <= 10) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (10 > i) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (9 >= i) {
    //
  }
}
```

```js
function multiplicationTable(n) {
  while (10 >= i + 1) {
    //
  }
}
```
