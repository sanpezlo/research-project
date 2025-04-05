---
Write a JavaScript function that returns a string in reverse order using a "while" loop.
---

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length - 1;
  while (i >= 0) {
    reversed += str[i];
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length - 1;
  while (i + 1 > 0) {
    reversed += str[i];
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length - 1;
  while (i > -1) {
    reversed += str[i];
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length - 1;
  while (i >= 0) {
    reversed = reversed.concat(str[i]);
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length - 1;
  while (i + 1 > 0) {
    reversed = reversed.concat(str[i]);
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length - 1;
  while (i > -1) {
    reversed = reversed.concat(str[i]);
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i >= 1) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i > 0) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i != 0) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i >= 1) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i > 0) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i != 0) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = str.length;
  while (i) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = 0;
  while (i < str.length) {
    reversed = str[i] + reversed;
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = 0;
  while (i <= str.length - 1) {
    reversed = str[i] + reversed;
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = 0;
  while (i < str.length) {
    reversed = str[i].concat(reversed);
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let reversed = "";
  let i = 0;
  while (i <= str.length - 1) {
    reversed = str[i].concat(reversed);
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let result = [];
  let i = 0;
  while (i < str.length) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let result = [];
  let i = 0;
  while (i <= str.length - 1) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  const result = [];
  let i = 0;
  while (i < str.length) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  const result = [];
  let i = 0;
  while (i <= str.length - 1) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  const result = [];
  let i = str.length - 1;
  while (i >= 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  const result = [];
  let i = str.length - 1;
  while (i + 1 > 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  const result = [];
  let i = str.length - 1;
  while (i > -1) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let result = [];
  let i = str.length - 1;
  while (i >= 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let result = [];
  let i = str.length - 1;
  while (i + 1 > 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let result = [];
  let i = str.length - 1;
  while (i > -1) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let reversed = "";
  while (i >= 0) {
    reversed += str[i];
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let reversed = "";
  while (i + 1 > 0) {
    reversed += str[i];
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let reversed = "";
  while (i > -1) {
    reversed += str[i];
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let reversed = "";
  while (i >= 0) {
    reversed = reversed.concat(str[i]);
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let reversed = "";
  while (i + 1 > 0) {
    reversed = reversed.concat(str[i]);
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let reversed = "";
  while (i > -1) {
    reversed = reversed.concat(str[i]);
    i--;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i >= 1) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i > 0) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i != 0) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i) {
    i--;
    reversed += str[i];
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i >= 1) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i > 0) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i != 0) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = str.length;
  let reversed = "";
  while (i) {
    i--;
    reversed = reversed.concat(str[i]);
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = 0;
  let reversed = "";
  while (i < str.length) {
    reversed = str[i] + reversed;
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = 0;
  let reversed = "";
  while (i <= str.length - 1) {
    reversed = str[i] + reversed;
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = 0;
  let reversed = "";
  while (i < str.length) {
    reversed = str[i].concat(reversed);
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = 0;
  let reversed = "";
  while (i <= str.length - 1) {
    reversed = str[i].concat(reversed);
    i++;
  }
  return reversed;
}
```

```js
function reverseString(str) {
  let i = 0;
  let result = [];
  while (i < str.length) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = 0;
  let result = [];
  while (i <= str.length - 1) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = 0;
  const result = [];
  while (i < str.length) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = 0;
  const result = [];
  while (i <= str.length - 1) {
    result.unshift(str[i]);
    i++;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  const result = [];
  while (i >= 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  const result = [];
  while (i + 1 > 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  const result = [];
  while (i > -1) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let result = [];
  while (i >= 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let result = [];
  while (i + 1 > 0) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(str) {
  let i = str.length - 1;
  let result = [];
  while (i > -1) {
    result.push(str[i]);
    i--;
  }
  return result.join("");
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length - 1;
  while (ind >= 0) {
    rev += s[ind];
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length - 1;
  while (ind + 1 > 0) {
    rev += s[ind];
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length - 1;
  while (ind > -1) {
    rev += s[ind];
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length - 1;
  while (ind >= 0) {
    rev = rev.concat(s[ind]);
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length - 1;
  while (ind + 1 > 0) {
    rev = rev.concat(s[ind]);
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length - 1;
  while (ind > -1) {
    rev = rev.concat(s[ind]);
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind >= 1) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind > 0) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind != 0) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind >= 1) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind > 0) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind != 0) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = s.length;
  while (ind) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = 0;
  while (ind < s.length) {
    rev = s[ind] + rev;
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = 0;
  while (ind <= s.length - 1) {
    rev = s[ind] + rev;
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = 0;
  while (ind < s.length) {
    rev = s[ind].concat(rev);
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let rev = "";
  let ind = 0;
  while (ind <= s.length - 1) {
    rev = s[ind].concat(rev);
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let arr = [];
  let ind = 0;
  while (ind < s.length) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let arr = [];
  let ind = 0;
  while (ind <= s.length - 1) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  const arr = [];
  let ind = 0;
  while (ind < s.length) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  const arr = [];
  let ind = 0;
  while (ind <= s.length - 1) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  const arr = [];
  let ind = s.length - 1;
  while (ind >= 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  const arr = [];
  let ind = s.length - 1;
  while (ind + 1 > 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  const arr = [];
  let ind = s.length - 1;
  while (ind > -1) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let arr = [];
  let ind = s.length - 1;
  while (ind >= 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let arr = [];
  let ind = s.length - 1;
  while (ind + 1 > 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let arr = [];
  let ind = s.length - 1;
  while (ind > -1) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let rev = "";
  while (ind >= 0) {
    rev += s[ind];
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let rev = "";
  while (ind + 1 > 0) {
    rev += s[ind];
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let rev = "";
  while (ind > -1) {
    rev += s[ind];
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let rev = "";
  while (ind >= 0) {
    rev = rev.concat(s[ind]);
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let rev = "";
  while (ind + 1 > 0) {
    rev = rev.concat(s[ind]);
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let rev = "";
  while (ind > -1) {
    rev = rev.concat(s[ind]);
    ind--;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind >= 1) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind > 0) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind != 0) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind) {
    ind--;
    rev += s[ind];
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind >= 1) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind > 0) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind != 0) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = s.length;
  let rev = "";
  while (ind) {
    ind--;
    rev = rev.concat(s[ind]);
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = 0;
  let rev = "";
  while (ind < s.length) {
    rev = s[ind] + rev;
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = 0;
  let rev = "";
  while (ind <= s.length - 1) {
    rev = s[ind] + rev;
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = 0;
  let rev = "";
  while (ind < s.length) {
    rev = s[ind].concat(rev);
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = 0;
  let rev = "";
  while (ind <= s.length - 1) {
    rev = s[ind].concat(rev);
    ind++;
  }
  return rev;
}
```

```js
function reverseString(s) {
  let ind = 0;
  let arr = [];
  while (ind < s.length) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = 0;
  let arr = [];
  while (ind <= s.length - 1) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = 0;
  const arr = [];
  while (ind < s.length) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = 0;
  const arr = [];
  while (ind <= s.length - 1) {
    arr.unshift(s[ind]);
    ind++;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  const arr = [];
  while (ind >= 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  const arr = [];
  while (ind + 1 > 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  const arr = [];
  while (ind > -1) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let arr = [];
  while (ind >= 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let arr = [];
  while (ind + 1 > 0) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```

```js
function reverseString(s) {
  let ind = s.length - 1;
  let arr = [];
  while (ind > -1) {
    arr.push(s[ind]);
    ind--;
  }
  return arr.join("");
}
```
