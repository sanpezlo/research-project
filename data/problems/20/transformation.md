---
Write a JavaScript function that returns the product of the digits of a number using a "while" loop.
---

```initial
  let product = 1;
```

```transformation
    num = Math.floor(num / 10);
```

```transformation
    product *= num / 10;
    num = Math.floor(num / 10);
```

```final
  return product;
```

```js
function productOfDigits(num) {
  while (num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num != 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num > 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num >= 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num - 1 >= 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 != num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 < num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (1 <= num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 <= num - 1) {
    //
  }
}
```

===

```initial
  let temp = num;
  let product = 1;
```

```initial
  let product = 1;
  let temp = num;
```

```transformation
    temp = Math.floor(temp / 10);
```

```transformation
    product *= temp / 10;
    temp = Math.floor(temp / 10);
```

```final
  return product;
```

```js
function productOfDigits(num) {
  while (temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp != 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp > 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp >= 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp - 1 >= 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 != temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 < temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (1 <= temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 <= temp - 1) {
    //
  }
}
```

===

```initial
  let product = 1;
  let temp = num.toString();
  let i = 0;
```

```initial
  let i = 0;
  let product = 1;
  let temp = num.toString();
```

```initial
  let temp = num.toString();
  let i = 0;
  let product = 1;
```

```transformation
    i++;
```

```transformation
    product += temp[i];
    i++;
```

```transformation
    product -= temp[i];
    i++;
```

```transformation
    product /= temp[i];
    i++;
```

```final
  return product;
```

```js
function productOfDigits(num) {
  while (i < temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i <= temp.length - 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i + 1 <= temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length > i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length - 1 >= i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length >= i + 1) {
    //
  }
}
```

===

```initial
  let product = 1;
  let temp = num.toString();
  let i = 1;
```

```initial
  let i = 1;
  let product = 1;
  let temp = num.toString();
```

```initial
  let temp = num.toString();
  let i = 1;
  let product = 1;
```

```transformation
    i++;
```

```transformation
    product *= temp[i];
    i++;
```

```transformation
    product /= temp[i - 1];
    i++;
```

```transformation
    product += temp[i - 1];
    i++;
```

```transformation
    product -= temp[i - 1];
    i++;
```

```final
  return product;
```

```js
function productOfDigits(num) {
  while (i <= temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i < temp.length + 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i - 1 < temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length >= i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length + 1 > i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length > i - 1) {
    //
  }
}
```

======

```initial
  let product = 1;
```

```transformation
    product *= num % 10;
```

```transformation

```

```transformation
    product *= num / 10;
```

```final
  #(ignore-test)
  return product;
```

```js
function productOfDigits(num) {
  while (num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num != 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num > 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num >= 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (num - 1 >= 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 != num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 < num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (1 <= num) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 <= num - 1) {
    //
  }
}
```

===

```initial
  let temp = num;
  let product = 1;
```

```initial
  let product = 1;
  let temp = num;
```

```transformation
    product *= temp % 10;
```

```transformation

```

```transformation
    product *= temp / 10;
```

```final
  #(ignore-test)
  return product;
```

```js
function productOfDigits(num) {
  while (temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp != 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp > 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp >= 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp - 1 >= 0) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 != temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 < temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (1 <= temp) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (0 <= temp - 1) {
    //
  }
}
```

===

```initial
  let product = 1;
  let temp = num.toString();
  let i = 0;
```

```initial
  let i = 0;
  let product = 1;
  let temp = num.toString();
```

```initial
  let temp = num.toString();
  let i = 0;
  let product = 1;
```

```transformation
    product *= temp[i];
```

```transformation

```

```transformation
    product += temp[i];
```

```transformation
    product -= temp[i];
```

```transformation
    product /= temp[i];
```

```final
  #(ignore-test)
  return product;
```

```js
function productOfDigits(num) {
  while (i < temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i <= temp.length - 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i + 1 <= temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length > i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length - 1 >= i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length >= i + 1) {
    //
  }
}
```

===

```initial
  let product = 1;
  let temp = num.toString();
  let i = 1;
```

```initial
  let i = 1;
  let product = 1;
  let temp = num.toString();
```

```initial
  let temp = num.toString();
  let i = 1;
  let product = 1;
```

```transformation
    product *= temp[i - 1];
```

```transformation

```

```transformation
    product *= temp[i];
```

```transformation
    product /= temp[i - 1];
```

```transformation
    product += temp[i - 1];
```

```transformation
    product -= temp[i - 1];
```

```final
  #(ignore-test)
  return product;
```

```js
function productOfDigits(num) {
  while (i <= temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i < temp.length + 1) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (i - 1 < temp.length) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length >= i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length + 1 > i) {
    //
  }
}
```

```js
function productOfDigits(num) {
  while (temp.length > i - 1) {
    //
  }
}
```
