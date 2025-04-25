---
Write a JavaScript function that given a string, returns a string with each letter capitalized using a "while" loop.
---

```initial
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  let result = "";
```

```transformation
    i++;
```

```transformation
    result += str[i];
    i++;
```

```transformation
    result += str[i - 1];
    i++;
```

```transformation
    result += str[i + 1];
    i++;
```

```transformation
    result *= str[i].toUpperCase();
    i++;
```

```transformation
    result /= str[i].toUpperCase();
    i++;
```

```transformation
    result *= str[i].toUpperCase();
    i++;
```

```final
  return result;
```

```js
function capitalizeLetters(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length >= i + 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let i = 0;
```

```initial
  let i = 0;
  let result = [];
```

```initial
  const result = [];
  let i = 0;
```

```initial
  let i = 0;
  const result = [];
```

```transformation
    i++;
```

```transformation
    result.push(str[i]);
    i++;
```

```final
  return result.join("");
```

```js
function capitalizeLetters(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length >= i + 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let i = str.length - 1;
```

```initial
  let i = str.length - 1;
  let result = [];
```

```initial
  const result = [];
  let i = str.length - 1;
```

```initial
  let i = str.length - 1;
  const result = [];
```

```transformation
    i--;
```

```transformation
    result.unshift(str[i]);
    i--;
```

```transformation
    result.unshift(str[i + 1]);
    i--;
```

```transformation
    result.unshift(str[i - 1]);
    i--;
```

```final
  return result.join("");
```

```js
function capitalizeLetters(str) {
  while (i >= 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i > -1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i + 1 > 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 <= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (-1 < i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 < i + 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let i = str.length;
```

```initial
  let i = str.length;
  let result = [];
```

```initial
  const result = [];
  let i = str.length;
```

```initial
  let i = str.length;
  const result = [];
```

```transformation
    i--;
```

```transformation
    i--;
    result.unshift(str[i]);
```

```transformation
    i--;
    result.unshift(str[i - 1]);
```

```transformation
    i--;
    result.unshift(str[i + 1]);
```

```final
  return result.join("");
```

```js
function capitalizeLetters(str) {
  while (i > 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i >= 1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 < i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (1 <= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 <= i - 1) {
    //
  }
}
```

======

```initial
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  let result = "";
```

```transformation
    result += str[i].toUpperCase();
```

```transformation

```

```transformation
    result += str[i];
```

```transformation
    result += str[i - 1];
```

```transformation
    result += str[i + 1];
```

```transformation
    result *= str[i].toUpperCase();
```

```transformation
    result /= str[i].toUpperCase();
```

```transformation
    result *= str[i].toUpperCase();
```

```final
  #(ignore-test)
  return result;
```

```js
function capitalizeLetters(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length >= i + 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let i = 0;
```

```initial
  let i = 0;
  let result = [];
```

```initial
  const result = [];
  let i = 0;
```

```initial
  let i = 0;
  const result = [];
```

```transformation
    result.push(str[i].toUpperCase());
```

```transformation

```

```transformation
    result.push(str[i]);
```

```final
  #(ignore-test)
  return result.join("");
```

```js
function capitalizeLetters(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (str.length >= i + 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let i = str.length - 1;
```

```initial
  let i = str.length - 1;
  let result = [];
```

```initial
  const result = [];
  let i = str.length - 1;
```

```initial
  let i = str.length - 1;
  const result = [];
```

```transformation
    result.unshift(str[i].toUpperCase());
```

```transformation

```

```transformation
    result.unshift(str[i]);
```

```transformation
    result.unshift(str[i + 1]);
```

```transformation
    result.unshift(str[i - 1]);
```

```final
  #(ignore-test)
  return result.join("");
```

```js
function capitalizeLetters(str) {
  while (i >= 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i > -1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i + 1 > 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 <= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (-1 < i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 < i + 1) {
    //
  }
}
```

===

```initial
  let result = [];
  let i = str.length;
```

```initial
  let i = str.length;
  let result = [];
```

```initial
  const result = [];
  let i = str.length;
```

```initial
  let i = str.length;
  const result = [];
```

```transformation
    result.unshift(str[i].toUpperCase());
```

```transformation

```

```transformation
    result.unshift(str[i]);
```

```transformation
    result.unshift(str[i - 1]);
```

```transformation
    result.unshift(str[i + 1]);
```

```final
  #(ignore-test)
  return result.join("");
```

```js
function capitalizeLetters(str) {
  while (i > 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i >= 1) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 < i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (1 <= i) {
    //
  }
}
```

```js
function capitalizeLetters(str) {
  while (0 <= i - 1) {
    //
  }
}
```
