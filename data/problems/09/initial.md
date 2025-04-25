---
Write a JavaScript function that returns in an array the odd numbers from 1 to N using a "while" loop.
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
    result.push(i);
    i += 2;
```

```final
  return result;
```

```js
function oddNumbers(n) {
  while (i <= n) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (n >= i) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (n > i - 1) {
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
    if (i % 2 != 0) {
      result.push(i);
    }
    i++;
```

```transformation
    if (0 != i % 2) {
      result.push(i);
    }
    i++;
```

```transformation
    if (i % 2 == 1) {
      result.push(i);
    }
    i++;
```

```transformation
    if (1 == i % 2) {
      result.push(i);
    }
    i++;
```

```final
  return result;
```

```js
function oddNumbers(n) {
  while (i <= n) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (n >= i) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function oddNumbers(n) {
  while (n > i - 1) {
    //
  }
}
```
