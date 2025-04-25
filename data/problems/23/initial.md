---
Write a JavaScript function that returns in an array all factors of a number using a "while" loop.
---

```initial
  let factors = [0];
  let i = 1;
```

```initial
  let i = 1;
  let factors = [0];
```

```initial
  const factors = [0];
  let i = 1;
```

```initial
  let i = 1;
  const factors = [0];
```

```initial
  let factors = [0];
  let i = 0;
```

```initial
  let i = 0;
  let factors = [0];
```

```initial
  const factors = [0];
  let i = 0;
```

```initial
  let i = 0;
  const factors = [0];
```

```initial
  let factors = [num];
  let i = 1;
```

```initial
  let i = 1;
  let factors = [num];
```

```initial
  const factors = [num];
  let i = 1;
```

```initial
  let i = 1;
  const factors = [num];
```

```initial
  let factors = [num];
  let i = 0;
```

```initial
  let i = 0;
  let factors = [num];
```

```initial
  const factors = [num];
  let i = 0;
```

```initial
  let i = 0;
  const factors = [num];
```

```transformation
    if (num % i == 0) {
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
