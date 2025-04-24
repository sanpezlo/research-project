---
Write a JavaScript function that returns the largest number from an array of numbers using a "while" loop.
---

```initial
  let max = numbers[0];
  let i = 0;
```

```initial
  let i = 0;
  let max = numbers[0];
```

```initial
  let max = numbers[0];
  let i = 1;
```

```initial
  let i = 1;
  let max = numbers[0];
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let max = 0;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let max = 0;
```

```transformation
    i++;
```

```transformation
    if (numbers[i] < max) {
      max = numbers[i];
    }
    i++;
```

```transformation
    if (numbers[i] - 1 <= max) {
      max = numbers[i];
    }
    i++;
```

```transformation
    if (numbers[i] <= max + 1) {
      max = numbers[i];
    }
    i++;
```

```transformation
    if (max > numbers[i]) {
      max = numbers[i];
    }
    i++;
```

```transformation
    if (max >= numbers[i] - 1) {
      max = numbers[i];
    }
    i++;
```

```transformation
    if (max + 1 >= numbers[i]) {
      max = numbers[i];
    }
    i++;
```

```final
  return max;
```

```js
function max(numbers) {
  while (i < numbers.length) {
    //
  }
}
```

```js
function max(numbers) {
  while (i <= numbers.length - 1) {
    //
  }
}
```

```js
function max(numbers) {
  while (i + 1 <= numbers.length) {
    //
  }
}
```

```js
function max(numbers) {
  while (numbers.length > i) {
    //
  }
}
```

```js
function max(numbers) {
  while (numbers.length - 1 >= i) {
    //
  }
}
```

```js
function max(numbers) {
  while (numbers.length >= i + 1) {
    //
  }
}
```

======

```initial
  let max = numbers[0];
  let i = 0;
```

```initial
  let i = 0;
  let max = numbers[0];
```

```initial
  let max = numbers[0];
  let i = 1;
```

```initial
  let i = 1;
  let max = numbers[0];
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let max = 0;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let max = 0;
```

```transformation

```

```transformation
    if (numbers[i] > max) {
      max = numbers[i];
    }
```

```transformation
    if (numbers[i] - 1 >= max) {
      max = numbers[i];
    }
```

```transformation
    if (numbers[i] >= max + 1) {
      max = numbers[i];
    }
```

```transformation
    if (max < numbers[i]) {
      max = numbers[i];
    }
```

```transformation
    if (max <= numbers[i] - 1) {
      max = numbers[i];
    }
```

```transformation
    if (max + 1 <= numbers[i]) {
      max = numbers[i];
    }
```

```transformation
    if (numbers[i] < max) {
      max = numbers[i];
    }
```

```transformation
    if (numbers[i] - 1 <= max) {
      max = numbers[i];
    }
```

```transformation
    if (numbers[i] <= max + 1) {
      max = numbers[i];
    }
```

```transformation
    if (max > numbers[i]) {
      max = numbers[i];
    }
```

```transformation
    if (max >= numbers[i] - 1) {
      max = numbers[i];
    }
```

```transformation
    if (max + 1 >= numbers[i]) {
      max = numbers[i];
    }
```

```final
  #(ignore-test)
  return max;
```

```js
function max(numbers) {
  while (i < numbers.length) {
    //
  }
}
```

```js
function max(numbers) {
  while (i <= numbers.length - 1) {
    //
  }
}
```

```js
function max(numbers) {
  while (i + 1 <= numbers.length) {
    //
  }
}
```

```js
function max(numbers) {
  while (numbers.length > i) {
    //
  }
}
```

```js
function max(numbers) {
  while (numbers.length - 1 >= i) {
    //
  }
}
```

```js
function max(numbers) {
  while (numbers.length >= i + 1) {
    //
  }
}
```
