---
Write a JavaScript function that given a string returns it without vowels using a "while" loop.
---

TODO: Cambiar operador logico del while ("<" - "<=") o (">" - ">=")

```js
function removeVowels(str) {
  let result = "",
    i = 0;
  while (i < str.length) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "",
    i = 0;
  while (i <= str.length - 1) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "",
    i = 0;
  while (i + 1 <= str.length) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "";
  let i = 0;
  while (i < str.length) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "";
  let i = 0;
  while (i <= str.length - 1) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "";
  let i = 0;
  while (i + 1 <= str.length) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  while (i < str.length) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  while (i <= str.length - 1) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  while (i + 1 <= str.length) {
    if (!"aeiouAEIOU".includes(str[i])) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "",
    i = 0;
  while (i < str.length) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "",
    i = 0;
  while (i <= str.length - 1) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "",
    i = 0;
  while (i + 1 <= str.length) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "";
  let i = 0;
  while (i < str.length) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "";
  let i = 0;
  while (i <= str.length - 1) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let result = "";
  let i = 0;
  while (i + 1 <= str.length) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  while (i < str.length) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  while (i <= str.length - 1) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  while (i + 1 <= str.length) {
    if (!"aeiou".includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
  while (i < str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
  while (i <= str.length - 1) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
  while (i + 1 <= str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  let vowels = ["a", "e", "i", "o", "u"];
  while (i < str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  let vowels = ["a", "e", "i", "o", "u"];
  while (i <= str.length - 1) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  let vowels = ["a", "e", "i", "o", "u"];
  while (i + 1 <= str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
  while (i < str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
  while (i <= str.length - 1) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  const vowels = ["a", "e", "i", "o", "u"];
  let result = "";
  let i = 0;
  while (i + 1 <= str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  const vowels = ["a", "e", "i", "o", "u"];
  while (i < str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  const vowels = ["a", "e", "i", "o", "u"];
  while (i <= str.length - 1) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(str) {
  let i = 0;
  let result = "";
  const vowels = ["a", "e", "i", "o", "u"];
  while (i + 1 <= str.length) {
    if (!vowels.includes(str[i].toLowerCase())) {
      result += str[i];
    }
    i++;
  }
  return result;
}
```

```js
function removeVowels(s) {
  let r = "",
    idx = 0;
  while (idx < s.length) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "",
    idx = 0;
  while (idx <= s.length - 1) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "",
    idx = 0;
  while (idx + 1 <= s.length) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "";
  let idx = 0;
  while (idx < s.length) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "";
  let idx = 0;
  while (idx <= s.length - 1) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "";
  let idx = 0;
  while (idx + 1 <= s.length) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  while (idx < s.length) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  while (idx <= s.length - 1) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  while (idx + 1 <= s.length) {
    if (!"aeiouAEIOU".includes(s[idx])) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "",
    idx = 0;
  while (idx < s.length) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "",
    idx = 0;
  while (idx <= s.length - 1) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "",
    idx = 0;
  while (idx + 1 <= s.length) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "";
  let idx = 0;
  while (idx < s.length) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "";
  let idx = 0;
  while (idx <= s.length - 1) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let r = "";
  let idx = 0;
  while (idx + 1 <= s.length) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  while (idx < s.length) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  while (idx <= s.length - 1) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  while (idx + 1 <= s.length) {
    if (!"aeiou".includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let v = ["a", "e", "i", "o", "u"];
  let r = "";
  let idx = 0;
  while (idx < s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let v = ["a", "e", "i", "o", "u"];
  let r = "";
  let idx = 0;
  while (idx <= s.length - 1) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let v = ["a", "e", "i", "o", "u"];
  let r = "";
  let idx = 0;
  while (idx + 1 <= s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  let v = ["a", "e", "i", "o", "u"];
  while (idx < s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  let v = ["a", "e", "i", "o", "u"];
  while (idx <= s.length - 1) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  let v = ["a", "e", "i", "o", "u"];
  while (idx + 1 <= s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  const v = ["a", "e", "i", "o", "u"];
  let r = "";
  let idx = 0;
  while (idx < s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  const v = ["a", "e", "i", "o", "u"];
  let r = "";
  let idx = 0;
  while (idx <= s.length - 1) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  const v = ["a", "e", "i", "o", "u"];
  let r = "";
  let idx = 0;
  while (idx + 1 <= s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  const v = ["a", "e", "i", "o", "u"];
  while (idx < s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  const v = ["a", "e", "i", "o", "u"];
  while (idx <= s.length - 1) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```

```js
function removeVowels(s) {
  let idx = 0;
  let r = "";
  const v = ["a", "e", "i", "o", "u"];
  while (idx + 1 <= s.length) {
    if (!v.includes(s[idx].toLowerCase())) {
      r += s[idx];
    }
    idx++;
  }
  return r;
}
```
