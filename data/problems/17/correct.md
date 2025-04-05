---
Write a JavaScript function that returns in an array all uppercase letters of the alphabet from 'A' to 'Z' using a "while" loop.
---

```js
function uppercaseLetters() {
  let result = [];
  let charCode = 65;
  while (charCode <= 90) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let result = [];
  let charCode = 65;
  while (charCode < 91) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let result = [];
  let charCode = 65;
  while (charCode < 90 + 1) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let result = [];
  let i = "A".charCodeAt(0);
  while (i <= "Z".charCodeAt(0)) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let result = [];
  let i = "A".charCodeAt(0);
  while (i < "Z".charCodeAt(0) + 1) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let result = [];
  let letter = "A";
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let letter = "A";
  let result = [];
  let i = 0;
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
    i += 1;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let charCode = 65;
  let result = [];
  while (charCode <= 90) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let charCode = 65;
  let result = [];
  while (charCode < 91) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let charCode = 65;
  let result = [];
  while (charCode < 90 + 1) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let i = "A".charCodeAt(0);
  let result = [];
  while (i <= "Z".charCodeAt(0)) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let i = "A".charCodeAt(0);
  let result = [];
  while (i < "Z".charCodeAt(0) + 1) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let letter = "A";
  let result = [];
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let i = 0;
  let result = [];
  let letter = "A";
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
    i += 1;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  const result = [];
  let charCode = 65;
  while (charCode <= 90) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  const result = [];
  let charCode = 65;
  while (charCode < 91) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  const result = [];
  let charCode = 65;
  while (charCode < 90 + 1) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  const result = [];
  let i = "A".charCodeAt(0);
  while (i <= "Z".charCodeAt(0)) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  const result = [];
  let i = "A".charCodeAt(0);
  while (i < "Z".charCodeAt(0) + 1) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  const result = [];
  let letter = "A";
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let letter = "A";
  const result = [];
  let i = 0;
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
    i += 1;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let charCode = 65;
  const result = [];
  while (charCode <= 90) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let charCode = 65;
  const result = [];
  while (charCode < 91) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let charCode = 65;
  const result = [];
  while (charCode < 90 + 1) {
    let letter = String.fromCharCode(charCode);
    result.push(letter);
    charCode++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let i = "A".charCodeAt(0);
  const result = [];
  while (i <= "Z".charCodeAt(0)) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let i = "A".charCodeAt(0);
  const result = [];
  while (i < "Z".charCodeAt(0) + 1) {
    result.push(String.fromCharCode(i));
    i++;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let letter = "A";
  const result = [];
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let i = 0;
  const result = [];
  let letter = "A";
  while (letter <= "Z") {
    result.push(letter);
    letter = String.fromCharCode(letter.charCodeAt(0) + 1);
    i += 1;
  }
  return result;
}
```

```js
function uppercaseLetters() {
  let letters = [];
  let code = 65;
  while (code <= 90) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let letters = [];
  let code = 65;
  while (code < 91) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let letters = [];
  let code = 65;
  while (code < 90 + 1) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let letters = [];
  let index = "A".charCodeAt(0);
  while (index <= "Z".charCodeAt(0)) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let letters = [];
  let index = "A".charCodeAt(0);
  while (index < "Z".charCodeAt(0) + 1) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let letters = [];
  let c = "A";
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let c = "A";
  let letters = [];
  let index = 0;
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
    index += 1;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let code = 65;
  let letters = [];
  while (code <= 90) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let code = 65;
  let letters = [];
  while (code < 91) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let code = 65;
  let letters = [];
  while (code < 90 + 1) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let index = "A".charCodeAt(0);
  let letters = [];
  while (index <= "Z".charCodeAt(0)) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let index = "A".charCodeAt(0);
  let letters = [];
  while (index < "Z".charCodeAt(0) + 1) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let c = "A";
  let letters = [];
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let index = 0;
  let letters = [];
  let c = "A";
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
    index += 1;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  const letters = [];
  let code = 65;
  while (code <= 90) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  const letters = [];
  let code = 65;
  while (code < 91) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  const letters = [];
  let code = 65;
  while (code < 90 + 1) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  const letters = [];
  let index = "A".charCodeAt(0);
  while (index <= "Z".charCodeAt(0)) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  const letters = [];
  let index = "A".charCodeAt(0);
  while (index < "Z".charCodeAt(0) + 1) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  const letters = [];
  let c = "A";
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let c = "A";
  const letters = [];
  let index = 0;
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
    index += 1;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let code = 65;
  const letters = [];
  while (code <= 90) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let code = 65;
  const letters = [];
  while (code < 91) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let code = 65;
  const letters = [];
  while (code < 90 + 1) {
    let c = String.fromCharCode(code);
    letters.push(c);
    code++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let index = "A".charCodeAt(0);
  const letters = [];
  while (index <= "Z".charCodeAt(0)) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let index = "A".charCodeAt(0);
  const letters = [];
  while (index < "Z".charCodeAt(0) + 1) {
    letters.push(String.fromCharCode(index));
    index++;
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let c = "A";
  const letters = [];
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
  }
  return letters;
}
```

```js
function uppercaseLetters() {
  let index = 0;
  const letters = [];
  let c = "A";
  while (c <= "Z") {
    letters.push(c);
    c = String.fromCharCode(c.charCodeAt(0) + 1);
    index += 1;
  }
  return letters;
}
```
