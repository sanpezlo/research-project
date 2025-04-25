---
Write a JavaScript function that returns in an array all factors of a number using a "while" loop.
---

```initial
  let factors = [];
  let i = 1;
```

```initial
  let i = 1;
  let factors = [];
```

```initial
  const factors = [];
  let i = 1;
```

```initial
  let i = 1;
  const factors = [];
```

```initial
  let factors = [];
  let i = 0;
```

```initial
  let i = 0;
  let factors = [];
```

```initial
  const factors = [];
  let i = 0;
```

```initial
  let i = 0;
  const factors = [];
```

```transformation
    i++;
```

```transformation
    if (num % i != 0) {
      factors.push(i);
    }
    i++;
```

```transformation
    if (num / i == 0) {
      factors.push(i);
    }
    i++;
```

```final
  return factors;
```

```js
function factorsOfNumber(num) {
  while (i <= num) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (i < num + 1) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (i - 1 < num) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (num >= i) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (num + 1 > i) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (num > i - 1) {
    //
  }
}
```

======

```initial
  let factors = [];
  let i = 1;
```

```initial
  let i = 1;
  let factors = [];
```

```initial
  const factors = [];
  let i = 1;
```

```initial
  let i = 1;
  const factors = [];
```

```initial
  let factors = [];
  let i = 0;
```

```initial
  let i = 0;
  let factors = [];
```

```initial
  const factors = [];
  let i = 0;
```

```initial
  let i = 0;
  const factors = [];
```

```transformation
    if (num % i == 0) {
      factors.push(i);
    }
```

```transformation

```

```transformation
    if (num % i != 0) {
      factors.push(i);
    }
```

```transformation
    if (num / i == 0) {
      factors.push(i);
    }
```

```final
  #(ignore-test)
  return factors;
```

```js
function factorsOfNumber(num) {
  while (i <= num) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (i < num + 1) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (i - 1 < num) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (num >= i) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (num + 1 > i) {
    //
  }
}
```

```js
function factorsOfNumber(num) {
  while (num > i - 1) {
    //
  }
}
```
