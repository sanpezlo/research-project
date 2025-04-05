---
Write a JavaScript function that returns whether a number is an Armstrong number using a "while" loop.
---

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp > 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp > 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp > 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp > 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp > 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp > 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp > 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp > 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp > 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp > 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp > 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp > 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp > 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp != 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp != 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp != 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp != 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp != 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp != 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp != 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp != 0) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp != 0) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp != 0) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp != 0) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp != 0) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp != 0) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0,
    temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let sum = 0;
  let temp = num;
  let digits = num.toString().length;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp >= 1) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp >= 1) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let sum = 0,
    temp = num;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp >= 1) {
    sum += Math.pow(temp % 10, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp >= 1) {
    sum += (temp % 10) ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp >= 1) {
    let digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += digit ** digits;
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(num) {
  let digits = num.toString().length;
  let temp = num;
  let sum = 0;
  while (temp >= 1) {
    const digit = temp % 10;
    sum += Math.pow(digit, digits);
    temp = Math.floor(temp / 10);
  }
  return sum == num;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t > 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t > 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t > 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t > 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t > 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t > 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t > 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t > 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t > 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t > 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t > 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t > 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t > 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t > 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t > 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t > 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t > 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t > 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t > 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t > 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t > 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t > 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t > 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t > 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t != 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t != 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t != 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t != 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t != 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t != 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t != 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t != 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t != 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t != 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t != 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t != 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t != 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t != 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t != 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t != 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t != 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t != 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t != 0) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t != 0) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t != 0) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t != 0) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t != 0) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t != 0) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t >= 1) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t >= 1) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t >= 1) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t >= 1) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t >= 1) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0,
    t = n;
  const d = n.toString().length;
  while (t >= 1) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t >= 1) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t >= 1) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t >= 1) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t >= 1) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t >= 1) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  let s = 0;
  let t = n;
  const d = n.toString().length;
  while (t >= 1) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t >= 1) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t >= 1) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t >= 1) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t >= 1) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t >= 1) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let s = 0,
    t = n;
  while (t >= 1) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t >= 1) {
    s += Math.pow(t % 10, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t >= 1) {
    s += (t % 10) ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t >= 1) {
    let l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t >= 1) {
    let l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t >= 1) {
    const l = t % 10;
    s += l ** d;
    t = Math.floor(t / 10);
  }
  return s == n;
}
```

```js
function isArmstrongNumber(n) {
  const d = n.toString().length;
  let t = n;
  let s = 0;
  while (t >= 1) {
    const l = t % 10;
    s += Math.pow(l, d);
    t = Math.floor(t / 10);
  }
  return s == n;
}
```
