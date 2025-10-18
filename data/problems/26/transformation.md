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
    i--;
```

```transformation
    reversed -= str[i];
    i--;
```

```transformation
    reversed *= str[i];
    i--;
```

```transformation
    reversed /= str[i];
    i--;
```

```transformation
    reversed = reversed.concat(str[i + 1]);
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
```

```transformation
    i--;
    reversed -= str[i];
```

```transformation
    i--;
    reversed *= str[i];
```

```transformation
    i--;
    reversed /= str[i];
```

```transformation
    i--;
    reversed = reversed.concat(str[i - 1]);
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
    i++;
```

```transformation
    reversed = str[i] - reversed;
    i++;
```

```transformation
    reversed = str[i] * reversed;
    i++;
```

```transformation
    reversed = str[i] / reversed;
    i++;
```

```transformation
    reversed = str[i].concat(i);
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
    i++;
```

```transformation
    result.unshift(str[i + 1]);
    i++;
```

```transformation
    result.unshift(str[i - 1]);
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
    i--;
```

```transformation
    result.push(str[i - 1]);
    i--;
```

```transformation
    result.push(str[i + 1]);
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

======

```initial
  let reversed = "";
  let i = str.length - 1;
```

```initial
  let i = str.length - 1;
  let reversed = "";
```

```transformation
    #(ignore-test)
    reversed += str[i];
```

```transformation
    #(ignore-test)
    reversed = reversed.concat(str[i]);
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    reversed -= str[i];
```

```transformation
    #(ignore-test)
    reversed *= str[i];
```

```transformation
    #(ignore-test)
    reversed /= str[i];
```

```transformation
    #(ignore-test)
    reversed = reversed.concat(str[i + 1]);
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
    #(ignore-test)
    reversed += str[i];
```

```transformation
    #(ignore-test)
    reversed = reversed.concat(str[i]);
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    reversed -= str[i];
```

```transformation
    #(ignore-test)
    reversed *= str[i];
```

```transformation
    #(ignore-test)
    reversed /= str[i];
```

```transformation
    #(ignore-test)
    reversed = reversed.concat(str[i - 1]);
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
    #(ignore-test)
    reversed = str[i] + reversed;
```

```transformation
    #(ignore-test)
    reversed = str[i].concat(reversed);
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    reversed = str[i] - reversed;
```

```transformation
    #(ignore-test)
    reversed = str[i] * reversed;
```

```transformation
    #(ignore-test)
    reversed = str[i] / reversed;
```

```transformation
    #(ignore-test)
    reversed = str[i].concat(i);
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
    #(ignore-test)
    result.unshift(str[i]);
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result.unshift(str[i + 1]);
```

```transformation
    #(ignore-test)
    result.unshift(str[i - 1]);
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
    #(ignore-test)
    result.push(str[i]);
```

```transformation
    #(ignore-test)

```

```transformation
    #(ignore-test)
    result.push(str[i - 1]);
```

```transformation
    #(ignore-test)
    result.push(str[i + 1]);
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
