---
Write a JavaScript function that returns in an array the even numbers from 1 to N using a while loop.
---

```initial
  let result = [];
  let i = 2;
```

```initial
  let i = 2;
  let result = [];
```

```initial
  const result = [];
  let i = 2;
```

```initial
  let i = 2;
  const result = [];
```

```transformation
    i += 2;
```

```transformation
    result.push(i);
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

===

```initial
  let result = [];
  let i = 2;
```

```initial
  let i = 2;
  let result = [];
```

```initial
  const result = [];
  let i = 2;
```

```initial
  let i = 2;
  const result = [];
```

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
    i++;
```

```transformation
    if (i % 2 == 1) {
      result.push(i);
    }
    i++;
```

```transformation
    if (i % 2 != 0) {
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

======

```initial
  let result = [];
  let i = 2;
```

```initial
  let i = 2;
  let result = [];
```

```initial
  const result = [];
  let i = 2;
```

```initial
  let i = 2;
  const result = [];
```

```transformation
    #(ignore-test)
    result.push(i);
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result.push(i);
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
  let result = [];
  let i = 2;
```

```initial
  let i = 2;
  let result = [];
```

```initial
  const result = [];
  let i = 2;
```

```initial
  let i = 2;
  const result = [];
```

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
    #(ignore-test)
    if (i % 2 != 1) {
      result.push(i);
    }
```

```transformation
    #(ignore-test)
    if (i % 2 == 0) {
      result.push(i);
    }
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    if (i % 2 == 1) {
      result.push(i);
    }
```

```transformation
    #(ignore-test)
    if (i % 2 != 0) {
      result.push(i);
    }
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
