---
Write a JavaScript function that given a string returns it without vowels using a "while" loop.
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
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
```

```transformation
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
```

```final

```

```final
  return i;
```

```final
  return str;
```

```js
function removeVowels(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length >= i + 1) {
    //
  }
}
```

===

```initial
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
```

```initial
  let result = "";
  let i = 0;
  let vowels = ["a", "e", "i", "o", "u"];
```

```initial
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
```

```initial
  let result = "";
  let i = 0;
  const vowels = ["a", "e", "i", "o", "u"];
```

```transformation
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
```

```final

```

```final
  return i;
```

```final
  return str;
```

```js
function removeVowels(str) {
  while (i < str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i <= str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 <= str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length > i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 >= i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length >= i + 1) {
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
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
```

```transformation
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
```

```final
  return result;
```

```final

```

```final
  return i;
```

```final
  return str;
```

```js
function removeVowels(str) {
  while (i < str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 < str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 <= str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 > i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length > i + 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 >= i + 1) {
    //
  }
}
```

===

```initial
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
```

```initial
  let result = "";
  let i = 0;
  let vowels = ["a", "e", "i", "o", "u"];
```

```initial
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
```

```initial
  let result = "";
  let i = 0;
  const vowels = ["a", "e", "i", "o", "u"];
```

```transformation
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
```

```final
  return result;
```

```final

```

```final
  return i;
```

```final
  return str;
```

```js
function removeVowels(str) {
  while (i < str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 < str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 <= str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 > i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length > i + 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 >= i + 1) {
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
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
```

```transformation
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return i;
```

```final
  #(ignore-test)
  return str;
```

```js
function removeVowels(str) {
  while (i > str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i >= str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 >= str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length < i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 <= i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length <= i + 1) {
    //
  }
}
```

===

```initial
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
```

```initial
  let result = "";
  let i = 0;
  let vowels = ["a", "e", "i", "o", "u"];
```

```initial
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
```

```initial
  let i = 0;
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
```

```initial
  let result = "";
  let i = 0;
  const vowels = ["a", "e", "i", "o", "u"];
```

```transformation
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
```

```final
  #(ignore-test)
  return result;
```

```final
  #(ignore-test)
```

```final
  #(ignore-test)
  return i;
```

```final
  #(ignore-test)
  return str;
```

```js
function removeVowels(str) {
  while (i > str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i >= str.length - 1) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (i + 1 >= str.length) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length < i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length - 1 <= i) {
    //
  }
}
```

```js
function removeVowels(str) {
  while (str.length <= i + 1) {
    //
  }
}
```
