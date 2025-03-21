---
Write a JavaScript function that returns the largest number from an array of numbers using a "while" loop.
---

```js
function max(numbers) {
  let max = numbers[0];
  let i = 0;
  while (i < numbers.length) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let max = numbers[0];
  let i = 0;
  while (i <= numbers.length - 1) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let max = numbers[0];
  let i = 0;
  while (i < numbers.length) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let max = numbers[0];
  let i = 0;
  while (i <= numbers.length - 1) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let max = numbers[0];
  let i = 0;
  while (i <= numbers.length - 1) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let max = numbers[0];
  let i = 1;
  while (i <= numbers.length - 1) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let max = numbers[0];
  let i = 1;
  while (i < numbers.length) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let max = numbers[0];
  let i = 1;
  while (i <= numbers.length - 1) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let max = Number.MIN_VALUE;
  let i = 0;
  while (i < numbers.length) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let max = Number.MIN_VALUE;
  let i = 0;
  while (i <= numbers.length - 1) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let max = Number.MIN_VALUE;
  let i = 0;
  while (i < numbers.length) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let max = Number.MIN_VALUE;
  let i = 0;
  while (i <= numbers.length - 1) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 0;
  let max = numbers[0];
  while (i < numbers.length) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 0;
  let max = numbers[0];
  while (i <= numbers.length - 1) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 0;
  let max = numbers[0];
  while (i < numbers.length) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 0;
  let max = numbers[0];
  while (i <= numbers.length - 1) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 1;
  let max = numbers[0];
  while (i < numbers.length) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 1;
  let max = numbers[0];
  while (i <= numbers.length - 1) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 1;
  let max = numbers[0];
  while (i < numbers.length) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  let i = 1;
  let max = numbers[0];
  while (i <= numbers.length - 1) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let max = Number.MIN_VALUE;
  while (i < numbers.length) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let max = Number.MIN_VALUE;
  while (i <= numbers.length - 1) {
    if (numbers[i] > max) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let max = Number.MIN_VALUE;
  while (i < numbers.length) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```

```js
function max(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let max = Number.MIN_VALUE;
  while (i <= numbers.length - 1) {
    if (max < numbers[i]) {
      max = numbers[i];
    }
    i++;
  }
  return max;
}
```
