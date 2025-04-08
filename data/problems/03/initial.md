---
Write a JavaScript function that returns in an array the numbers from 1 to N using a "while" loop.
---

```initial
  let numbers = [n];
  let i = 1;
```

```initial
  let i = 1;
  let numbers = [n];
```

```initial
  const numbers = [n];
  let i = 1;
```

```initial
  let i = 1;
  const numbers = [n];
```

```initial
  let numbers = [0];
  let i = 1;
```

```initial
  let i = 1;
  let numbers = [0];
```

```initial
  const numbers = [0];
  let i = 1;
```

```initial
  let i = 1;
  const numbers = [0];
```

```transformation
    numbers.push(i);
    i++;
```

```final
  return numbers;
```

```js
function count(n) {
  while (i <= n) {
    //
  }
}
```

```js
function count(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function count(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function count(n) {
  while (n >= i) {
    //
  }
}
```

```js
function count(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function count(n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let numbers = [n];
  let i = 1;
```

```initial
  let i = 1;
  let numbers = [n];
```

```initial
  let numbers = [0];
  let i = 1;
```

```initial
  let i = 1;
  let numbers = [0];
```

```transformation
    numbers = numbers.concat([i]);
    i++;
```

```final
  return numbers;
```

```js
function count(n) {
  while (i <= n) {
    //
  }
}
```

```js
function count(n) {
  while (i < n + 1) {
    //
  }
}
```

```js
function count(n) {
  while (i - 1 < n) {
    //
  }
}
```

```js
function count(n) {
  while (n >= i) {
    //
  }
}
```

```js
function count(n) {
  while (n + 1 > i) {
    //
  }
}
```

```js
function count(n) {
  while (n > i - 1) {
    //
  }
}
```

===

```initial
  let numbers = [n];
  let i = 0;
```

```initial
  let i = 0;
  let numbers = [n];
```

```initial
  const numbers = [n];
  let i = 0;
```

```initial
  let i = 0;
  const numbers = [n];
```

```initial
  let numbers = [0];
  let i = 0;
```

```initial
  let i = 0;
  let numbers = [0];
```

```initial
  const numbers = [0];
  let i = 0;
```

```initial
  let i = 0;
  const numbers = [0];
```

```transformation
    i++;
    numbers.push(i);
```

```final
  return numbers;
```

```js
function count(n) {
  while (i < n) {
    //
  }
}
```

```js
function count(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function count(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function count(n) {
  while (n > i) {
    //
  }
}
```

```js
function count(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function count(n) {
  while (n >= i + 1) {
    //
  }
}
```
