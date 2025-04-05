---
Write a JavaScript function that returns the conversion from binary to decimal using a "while" loop.
---

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary > 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary >= 1) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary - 1 >= 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary != 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary > 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary >= 1) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary - 1 >= 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary != 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0,
    power = 0;
  while (binary) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary > 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary >= 1) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary - 1 >= 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary != 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary > 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary >= 1) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary - 1 >= 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary != 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let decimal = 0;
  let power = 0;
  while (binary) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary > 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary >= 1) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary - 1 >= 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary != 0) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary) {
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary > 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary >= 1) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary - 1 >= 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary != 0) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(binary) {
  let power = 0;
  let decimal = 0;
  while (binary) {
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
  }
  return decimal;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n > 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n >= 1) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n - 1 >= 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n != 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n > 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n >= 1) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n - 1 >= 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n != 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0,
    i = 0;
  while (n) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n > 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n >= 1) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n - 1 >= 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n != 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n > 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n >= 1) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n - 1 >= 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n != 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let result = 0;
  let i = 0;
  while (n) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n > 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n >= 1) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n - 1 >= 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n != 0) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n) {
    result += (n % 10) * Math.pow(2, i);
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n > 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n >= 1) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n - 1 >= 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n != 0) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```

```js
function binaryToDecimal(n) {
  let i = 0;
  let result = 0;
  while (n) {
    result += (n % 10) * 2 ** i;
    n = Math.floor(n / 10);
    i++;
  }
  return result;
}
```
