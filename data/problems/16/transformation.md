---
Write a JavaScript function that returns in an array all uppercase letters of the alphabet from 'A' to 'Z' using a "while" loop.
---

```initial
  let result = [];
  let charCode = 65;
```

```initial
  let charCode = 65;
  let result = [];
```

```initial
  const result = [];
  let charCode = 65;
```

```initial
  let charCode = 65;
  const result = [];
```

```initial
  let result = [];
  let charCode = "A".charCodeAt(0);
```

```initial
  let charCode = "A".charCodeAt(0);
  let result = [];
```

```initial
  const result = [];
  let charCode = "A".charCodeAt(0);
```

```initial
  let charCode = "A".charCodeAt(0);
  const result = [];
```

```transformation
    charCode++;
```

```transformation
    let letter = String.fromCharCode(charCode + 1);
    result.push(letter);
    charCode++;
```

```transformation
    const letter = String.fromCharCode(charCode + 1);
    result.push(letter);
    charCode++;
```

```transformation
    result.push(String.fromCharCode(charCode + 1));
    charCode++;
```

```final
  return result;
```

```js
function uppercaseLetters() {
  while (charCode <= 90) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode < 91) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode - 1 < 90) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (90 >= charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (91 > charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (90 > charCode - 1) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode <= "Z".charCodeAt(0)) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode < "Z".charCodeAt(0) + 1) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode - 1 < "Z".charCodeAt(0)) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z".charCodeAt(0) >= charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z".charCodeAt(0) + 1 > charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z".charCodeAt(0) > charCode - 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let letter = "A";
```

```initial
  let letter = "A";
  let result = [];
```

```initial
  const result = [];
  let letter = "A";
```

```initial
  let letter = "A";
  const result = [];
```

```transformation
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
```

```transformation
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 2);
```

```final
  return result;
```

```js
function uppercaseLetters() {
  while (letter <= "Z") {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z" >= letter) {
    //
  }
}
```

======

```initial
  let result = [];
  let charCode = 65;
```

```initial
  let charCode = 65;
  let result = [];
```

```initial
  const result = [];
  let charCode = 65;
```

```initial
  let charCode = 65;
  const result = [];
```

```initial
  let result = [];
  let charCode = "A".charCodeAt(0);
```

```initial
  let charCode = "A".charCodeAt(0);
  let result = [];
```

```initial
  const result = [];
  let charCode = "A".charCodeAt(0);
```

```initial
  let charCode = "A".charCodeAt(0);
  const result = [];
```

```transformation
    let letter = String.fromCharCode(charCode);
    result.push(letter);
```

```transformation
    const letter = String.fromCharCode(charCode);
    result.push(letter);
```

```transformation
    result.push(String.fromCharCode(charCode));
```

```transformation

```

```transformation
    let letter = String.fromCharCode(charCode + 1);
    result.push(letter);
```

```transformation
    const letter = String.fromCharCode(charCode + 1);
    result.push(letter);
```

```transformation
    result.push(String.fromCharCode(charCode + 1));
```

```final
  #(ignore-test)
  return result;
```

```js
function uppercaseLetters() {
  while (charCode <= 90) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode < 91) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode - 1 < 90) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (90 >= charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (91 > charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (90 > charCode - 1) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode <= "Z".charCodeAt(0)) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode < "Z".charCodeAt(0) + 1) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while (charCode - 1 < "Z".charCodeAt(0)) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z".charCodeAt(0) >= charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z".charCodeAt(0) + 1 > charCode) {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z".charCodeAt(0) > charCode - 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let letter = "A";
```

```initial
  let letter = "A";
  let result = [];
```

```initial
  const result = [];
  let letter = "A";
```

```initial
  let letter = "A";
  const result = [];
```

```transformation
    result.push(letter);
```

```transformation

```

```transformation
    result.push(letter);
```

```final
  #(ignore-test)
  return result;
```

```js
function uppercaseLetters() {
  while (letter <= "Z") {
    //
  }
}
```

```js
function uppercaseLetters() {
  while ("Z" >= letter) {
    //
  }
}
```
