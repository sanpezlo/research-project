---
Write a JavaScript function that counts the number of infants (<5), children (≤17) and adults in an array, respectively, given an array of ages using a while loop.
---

TODO: cambiar orden de declaracion de variables

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] < 5) {
      babies++;
    } else if (ages[i] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] < 5) {
      babies++;
    } else if (ages[i] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] < 5) {
      babies++;
    } else if (ages[i - 1] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] <= 4) {
      babies++;
    } else if (ages[i] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] <= 4) {
      babies++;
    } else if (ages[i] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] <= 4) {
      babies++;
    } else if (ages[i - 1] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] > 17) {
      adults++;
    } else if (ages[i] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] > 17) {
      adults++;
    } else if (ages[i] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] > 17) {
      adults++;
    } else if (ages[i - 1] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] >= 18) {
      adults++;
    } else if (ages[i] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] >= 18) {
      adults++;
    } else if (ages[i] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0,
    children = 0,
    adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] >= 18) {
      adults++;
    } else if (ages[i - 1] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] < 5) {
      babies++;
    } else if (ages[i] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] < 5) {
      babies++;
    } else if (ages[i] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] < 5) {
      babies++;
    } else if (ages[i - 1] <= 17) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] <= 4) {
      babies++;
    } else if (ages[i] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] <= 4) {
      babies++;
    } else if (ages[i] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] <= 4) {
      babies++;
    } else if (ages[i - 1] < 18) {
      children++;
    } else {
      adults++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] > 17) {
      adults++;
    } else if (ages[i] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] > 17) {
      adults++;
    } else if (ages[i] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] > 17) {
      adults++;
    } else if (ages[i - 1] >= 5) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i < ages.length) {
    if (ages[i] >= 18) {
      adults++;
    } else if (ages[i] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 0;
  while (i <= ages.length - 1) {
    if (ages[i] >= 18) {
      adults++;
    } else if (ages[i] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(ages) {
  let babies = 0;
  let children = 0;
  let adults = 0;
  let i = 1;
  while (i <= ages.length) {
    if (ages[i - 1] >= 18) {
      adults++;
    } else if (ages[i - 1] > 4) {
      children++;
    } else {
      babies++;
    }
    i++;
  }
  return [babies, children, adults];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] < 5) {
      c1++;
    } else if (numbers[count] <= 17) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] < 5) {
      c1++;
    } else if (numbers[count] <= 17) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] < 5) {
      c1++;
    } else if (numbers[count - 1] <= 17) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] <= 4) {
      c1++;
    } else if (numbers[count] < 18) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] <= 4) {
      c1++;
    } else if (numbers[count] < 18) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] <= 4) {
      c1++;
    } else if (numbers[count - 1] < 18) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] > 17) {
      c3++;
    } else if (numbers[count] >= 5) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] > 17) {
      c3++;
    } else if (numbers[count] >= 5) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] > 17) {
      c3++;
    } else if (numbers[count - 1] >= 5) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] >= 18) {
      c3++;
    } else if (numbers[count] > 4) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] >= 18) {
      c3++;
    } else if (numbers[count] > 4) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0,
    c2 = 0,
    c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] >= 18) {
      c3++;
    } else if (numbers[count - 1] > 4) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] < 5) {
      c1++;
    } else if (numbers[count] <= 17) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] < 5) {
      c1++;
    } else if (numbers[count] <= 17) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] < 5) {
      c1++;
    } else if (numbers[count - 1] <= 17) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] <= 4) {
      c1++;
    } else if (numbers[count] < 18) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] <= 4) {
      c1++;
    } else if (numbers[count] < 18) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] <= 4) {
      c1++;
    } else if (numbers[count - 1] < 18) {
      c2++;
    } else {
      c3++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] > 17) {
      c3++;
    } else if (numbers[count] >= 5) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] > 17) {
      c3++;
    } else if (numbers[count] >= 5) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] > 17) {
      c3++;
    } else if (numbers[count - 1] >= 5) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count < numbers.length) {
    if (numbers[count] >= 18) {
      c3++;
    } else if (numbers[count] > 4) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 0;
  while (count <= numbers.length - 1) {
    if (numbers[count] >= 18) {
      c3++;
    } else if (numbers[count] > 4) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```

```js
function countAgeGroups(numbers) {
  let c1 = 0;
  let c2 = 0;
  let c3 = 0;
  let count = 1;
  while (count <= numbers.length) {
    if (numbers[count - 1] >= 18) {
      c3++;
    } else if (numbers[count - 1] > 4) {
      c2++;
    } else {
      c1++;
    }
    count++;
  }
  return [c1, c2, c3];
}
```
