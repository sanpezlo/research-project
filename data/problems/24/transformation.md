---
Write a JavaScript function that returns the conversion from binary to decimal using a "while" loop.
---

```initial
  let decimal = 0;
  let power = 0;
```

```initial
  let power = 0;
  let decimal = 0;
```

```transformation
    binary = Math.floor(binary / 10);
```

```transformation
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
```

```transformation
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
```

```transformation
    binary = Math.floor(binary / 10);
    power++;
```

```transformation
    power++;
    binary = Math.floor(binary / 10);
```

```final
  return decimal;
```

```js
function binaryToDecimal(binary) {
  while (binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary != 0) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary > 0) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary >= 1) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary - 1 >= 0) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (0 != binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (0 < binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (1 <= binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (0 <= binary - 1) {
    //
  }
}
```

======

```initial
  let decimal = 0;
  let power = 0;
```

```initial
  let power = 0;
  let decimal = 0;
```

```transformation
    decimal += (binary % 10) * Math.pow(2, power);
    power++;
```

```transformation
    decimal += (binary % 10) * 2 ** power;
    power++;
```

```transformation

```

```transformation
    decimal += (binary % 10) * Math.pow(2, power);
```

```transformation
    decimal += (binary % 10) * 2 ** power;
```

```transformation
    power++;
```

```final
  #(ignore-test)
  return decimal;
```

```js
function binaryToDecimal(binary) {
  while (binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary != 0) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary > 0) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary >= 1) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (binary - 1 >= 0) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (0 != binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (0 < binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (1 <= binary) {
    //
  }
}
```

```js
function binaryToDecimal(binary) {
  while (0 <= binary - 1) {
    //
  }
}
```
