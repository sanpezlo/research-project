---
Write a JavaScript function that returns the square, cube and square root of all numbers from 1 to N using a "while" loop.
---

```js
function calculatePowers(n) {
  let result = [];
  let i = 1;
  while (i <= n) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 1;
  while (i < n + 1) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 0;
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) ** 2,
      cube: (i + 1) ** 3,
      squareRoot: Math.sqrt(i + 1),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 1;
  while (i <= n) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 1;
  while (i < n + 1) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 0;
  while (i < n) {
    result.push({
      number: i + 1,
      square: Math.pow(i + 1, 2),
      cube: Math.pow(i + 1, 3),
      squareRoot: Math.pow(i + 1, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 1;
  while (i <= n) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 1;
  while (i < n + 1) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let result = [];
  let i = 0;
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) * (i + 1),
      cube: (i + 1) * (i + 1) * (i + 1),
      squareRoot: (i + 1) ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  let result = [];
  while (i <= n) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  let result = [];
  while (i < n + 1) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 0;
  let result = [];
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) ** 2,
      cube: (i + 1) ** 3,
      squareRoot: Math.sqrt(i + 1),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  let result = [];
  while (i <= n) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  let result = [];
  while (i < n + 1) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 0;
  let result = [];
  while (i < n) {
    result.push({
      number: i + 1,
      square: Math.pow(i + 1, 2),
      cube: Math.pow(i + 1, 3),
      squareRoot: Math.pow(i + 1, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  let result = [];
  while (i <= n) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  let result = [];
  while (i < n + 1) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 0;
  let result = [];
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) * (i + 1),
      cube: (i + 1) * (i + 1) * (i + 1),
      squareRoot: (i + 1) ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 1;
  while (i <= n) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 1;
  while (i < n + 1) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 0;
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) ** 2,
      cube: (i + 1) ** 3,
      squareRoot: Math.sqrt(i + 1),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 1;
  while (i <= n) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 1;
  while (i < n + 1) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 0;
  while (i < n) {
    result.push({
      number: i + 1,
      square: Math.pow(i + 1, 2),
      cube: Math.pow(i + 1, 3),
      squareRoot: Math.pow(i + 1, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 1;
  while (i <= n) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 1;
  while (i < n + 1) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  const result = [];
  let i = 0;
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) * (i + 1),
      cube: (i + 1) * (i + 1) * (i + 1),
      squareRoot: (i + 1) ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  const result = [];
  while (i <= n) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  const result = [];
  while (i < n + 1) {
    result.push({
      number: i,
      square: i ** 2,
      cube: i ** 3,
      squareRoot: Math.sqrt(i),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 0;
  const result = [];
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) ** 2,
      cube: (i + 1) ** 3,
      squareRoot: Math.sqrt(i + 1),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  const result = [];
  while (i <= n) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  const result = [];
  while (i < n + 1) {
    result.push({
      number: i,
      square: Math.pow(i, 2),
      cube: Math.pow(i, 3),
      squareRoot: Math.pow(i, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 0;
  const result = [];
  while (i < n) {
    result.push({
      number: i + 1,
      square: Math.pow(i + 1, 2),
      cube: Math.pow(i + 1, 3),
      squareRoot: Math.pow(i + 1, 1 / 2),
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  const result = [];
  while (i <= n) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 1;
  const result = [];
  while (i < n + 1) {
    result.push({
      number: i,
      square: i * i,
      cube: i * i * i,
      squareRoot: i ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(n) {
  let i = 0;
  const result = [];
  while (i < n) {
    result.push({
      number: i + 1,
      square: (i + 1) * (i + 1),
      cube: (i + 1) * (i + 1) * (i + 1),
      squareRoot: (i + 1) ** 0.5,
    });
    i++;
  }
  return result;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 1;
  while (index <= N) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 1;
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 0;
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) ** 2,
      cube: (index + 1) ** 3,
      squareRoot: Math.sqrt(index + 1),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 1;
  while (index <= N) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 1;
  while (index < N + 1) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 0;
  while (index < N) {
    powers.push({
      number: index + 1,
      square: Math.pow(index + 1, 2),
      cube: Math.pow(index + 1, 3),
      squareRoot: Math.pow(index + 1, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 1;
  while (index <= N) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 1;
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let powers = [];
  let index = 0;
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) * (index + 1),
      cube: (index + 1) * (index + 1) * (index + 1),
      squareRoot: (index + 1) ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  let powers = [];
  while (index <= N) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  let powers = [];
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 0;
  let powers = [];
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) ** 2,
      cube: (index + 1) ** 3,
      squareRoot: Math.sqrt(index + 1),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  let powers = [];
  while (index <= N) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  let powers = [];
  while (index < N + 1) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 0;
  let powers = [];
  while (index < N) {
    powers.push({
      number: index + 1,
      square: Math.pow(index + 1, 2),
      cube: Math.pow(index + 1, 3),
      squareRoot: Math.pow(index + 1, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  let powers = [];
  while (index <= N) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  let powers = [];
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 0;
  let powers = [];
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) * (index + 1),
      cube: (index + 1) * (index + 1) * (index + 1),
      squareRoot: (index + 1) ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 1;
  while (index <= N) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 1;
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 0;
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) ** 2,
      cube: (index + 1) ** 3,
      squareRoot: Math.sqrt(index + 1),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 1;
  while (index <= N) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 1;
  while (index < N + 1) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 0;
  while (index < N) {
    powers.push({
      number: index + 1,
      square: Math.pow(index + 1, 2),
      cube: Math.pow(index + 1, 3),
      squareRoot: Math.pow(index + 1, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 1;
  while (index <= N) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 1;
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  const powers = [];
  let index = 0;
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) * (index + 1),
      cube: (index + 1) * (index + 1) * (index + 1),
      squareRoot: (index + 1) ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  const powers = [];
  while (index <= N) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  const powers = [];
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index ** 2,
      cube: index ** 3,
      squareRoot: Math.sqrt(index),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 0;
  const powers = [];
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) ** 2,
      cube: (index + 1) ** 3,
      squareRoot: Math.sqrt(index + 1),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  const powers = [];
  while (index <= N) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  const powers = [];
  while (index < N + 1) {
    powers.push({
      number: index,
      square: Math.pow(index, 2),
      cube: Math.pow(index, 3),
      squareRoot: Math.pow(index, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 0;
  const powers = [];
  while (index < N) {
    powers.push({
      number: index + 1,
      square: Math.pow(index + 1, 2),
      cube: Math.pow(index + 1, 3),
      squareRoot: Math.pow(index + 1, 1 / 2),
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  const powers = [];
  while (index <= N) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 1;
  const powers = [];
  while (index < N + 1) {
    powers.push({
      number: index,
      square: index * index,
      cube: index * index * index,
      squareRoot: index ** 0.5,
    });
    index++;
  }
  return powers;
}
```

```js
function calculatePowers(N) {
  let index = 0;
  const powers = [];
  while (index < N) {
    powers.push({
      number: index + 1,
      square: (index + 1) * (index + 1),
      cube: (index + 1) * (index + 1) * (index + 1),
      squareRoot: (index + 1) ** 0.5,
    });
    index++;
  }
  return powers;
}
```
