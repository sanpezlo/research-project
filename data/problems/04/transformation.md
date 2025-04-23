---
Write a JavaScript function that returns whether a number is prime using a "while" loop.
---

```initial
  if (num <= 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 2;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 >= num) {
    return false;
  }

  let i = 2;
```

```initial
  if (2 > num) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let i = 2;
```

```transformation
    if (num % i != 0) {
      return false;
    }
    i++;
```

```transformation
    if (num / i == 0) {
      return false;
    }
    i++;
```

```transformation
    if (num * i == 0) {
      return false;
    }
    i++;
```

```transformation
    if (num - i == 0) {
      return false;
    }
    i++;
```

```transformation
    if (num + i == 0) {
      return false;
    }
    i++;
```

```transformation
    if (num / i != 0) {
      return false;
    }
    i++;
```

```transformation
    if (num * i != 0) {
      return false;
    }
    i++;
```

```transformation
    if (num - i != 0) {
      return false;
    }
    i++;
```

```transformation
    if (num + i != 0) {
      return false;
    }
    i++;
```

```transformation
    if (num % i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num % i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num % i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i != 0 && i != num) {
      return false;
    }
    i++;
```

```final
  return true;
```

```js
function isPrime(num) {
  while (i < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= num - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i + 1 <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) - 1 <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= Math.floor(num / 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < Math.floor(num / 2) + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < Math.floor(num / 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= num / 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < num / 2 + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < num / 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= Math.sqrt(num)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= num ** 0.5) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= Math.pow(num, 0.5)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num - 1 >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i * i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i * i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i * i - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i ** 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i ** 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i ** 2 - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= Math.pow(i, 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > Math.pow(i, 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= Math.pow(i, 2) - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.floor(num / 2) >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.floor(num / 2) + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.floor(num / 2) > i - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num / 2 >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num / 2 + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num / 2 > i - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.sqrt(num) >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num ** 0.5 >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(num, 0.5) >= i) {
    //
  }
}
```

===

```initial
  if (num <= 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 2;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 >= num) {
    return false;
  }

  let i = 2;
```

```initial
  if (2 > num) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let i = 2;
```

```transformation
    if (num % i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num % i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num % i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i == 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i == 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i != 0 && i == num) {
      return false;
    }
    i++;
```

```transformation
    if (num / i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num * i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num + i != 0 && i != num) {
      return false;
    }
    i++;
```

```transformation
    if (num - i != 0 && i != num) {
      return false;
    }
    i++;
```

```final
  return true;
```

```js
function isPrime(num) {
  while (i <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i - 1) {
    //
  }
}
```

===

```initial
  if (num == 1 || num == 0) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num == 0 || num == 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num == 1 || num == 0) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num == 0 || num == 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num <= 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num < 2) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (1 >= num) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (2 > num) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num <= 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (1 >= num) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (2 > num) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  let count = 0;
  let i = 1;
```

```initial
  let i = 1;
  let count = 0;
```

```transformation
    if (num % i != 0) {
      count++;
    }
    i++;
```

```transformation
    if (num / i == 0) {
      count++;
    }
    i++;
```

```transformation
    if (num * i == 0) {
      count++;
    }
    i++;
```

```transformation
    if (num + i == 0) {
      count++;
    }
    i++;
```

```transformation
    if (num - i == 0) {
      count++;
    }
    i++;
```

```transformation
    if (num / i != 0) {
      count++;
    }
    i++;
```

```transformation
    if (num * i != 0) {
      count++;
    }
    i++;
```

```transformation
    if (num + i != 0) {
      count++;
    }
    i++;
```

```transformation
    if (num - i != 0) {
      count++;
    }
    i++;
```

```final
  if (count > 2 || count < 2) {
    return false;
  } else {
    return true;
  }
```

```final
  if (count >= 3 || count <= 1) {
    return false;
  } else {
    return true;
  }
```

```final
  if (count == 2) {
    return true;
  } else {
    return false;
  }
```

```final
  return count == 2;
```

```final
  return !(count != 2);
```

```js
function isPrime(num) {
  while (i <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i - 1) {
    //
  }
}
```

===

```initial
  if (num <= 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 2;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 2;
```

```transformation
    i--;
```

```final
  return i * i > num;
```

```final
  return Math.pow(i, 2) > num;
```

```js
function isPrime(num) {
  while (i * i <= num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i < num + 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i - 1 < num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 <= num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 < num + 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 - 1 < num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) <= num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) < num + 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) - 1 < num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i * i && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i * i && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i * i - 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i ** 2 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i ** 2 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i ** 2 - 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= Math.pow(i, 2) && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > Math.pow(i, 2) && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > Math.pow(i, 2) - 1 && num % i != 0) {
    //
  }
}
```

======

```initial
  if (num <= 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 2;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 >= num) {
    return false;
  }

  let i = 2;
```

```initial
  if (2 > num) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let i = 2;
```

```transformation
    if (num % i == 0) {
      return false;
    }
```

```transformation
    if (num % i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num % i != 0) {
      return false;
    }
```

```transformation
    if (num / i == 0) {
      return false;
    }
```

```transformation
    if (num * i == 0) {
      return false;
    }
```

```transformation
    if (num - i == 0) {
      return false;
    }
```

