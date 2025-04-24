---
Write a JavaScript function that returns the smallest number from an array of numbers using a "while" loop.
---

```initial
  let min = 0;
  let i = 0;
```

```initial
  let i = 0;
  let min = 0;
```

```initial
  let min = 0;
  let i = 1;
```

```initial
  let i = 1;
  let min = 0;
```

```initial
  let min = Number.MAX_VALUE;
  let i = 0;
```

```initial
  let i = 0;
  let min = Number.MAX_VALUE;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let min = 0;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let min = 0;
```

```transformation
    if (numbers[i] < min) {
      min = numbers[i];
    }
    i++;
```

```transformation
    if (numbers[i] <= min - 1) {
      min = numbers[i];
    }
    i++;
```

```transformation
    if (numbers[i] + 1 <= min) {
      min = numbers[i];
    }
    i++;
```

```transformation
    if (min > numbers[i]) {
      min = numbers[i];
    }
    i++;
```

```transformation
    if (min - 1 >= numbers[i]) {
      min = numbers[i];
    }
    i++;
```

```transformation
    if (min >= numbers[i] + 1) {
      min = numbers[i];
    }
    i++;
```

```final
  return min;
```

```js
function min(numbers) {
  while (i < numbers.length) {
    //
  }
}
```

```js
function min(numbers) {
  while (i <= numbers.length - 1) {
    //
  }
}
```

```js
function min(numbers) {
  while (i + 1 <= numbers.length) {
    //
  }
}
```

```js
function min(numbers) {
  while (numbers.length > i) {
    //
  }
}
```

```js
function min(numbers) {
  while (numbers.length - 1 >= i) {
    //
  }
}
```

```js
function min(numbers) {
  while (numbers.length >= i + 1) {
    //
  }
}
```
