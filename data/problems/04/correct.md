---
Write a JavaScript function that returns whether a number is prime using a "while" loop.
---

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i < num) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i <= num) {
    if (num % i == 0 && i !== num) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i <= num - 1) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num == 1 || num == 0) {
    return false;
  }

  let count = 0;
  let i = 1;
  while (i <= num) {
    if (num % i == 0) {
      count++;
    }
    i++;
  }

  if (count > 2) {
    return false;
  } else {
    return true;
  }
}
```

```js
function isPrime(num) {
  let count = 0;
  let i = 1;
  while (i <= num) {
    if (num % i == 0) {
      count++;
    }
    i++;
  }
  return count == 2;
}
```

```js
function isPrime(num) {
  let i = 1;
  let count = 0;
  while (i <= num) {
    if (num % i == 0) {
      count++;
    }
    i++;
  }
  return count == 2;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i * i <= num) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i <= Math.floor(num / 2)) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i <= num / 2) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i <= Math.sqrt(num)) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i <= num ** 0.5) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i <= Math.pow(num, 0.5)) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (i * i <= num && num % i !== 0) {
    i++;
  }
  return i * i > num;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (Math.pow(i, 2) <= num) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  let i = 2;
  while (Math.pow(i, 2) <= num && num % i !== 0) {
    i++;
  }
  return Math.pow(i, 2) > num;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i < num) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i <= num) {
    if (num % i == 0 && i !== num) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i * i <= num) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i <= Math.floor(num / 2)) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i <= num / 2) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i <= Math.sqrt(num)) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i <= num ** 0.5) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i <= Math.pow(num, 0.5)) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (i * i <= num && num % i !== 0) {
    i++;
  }
  return i * i > num;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (Math.pow(i, 2) <= num) {
    if (num % i == 0) {
      return false;
    }
    i++;
  }
  return true;
}
```

```js
function isPrime(num) {
  if (num < 2) {
    return false;
  }

  let i = 2;
  while (Math.pow(i, 2) <= num && num % i !== 0) {
    i++;
  }
  return Math.pow(i, 2) > num;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count < x) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count <= x) {
    if (x % count == 0 && count !== x) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count <= x - 1) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count * count <= x) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count <= Math.floor(x / 2)) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count <= x / 2) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count <= Math.sqrt(x)) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count <= x ** 0.5) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count <= Math.pow(x, 0.5)) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (count * count <= x && x % count !== 0) {
    count++;
  }
  return count * count > x;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (Math.pow(count, 2) <= x) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x <= 1) {
    return false;
  }

  let count = 2;
  while (Math.pow(count, 2) <= x && x % count !== 0) {
    count++;
  }
  return Math.pow(count, 2) > x;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count < x) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count <= x) {
    if (x % count == 0 && count !== x) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count * count <= x) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count <= Math.floor(x / 2)) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count <= x / 2) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count <= Math.sqrt(x)) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count <= x ** 0.5) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count <= Math.pow(x, 0.5)) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (count * count <= x && x % count !== 0) {
    count++;
  }
  return count * count > x;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (Math.pow(count, 2) <= x) {
    if (x % count == 0) {
      return false;
    }
    count++;
  }
  return true;
}
```

```js
function isPrime(x) {
  if (x < 2) {
    return false;
  }

  let count = 2;
  while (Math.pow(count, 2) <= x && x % count !== 0) {
    count++;
  }
  return Math.pow(count, 2) > x;
}
```
