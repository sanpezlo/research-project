---
Write a JavaScript function that returns the average of an array of numbers using a "while" loop.
---

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```initial
  let sum = 1;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let sum = 1;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let sum = 1;
```

```transformation
    sum += numbers[i];
    i++;
```

```final
  return sum / numbers.length;
```

```js
function average(numbers) {
  while (i < numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (i <= numbers.length - 1) {
    //
  }
}
```

```js
function average(numbers) {
  while (i + 1 <= numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length > i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length - 1 >= i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length >= i + 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
  let i = 1;
```

```initial
  let i = 1;
  let sum = 0;
```

```initial
  let sum = 1;
  let i = 1;
```

```initial
  let i = 1;
  let sum = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let sum = 1;
  let i = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 1;
  let sum = 1;
```

```transformation
    sum += numbers[i - 1];
    i++;
```

```final
  return sum / numbers.length;
```

```js
function average(numbers) {
  while (i <= numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (i < numbers.length + 1) {
    //
  }
}
```

```js
function average(numbers) {
  while (i - 1 < numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length >= i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length + 1 > i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length > i - 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 0;
```

```initial
  let sum = 1;
  let i = 0;
```

```initial
  let i = 0;
  let sum = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let sum = 1;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let sum = 1;
```

```transformation
    sum += numbers[i] / numbers.length;
    i++;
```

```final
  return sum;
```

```js
function average(numbers) {
  while (i < numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (i <= numbers.length - 1) {
    //
  }
}
```

```js
function average(numbers) {
  while (i + 1 <= numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length > i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length - 1 >= i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length >= i + 1) {
    //
  }
}
```

===

```initial
  let sum = 0;
  let i = 1;
```

```initial
  let i = 1;
  let sum = 0;
```

```initial
  let sum = 1;
  let i = 1;
```

```initial
  let i = 1;
  let sum = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let sum = 1;
  let i = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 1;
  let sum = 1;
```

```transformation
    sum += numbers[i - 1] / numbers.length;
    i++;
```

```final
  return sum;
```

```js
function average(numbers) {
  while (i <= numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (i < numbers.length + 1) {
    //
  }
}
```

```js
function average(numbers) {
  while (i - 1 < numbers.length) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length >= i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length + 1 > i) {
    //
  }
}
```

```js
function average(numbers) {
  while (numbers.length > i - 1) {
    //
  }
}
```
