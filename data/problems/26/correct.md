---
Write a JavaScript function that returns a string in reverse order using a "while" loop.
---

```initial
  let reversed = "";
  let i = str.length - 1;
```

```initial
  let i = str.length - 1;
  let reversed = "";
```

```transformation
    reversed += str[i];
    i--;
```

```transformation
    reversed = reversed.concat(str[i]);
    i--;
```

```final
  return reversed;
```

```js
function reverseString(str) {
  while (i >= 0) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i > -1) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i + 1 > 0) {
    //
  }
}
```

```js
function reverseString(str) {
  while (0 <= i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (-1 < i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (0 < i + 1) {
    //
  }
}
```

===

```initial
  let reversed = "";
  let i = str.length;
```

```initial
  let i = str.length;
  let reversed = "";
```

```transformation
    i--;
    reversed += str[i];
```

```transformation
    i--;
    reversed = reversed.concat(str[i]);
```

```final
  return reversed;
```

```js
function reverseString(str) {
  while (i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i != 0) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i > 0) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i >= 1) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i - 1 >= 0) {
    //
  }
}
```

```js
function reverseString(str) {
  while (0 != i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (0 < i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (1 <= i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (0 <= i - 1) {
    //
  }
}
```

===

```initial
  let reversed = "";
  let i = 0;
```

```initial
  let i = 0;
  let reversed = "";
```

```transformation
    reversed = str[i] + reversed;
    i++;
```

```transformation
    reversed = str[i].concat(reversed);
    i++;
```

```final
  return reversed;
```

```js
function reverseString(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function reverseString(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function reverseString(str) {
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
    result.unshift(str[i]);
    i++;
```

```final
  return result.join("");
```

```js
function reverseString(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function reverseString(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function reverseString(str) {
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
    result.push(str[i]);
    i--;
```

```final
  return result.join("");
```

```js
function reverseString(str) {
  while (i >= 0) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i > -1) {
    //
  }
}
```

```js
function reverseString(str) {
  while (i + 1 > 0) {
    //
  }
}
```

```js
function reverseString(str) {
  while (0 <= i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (-1 < i) {
    //
  }
}
```

```js
function reverseString(str) {
  while (0 < i + 1) {
    //
  }
}
```
