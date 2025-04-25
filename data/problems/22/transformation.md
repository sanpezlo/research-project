---
Write a JavaScript function that returns the length of a number using a "while" loop.
---

```initial
  if (num == 0) {
    return 1;
  }

  let length = 0;
```

```initial
  if (0 == num) {
    return 1;
  }

  let length = 0;
```

```transformation
    num = Math.floor(num / 10);
```

```final
  return length;
```

```js
function lengthOfNumber(num) {
  while (num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num != 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num > 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num >= 1) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num - 1 >= 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 != num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 < num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (1 <= num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 <= num - 1) {
    //
  }
}
```

===

```initial
  let length = 1;
```

```transformation
    num = Math.floor(num / 10);
```

```final
  return length;
```

```js
function lengthOfNumber(num) {
  while (num >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < num + 1) {
    //
  }
}
```

===

```initial
  let length = 0;
```

```transformation
    num = Math.floor(num / 10);
```

```final
  return length + 1;
```

```js
function lengthOfNumber(num) {
  while (num >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < num + 1) {
    //
  }
}
```

===

```initial
  if (num == 0) {
    return 1;
  }

  let temp = num;
  let length = 0;
```

```initial
  if (num == 0) {
    return 1;
  }

  let length = 0;
  let temp = num;
```

```initial
  if (0 == num) {
    return 1;
  }

  let temp = num;
  let length = 0;
```

```initial
  if (0 == num) {
    return 1;
  }

  let length = 0;
  let temp = num;
```

```transformation
    temp = Math.floor(temp / 10);
```

```final
  return length;
```

```js
function lengthOfNumber(num) {
  while (temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp != 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp > 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp >= 1) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp - 1 >= 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 != temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 < temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (1 <= temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 <= temp - 1) {
    //
  }
}
```

===

```initial
  let temp = num;
  let length = 1;
```

```initial
  let length = 1;
  let temp = num;
```

```transformation
    temp = Math.floor(temp / 10);
```

```final
  return length;
```

```js
function lengthOfNumber(num) {
  while (temp >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < temp + 1) {
    //
  }
}
```

===

```initial
  let temp = num;
  let length = 0;
```

```initial
  let length = 0;
  let temp = num;
```

```transformation
    temp = Math.floor(temp / 10);
```

```final
  return length + 1;
```

```js
function lengthOfNumber(num) {
  while (temp >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < temp + 1) {
    //
  }
}
```

======

```initial
  if (num == 0) {
    return 1;
  }

  let length = 0;
```

```initial
  if (0 == num) {
    return 1;
  }

  let length = 0;
```

```transformation
    length++;
```

```transformation

```

```final
  #(ignore-test)
  return length;
```

```js
function lengthOfNumber(num) {
  while (num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num != 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num > 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num >= 1) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num - 1 >= 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 != num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 < num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (1 <= num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 <= num - 1) {
    //
  }
}
```

===

```initial
  let length = 1;
```

```transformation
    length++;
```

```transformation

```

```final
  #(ignore-test)
  return length;
```

```js
function lengthOfNumber(num) {
  while (num >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < num + 1) {
    //
  }
}
```

===

```initial
  let length = 0;
```

```transformation
    length++;
```

```transformation

```

```final
  #(ignore-test)
  return length + 1;
```

```js
function lengthOfNumber(num) {
  while (num >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (num + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < num) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < num + 1) {
    //
  }
}
```

===

```initial
  if (num == 0) {
    return 1;
  }

  let temp = num;
  let length = 0;
```

```initial
  if (num == 0) {
    return 1;
  }

  let length = 0;
  let temp = num;
```

```initial
  if (0 == num) {
    return 1;
  }

  let temp = num;
  let length = 0;
```

```initial
  if (0 == num) {
    return 1;
  }

  let length = 0;
  let temp = num;
```

```transformation
    length++;
```

```transformation

```

```final
  #(ignore-test)
  return length;
```

```js
function lengthOfNumber(num) {
  while (temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp != 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp > 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp >= 1) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp - 1 >= 0) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 != temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 < temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (1 <= temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (0 <= temp - 1) {
    //
  }
}
```

===

```initial
  let temp = num;
  let length = 1;
```

```initial
  let length = 1;
  let temp = num;
```

```transformation
    length++;
```

```transformation

```

```final
  #(ignore-test)
  return length;
```

```js
function lengthOfNumber(num) {
  while (temp >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < temp + 1) {
    //
  }
}
```

===

```initial
  let temp = num;
  let length = 0;
```

```initial
  let length = 0;
  let temp = num;
```

```transformation
    length++;
```

```transformation

```

```final
  #(ignore-test)
  return length + 1;
```

```js
function lengthOfNumber(num) {
  while (temp >= 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp > 9) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (temp + 1 > 10) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 <= temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (9 < temp) {
    //
  }
}
```

```js
function lengthOfNumber(num) {
  while (10 < temp + 1) {
    //
  }
}
```
