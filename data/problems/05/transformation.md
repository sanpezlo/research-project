---
Write a JavaScript function that returns the average of an array of numbers using a "while" loop.
---

```initial
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    sum += i;
    i++;
```

```transformation
    sum -= i;
    i++;
```

```transformation
    sum *= i;
    i++;
```

```transformation
    sum /= i;
    i++;
```

```transformation
    sum -= numbers[i];
    i++;
```

```transformation
    sum *= numbers[i];
    i++;
```

```transformation
    sum /= numbers[i];
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
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 1;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    sum += numbers[i];
    i++;
```

```transformation
    sum -= numbers[i];
    i++;
```

```transformation
    sum *= numbers[i];
    i++;
```

```transformation
    sum /= numbers[i];
    i++;
```

```transformation
    sum -= numbers[i - 1];
    i++;
```

```transformation
    sum *= numbers[i - 1];
    i++;
```

```transformation
    sum /= numbers[i - 1];
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
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    sum += numbers[i];
    i++;
```

```transformation
    sum -= numbers[i];
    i++;
```

```transformation
    sum *= numbers[i];
    i++;
```

```transformation
    sum /= numbers[i];
    i++;
```

```transformation
    sum -= numbers[i] / numbers.length;
    i++;
```

```transformation
    sum *= numbers[i] / numbers.length;
    i++;
```

```transformation
    sum /= numbers[i] / numbers.length;
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
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 1;
  let sum = 0;
```

```transformation
    i++;
```

```transformation
    sum += numbers[i] / numbers.length;
    i++;
```

```transformation
    sum -= numbers[i] / numbers.length;
    i++;
```

```transformation
    sum *= numbers[i] / numbers.length;
    i++;
```

```transformation
    sum /= numbers[i] / numbers.length;
    i++;
```

```transformation
    sum += numbers[i - 1] ;
    i++;
```

```transformation
    sum -= numbers[i - 1] ;
    i++;
```

```transformation
    sum *= numbers[i - 1] ;
    i++;
```

```transformation
    sum /= numbers[i - 1] ;
    i++;
```

```transformation
    sum -= numbers[i - 1] / numbers.length;
    i++;
```

```transformation
    sum *= numbers[i - 1] / numbers.length;
    i++;
```

```transformation
    sum /= numbers[i - 1] / numbers.length;
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

======

```initial
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let sum = 0;
```

```transformation

```

```transformation
    sum += i;
```

```transformation
    sum -= i;
```

```transformation
    sum *= i;
```

```transformation
    sum /= i;
```

```transformation
    sum += numbers[i];
```

```transformation
    sum -= numbers[i];
```

```transformation
    sum *= numbers[i];
```

```transformation
    sum /= numbers[i];
```

```final
  #(ignore-test)
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
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 1;
  let sum = 0;
```

```transformation

```

```transformation
    sum += numbers[i];
```

```transformation
    sum -= numbers[i];
```

```transformation
    sum *= numbers[i];
```

```transformation
    sum /= numbers[i];
```

```transformation
    sum += numbers[i - 1];
```

```transformation
    sum -= numbers[i - 1];
```

```transformation
    sum *= numbers[i - 1];
```

```transformation
    sum /= numbers[i - 1];
```

```final
  #(ignore-test)
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
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 0;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 0;
  let sum = 0;
```

```transformation

```

```transformation
    sum += numbers[i];
```

```transformation
    sum -= numbers[i];
```

```transformation
    sum *= numbers[i];
```

```transformation
    sum /= numbers[i];
```

```transformation
    sum += numbers[i] / numbers.length;
```

```transformation
    sum -= numbers[i] / numbers.length;
```

```transformation
    sum *= numbers[i] / numbers.length;
```

```transformation
    sum /= numbers[i] / numbers.length;
```

```final
  #(ignore-test)
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
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 1;
```

```initial
  if (numbers.length == 0) {
    return null;
  }

  let i = 1;
  let sum = 0;
```

```transformation

```

```transformation
    sum += numbers[i] / numbers.length;
```

```transformation
    sum -= numbers[i] / numbers.length;
```

```transformation
    sum *= numbers[i] / numbers.length;
```

```transformation
    sum /= numbers[i] / numbers.length;
```

```transformation
    sum += numbers[i - 1] ;
```

```transformation
    sum -= numbers[i - 1] ;
```

```transformation
    sum *= numbers[i - 1] ;
```

```transformation
    sum /= numbers[i - 1] ;
```

```transformation
    sum += numbers[i - 1] / numbers.length;
```

```transformation
    sum -= numbers[i - 1] / numbers.length;
```

```transformation
    sum *= numbers[i - 1] / numbers.length;
```

```transformation
    sum /= numbers[i - 1] / numbers.length;
```

```final
  #(ignore-test)
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
