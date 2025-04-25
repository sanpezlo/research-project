---
Write a JavaScript function that returns whether a number is an Armstrong number using a "while" loop.
---

```initial
  let sum = 1;
  let temp = num;
  let digits = num.toString().length;
```

```initial
  let digits = num.toString().length;
  let sum = 1;
  let temp = num;
```

```initial
  let digits = num.toString().length;
  let sum = 1;
  let temp = num;
```

```transformation
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
```

```transformation
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
```

```transformation
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
```

```transformation
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
```

```transformation
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
```

```transformation
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
```

```final
  return sum == num;
```

```js
function isArmstrongNumber(num) {
  while (temp) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (temp != 0) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (temp > 0) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (temp >= 1) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (temp - 1 >= 0) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (0 != temp) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (0 < temp) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (1 <= temp) {
    //
  }
}
```

```js
function isArmstrongNumber(num) {
  while (0 <= temp - 1) {
    //
  }
}
```
