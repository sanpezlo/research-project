---
Write a JavaScript function that returns the conversion from binary to decimal using a "while" loop.
---

```initial
  let decimal = 1;
  let power = 0;
```

```initial
  let power = 0;
  let decimal = 1;
```

```initial
  let decimal = 0;
  let power = 1;
```

```initial
  let power = 1;
  let decimal = 0;
```

```initial
  let decimal = 1;
  let power = 1;
```

```initial
  let power = 1;
  let decimal = 1;
```

```transformation
    decimal += (binary % 10) * Math.pow(2, power);
    binary = Math.floor(binary / 10);
    power++;
```

```transformation
    decimal += (binary % 10) * 2 ** power;
    binary = Math.floor(binary / 10);
    power++;
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
