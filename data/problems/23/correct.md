---
Write a JavaScript function that returns the length of a number using a "while" loop.
---

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num > 0) {
    num = Math.floor(num / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num >= 1) {
    num = Math.floor(num / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num != 0) {
    num = Math.floor(num / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num) {
    num = Math.floor(num / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num > 0) {
    length++;
    num = Math.floor(num / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num >= 1) {
    length++;
    num = Math.floor(num / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num != 0) {
    length++;
    num = Math.floor(num / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  while (num) {
    length++;
    num = Math.floor(num / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let length = 1;
  while (num >= 10) {
    num = Math.floor(num / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let length = 1;
  while (num > 9) {
    num = Math.floor(num / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let length = 0;
  while (num >= 10) {
    num = Math.floor(num / 10);
    length++;
  }
  return length + 1;
}
```

```js
function lengthOfNumber(num) {
  let length = 0;
  while (num > 9) {
    num = Math.floor(num / 10);
    length++;
  }
  return length + 1;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp > 0) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp >= 1) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp != 0) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp > 0) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp >= 1) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp != 0) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let temp = num;
  let length = 0;
  while (temp) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let temp = num;
  let length = 1;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let temp = num;
  let length = 1;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let temp = num;
  let length = 0;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length + 1;
}
```

```js
function lengthOfNumber(num) {
  let temp = num;
  let length = 0;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length + 1;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp > 0) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp >= 1) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp != 0) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp > 0) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp >= 1) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp != 0) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  if (num == 0) {
    return 1;
  }
  let length = 0;
  let temp = num;
  while (temp) {
    length++;
    temp = Math.floor(temp / 10);
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let length = 1;
  let temp = num;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let length = 1;
  let temp = num;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length;
}
```

```js
function lengthOfNumber(num) {
  let length = 0;
  let temp = num;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length + 1;
}
```

```js
function lengthOfNumber(num) {
  let length = 0;
  let temp = num;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
    length++;
  }
  return length + 1;
}
```
