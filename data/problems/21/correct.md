---
Write a JavaScript function that returns the product of the digits of a number using a "while" loop.
---

```js
function productOfDigits(num) {
  let product = 1;
  while (num >= 1) {
    product *= num % 10;
    num = Math.floor(num / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  while (num > 0) {
    product *= num % 10;
    num = Math.floor(num / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  while (num != 0) {
    product *= num % 10;
    num = Math.floor(num / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  while (num) {
    product *= num % 10;
    num = Math.floor(num / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let temp = num;
  let product = 1;
  while (temp >= 1) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let temp = num;
  let product = 1;
  while (temp > 0) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let temp = num;
  let product = 1;
  while (temp != 0) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let temp = num;
  let product = 1;
  while (temp) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num;
  while (temp >= 1) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num;
  while (temp > 0) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num;
  while (temp != 0) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num;
  while (temp) {
    product *= temp % 10;
    temp = Math.floor(temp / 10);
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num.toString();
  let i = 0;
  while (i < temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num.toString();
  let i = 0;
  while (i <= temp.length - 1) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num.toString();
  let i = 0;
  while (i + 1 <= temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  let temp = num.toString();
  let i = 1;
  while (i <= temp.length) {
    product *= temp[i - 1];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 0;
  let temp = num.toString();
  let product = 1;
  while (i < temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 0;
  let temp = num.toString();
  let product = 1;
  while (i <= temp.length - 1) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 0;
  let temp = num.toString();
  let product = 1;
  while (i + 1 <= temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 1;
  let temp = num.toString();
  let product = 1;
  while (i <= temp.length) {
    product *= temp[i - 1];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  const temp = num.toString();
  let i = 0;
  while (i < temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  const temp = num.toString();
  let i = 0;
  while (i <= temp.length - 1) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  const temp = num.toString();
  let i = 0;
  while (i + 1 <= temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let product = 1;
  const temp = num.toString();
  let i = 1;
  while (i <= temp.length) {
    product *= temp[i - 1];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 0;
  const temp = num.toString();
  let product = 1;
  while (i < temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 0;
  const temp = num.toString();
  let product = 1;
  while (i <= temp.length - 1) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 0;
  const temp = num.toString();
  let product = 1;
  while (i + 1 <= temp.length) {
    product *= temp[i];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(num) {
  let i = 1;
  const temp = num.toString();
  let product = 1;
  while (i <= temp.length) {
    product *= temp[i - 1];
    i++;
  }
  return product;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  while (n >= 1) {
    result *= n % 10;
    n = Math.floor(n / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  while (n > 0) {
    result *= n % 10;
    n = Math.floor(n / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  while (n != 0) {
    result *= n % 10;
    n = Math.floor(n / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  while (n) {
    result *= n % 10;
    n = Math.floor(n / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let t = n;
  let result = 1;
  while (t >= 1) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let t = n;
  let result = 1;
  while (t > 0) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let t = n;
  let result = 1;
  while (t != 0) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let t = n;
  let result = 1;
  while (t) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n;
  while (t >= 1) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n;
  while (t > 0) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n;
  while (t != 0) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n;
  while (t) {
    result *= t % 10;
    t = Math.floor(t / 10);
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n.toString();
  let i = 0;
  while (i < t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n.toString();
  let i = 0;
  while (i <= t.length - 1) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n.toString();
  let i = 0;
  while (i + 1 <= t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  let t = n.toString();
  let i = 1;
  while (i <= t.length) {
    result *= t[i - 1];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 0;
  let t = n.toString();
  let result = 1;
  while (i < t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 0;
  let t = n.toString();
  let result = 1;
  while (i <= t.length - 1) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 0;
  let t = n.toString();
  let result = 1;
  while (i + 1 <= t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 1;
  let t = n.toString();
  let result = 1;
  while (i <= t.length) {
    result *= t[i - 1];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  const t = n.toString();
  let i = 0;
  while (i < t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  const t = n.toString();
  let i = 0;
  while (i <= t.length - 1) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  const t = n.toString();
  let i = 0;
  while (i + 1 <= t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let result = 1;
  const t = n.toString();
  let i = 1;
  while (i <= t.length) {
    result *= t[i - 1];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 0;
  const t = n.toString();
  let result = 1;
  while (i < t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 0;
  const t = n.toString();
  let result = 1;
  while (i <= t.length - 1) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 0;
  const t = n.toString();
  let result = 1;
  while (i + 1 <= t.length) {
    result *= t[i];
    i++;
  }
  return result;
}
```

```js
function productOfDigits(n) {
  let i = 1;
  const t = n.toString();
  let result = 1;
  while (i <= t.length) {
    result *= t[i - 1];
    i++;
  }
  return result;
}
```
