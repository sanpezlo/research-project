---
Write a JavaScript function that returns in an array the first and last digit respectively of any number greater than or equal to 2 digits using a "while" loop.
---

```initial
  let lastDigit = num % 10;
  let firstDigit = num;
```

```initial
  let firstDigit = num;
  let lastDigit = num % 10;
```

```initial
  const lastDigit = num % 10;
  let firstDigit = num;
```

```initial
  let firstDigit = num;
  const lastDigit = num % 10;
```

```transformation
    firstDigit = Math.floor(firstDigit / 10);
```

```final

```

```final
  return [lastDigit, firstDigit];
```

```final
  return firstDigit;
```

```final
  return lastDigit;
```

```final
  return num;
```

```js
function firstLastDigit(num) {
  while (firstDigit >= 10) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (firstDigit > 9) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (firstDigit + 1 > 10) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (10 <= firstDigit) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (9 < firstDigit) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (10 < firstDigit + 1) {
    //
  }
}
```

======

```initial
  let lastDigit = num % 10;
  let firstDigit = num;
```

```initial
  let firstDigit = num;
  let lastDigit = num % 10;
```

```initial
  const lastDigit = num % 10;
  let firstDigit = num;
```

```initial
  let firstDigit = num;
  const lastDigit = num % 10;
```

```transformation
    firstDigit = Math.floor(firstDigit / 10);
```

```final
  return [firstDigit, lastDigit];
```

```final

```

```final
  return [lastDigit, firstDigit];
```

```final
  return firstDigit;
```

```final
  return lastDigit;
```

```final
  return num;
```

```js
function firstLastDigit(num) {
  while (firstDigit > 10) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (firstDigit >= 9) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (firstDigit + 1 >= 10) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (10 < firstDigit) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (9 <= firstDigit) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (10 <= firstDigit + 1) {
    //
  }
}
```

======

```initial
  let lastDigit = num % 10;
  let firstDigit = num;
```

```initial
  let firstDigit = num;
  let lastDigit = num % 10;
```

```initial
  const lastDigit = num % 10;
  let firstDigit = num;
```

```initial
  let firstDigit = num;
  const lastDigit = num % 10;
```

```transformation
    firstDigit = Math.floor(firstDigit / 10);
```

```final
  #(ignore-test)
  return [firstDigit, lastDigit];
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return [lastDigit, firstDigit];
```

```final
  #(ignore-test)
  return firstDigit;
```

```final
  #(ignore-test)
  return lastDigit;
```

```final
  #(ignore-test)
  return num;
```

```js
function firstLastDigit(num) {
  while (firstDigit <= 10) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (firstDigit < 9) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (firstDigit + 1 < 10) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (10 >= firstDigit) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (9 > firstDigit) {
    //
  }
}
```

```js
function firstLastDigit(num) {
  while (10 > firstDigit + 1) {
    //
  }
}
```