```transformation
    if (num + i == 0) {
      return false;
    }
```

```transformation
    if (num / i != 0) {
      return false;
    }
```

```transformation
    if (num * i != 0) {
      return false;
    }
```

```transformation
    if (num - i != 0) {
      return false;
    }
```

```transformation
    if (num + i != 0) {
      return false;
    }
```

```transformation
    if (num % i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num % i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num % i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num / i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num * i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num + i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num - i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num / i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num * i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num + i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num - i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num / i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num * i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num + i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num - i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num / i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num * i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num + i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num - i != 0 && i != num) {
      return false;
    }
```

```transformation

```

```final
  #(ignore-test)
  return true;
```

```js
function isPrime(num) {
  while (i < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= num - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i + 1 <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) - 1 <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= Math.floor(num / 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < Math.floor(num / 2) + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < Math.floor(num / 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= num / 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < num / 2 + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < num / 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= Math.sqrt(num)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= num ** 0.5) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i <= Math.pow(num, 0.5)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num - 1 >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i * i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i * i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i * i - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i ** 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i ** 2) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i ** 2 - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= Math.pow(i, 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > Math.pow(i, 2)) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= Math.pow(i, 2) - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.floor(num / 2) >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.floor(num / 2) + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.floor(num / 2) > i - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num / 2 >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num / 2 + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num / 2 > i - 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.sqrt(num) >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num ** 0.5 >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(num, 0.5) >= i) {
    //
  }
}
```

===

```initial
  if (num <= 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 2;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 >= num) {
    return false;
  }

  let i = 2;
```

```initial
  if (2 > num) {
    return false;
  }

  let i = 2;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let i = 2;
```

```transformation
    if (num % i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num % i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num % i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num % i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num / i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num * i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num + i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num - i == 0 && i == num) {
      return false;
    }
```

```transformation
    if (num / i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num * i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num + i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num - i == 0 && i != num) {
      return false;
    }
```

```transformation
    if (num / i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num * i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num + i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num - i != 0 && i == num) {
      return false;
    }
```

```transformation
    if (num / i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num * i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num + i != 0 && i != num) {
      return false;
    }
```

```transformation
    if (num - i != 0 && i != num) {
      return false;
    }
```

```transformation

```

```final
  #(ignore-test)
  return true;
```

```js
function isPrime(num) {
  while (i <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i - 1) {
    //
  }
}
```

===

```initial
  if (num == 1 || num == 0) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num == 0 || num == 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num == 1 || num == 0) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num == 0 || num == 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num <= 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num < 2) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (1 >= num) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (2 > num) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let count = 0;
  let i = 1;
```

```initial
  if (num <= 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (1 >= num) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (2 > num) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  if (1 > num - 1) {
    return false;
  }

  let i = 1;
  let count = 0;
```

```initial
  let count = 0;
  let i = 1;
```

```initial
  let i = 1;
  let count = 0;
```

```transformation
    if (num % i == 0) {
      count++;
    }
```

```transformation
    if (num % i != 0) {
      count++;
    }
```

```transformation
    if (num / i == 0) {
      count++;
    }
```

```transformation
    if (num * i == 0) {
      count++;
    }
```

```transformation
    if (num + i == 0) {
      count++;
    }
```

```transformation
    if (num - i == 0) {
      count++;
    }
```

```transformation
    if (num / i != 0) {
      count++;
    }
```

```transformation
    if (num * i != 0) {
      count++;
    }
```

```transformation
    if (num + i != 0) {
      count++;
    }
```

```transformation
    if (num - i != 0) {
      count++;
    }
```

```transformation

```

```final
  #(ignore-test)
  if (count > 2 || count < 2) {
    return false;
  } else {
    return true;
  }
```

```final
  #(ignore-test)
  if (count >= 3 || count <= 1) {
    return false;
  } else {
    return true;
  }
```

```final
  #(ignore-test)
  if (count == 2) {
    return true;
  } else {
    return false;
  }
```

```final
  #(ignore-test)
  return count == 2;
```

```final
  #(ignore-test)
  return !(count != 2);
```

```js
function isPrime(num) {
  while (i <= num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i < num + 1) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i - 1 < num) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i - 1) {
    //
  }
}
```

===

```initial
  if (num <= 1) {
    return false;
  }

  let i = 2;
```

```initial
  if (num < 2) {
    return false;
  }

  let i = 2;
```

```initial
  if (num - 1 < 1) {
    return false;
  }

  let i = 2;
```

```transformation
    #(ignore-test)
```

```final
  return i * i > num;
```

```final
  return Math.pow(i, 2) > num;
```

```js
function isPrime(num) {
  while (i * i <= num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i < num + 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i * i - 1 < num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 <= num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 < num + 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (i ** 2 - 1 < num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) <= num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) < num + 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (Math.pow(i, 2) - 1 < num && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i * i && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i * i && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i * i - 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= i ** 2 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > i ** 2 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > i ** 2 - 1 && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num >= Math.pow(i, 2) && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num + 1 > Math.pow(i, 2) && num % i != 0) {
    //
  }
}
```

```js
function isPrime(num) {
  while (num > Math.pow(i, 2) - 1 && num % i != 0) {
    //
  }
}
```
