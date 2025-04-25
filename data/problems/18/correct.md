---
Write a JavaScript function that counts the number of infants (<5), children (≤17) and adults in an array, respectively, given an array of ages using a while loop.
---

```initial
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
```

```initial
  let i = 0;
  let babies = 0;
  let children = 0;
  let adults = 0;
```

```initial
  let adults = 0;
  let i = 0;
  let babies = 0;
  let children = 0;
```

```initial
  let children = 0;
  let adults = 0;
  let i = 0;
  let babies = 0;
```

```transformation
    if (ages[i] < 5) {
      babies++;
    } else if (ages[i] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
```

```transformation
    if (ages[i] >= 18) {
      adults++;
    } else if (ages[i] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
```

```transformation
    if (ages[i] <= 4) {
      babies++;
    } else if (ages[i] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
```

```transformation
    if (ages[i] > 17) {
      adults++;
    } else if (ages[i] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
```

```final
  return [babies, children, adults];
```

```js
function countAgeGroups(ages) {
  while (i < ages.length) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (i <= ages.length - 1) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (i + 1 <= ages.length) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (ages.length > i) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (ages.length - 1 >= i) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (ages.length >= i + 1) {
    //
  }
}
```

===

```initial
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 1;
```

```initial
  let i = 1;
  let babies = 0;
  let children = 0;
  let adults = 0;
```

```initial
  let adults = 0;
  let i = 1;
  let babies = 0;
  let children = 0;
```

```initial
  let children = 0;
  let adults = 0;
  let i = 1;
  let babies = 0;
```

```transformation
    if (ages[i - 1] < 5) {
      babies++;
    } else if (ages[i - 1] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
```

```transformation
    if (ages[i - 1] >= 18) {
      adults++;
    } else if (ages[i - 1] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
```

```transformation
    if (ages[i - 1] <= 4) {
      babies++;
    } else if (ages[i - 1] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
```

```transformation
    if (ages[i - 1] > 17) {
      adults++;
    } else if (ages[i - 1] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
```

```final
  return [babies, children, adults];
```

```js
function countAgeGroups(ages) {
  while (i <= ages.length) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (i < ages.length + 1) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (i - 1 < ages.length) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (ages.length >= i) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (ages.length + 1 > i) {
    //
  }
}
```

```js
function countAgeGroups(ages) {
  while (ages.length > i - 1) {
    //
  }
}
```
