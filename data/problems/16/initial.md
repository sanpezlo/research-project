---
Write a JavaScript function that returns in an array the even numbers from 1 to N using a while loop.
---

```initial
  let result = [0];
  let i = 2;
```

```initial
  let i = 2;
  let result = [0];
```

```initial
  const result = [0];
  let i = 2;
```

```initial
  let i = 2;
  const result = [0];
```

```initial
  let result = [n];
  let i = 2;
```

```initial
  let i = 2;
  let result = [n];
```

```initial
  const result = [n];
  let i = 2;
```

```initial
  let i = 2;
  const result = [n];
```

```transformation
    result.push(i);
    i += 2;
```

```final
  return result;
```

```js
function evenNumbers(n) {
  while (i <= n) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (n >= i) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let result = [0];
  let i = 2;
```

```initial
  let i = 2;
  let result = [0];
```

```initial
  const result = [0];
  let i = 2;
```

```initial
  let i = 2;
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

```initial
  let result = [n];
  let i = 2;
```

```initial
  let i = 2;
  let result = [n];
```

```initial
  const result = [n];
  let i = 2;
```

```initial
  let i = 2;
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

```transformation
    if (i % 2 != 1) {
      result.push(i);
    }
    i++;
```

```transformation
    if (i % 2 == 0) {
      result.push(i);
    }
    i++;
```

```final
  return result;
```

```js
function evenNumbers(n) {
  while (i <= n) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (n >= i) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function evenNumbers(n) {
  while (n > i - 1) {
    //
  }
}
```
