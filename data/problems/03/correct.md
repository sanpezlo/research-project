---
Write a JavaScript function that returns in an array the numbers from 1 to N using a "while" loop.
---

```js
function count(n) {
  let numbers = [];
  let i = 1;
  while (i <= n) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let numbers = [];
  let i = 1;
  while (i < n + 1) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  const numbers = [];
  let i = 1;
  while (i <= n) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  const numbers = [];
  let i = 1;
  while (i < n + 1) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let numbers = [];
  let i = 1;
  while (i <= n) {
    numbers = numbers.concat([i]);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let numbers = [];
  let i = 1;
  while (i < n + 1) {
    numbers = numbers.concat([i]);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let numbers = [];
  let i = 1;
  while (true) {
    if (i > n) {
      break;
    }
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let numbers = [];
  let i = 1;
  while (true) {
    if (i >= n + 1) {
      break;
    }
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let numbers = [];
  let i = 0;
  while (i < n) {
    i++;
    numbers.push(i);
  }
  return numbers;
}
```

```js
function count(n) {
  let numbers = [];
  let i = 0;
  while (i <= n - 1) {
    i++;
    numbers.push(i);
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  let numbers = [];
  while (i <= n) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  let numbers = [];
  while (i < n + 1) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  const numbers = [];
  while (i <= n) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  const numbers = [];
  while (i < n + 1) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  let numbers = [];
  while (i <= n) {
    numbers = numbers.concat([i]);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  let numbers = [];
  while (i < n + 1) {
    numbers = numbers.concat([i]);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  let numbers = [];
  while (true) {
    if (i > n) {
      break;
    }
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 1;
  let numbers = [];
  while (true) {
    if (i >= n + 1) {
      break;
    }
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 0;
  let numbers = [];
  while (i < n) {
    i++;
    numbers.push(i);
  }
  return numbers;
}
```

```js
function count(n) {
  let i = 0;
  let numbers = [];
  while (i <= n - 1) {
    i++;
    numbers.push(i);
  }
  return numbers;
}
```

```js
function count(N) {
  let result = [];
  let count = 1;
  while (count <= N) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let result = [];
  let count = 1;
  while (count < N + 1) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  const result = [];
  let count = 1;
  while (count <= N) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  const result = [];
  let count = 1;
  while (count < N + 1) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let result = [];
  let count = 1;
  while (count <= N) {
    result = result.concat([count]);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let result = [];
  let count = 1;
  while (count < N + 1) {
    result = result.concat([count]);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let result = [];
  let count = 1;
  while (true) {
    if (count > N) {
      break;
    }
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let result = [];
  let count = 1;
  while (true) {
    if (count >= N + 1) {
      break;
    }
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let result = [];
  let count = 0;
  while (count < N) {
    count++;
    result.push(count);
  }
  return result;
}
```

```js
function count(N) {
  let result = [];
  let count = 0;
  while (count <= N - 1) {
    count++;
    result.push(count);
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  let result = [];
  while (count <= N) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  let result = [];
  while (count < N + 1) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  const result = [];
  while (count <= N) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  const result = [];
  while (count < N + 1) {
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  let result = [];
  while (count <= N) {
    result = result.concat([count]);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  let result = [];
  while (count < N + 1) {
    result = result.concat([count]);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  let result = [];
  while (true) {
    if (count > N) {
      break;
    }
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 1;
  let result = [];
  while (true) {
    if (count >= N + 1) {
      break;
    }
    result.push(count);
    count++;
  }
  return result;
}
```

```js
function count(N) {
  let count = 0;
  let result = [];
  while (count < N) {
    count++;
    result.push(count);
  }
  return result;
}
```

```js
function count(N) {
  let count = 0;
  let result = [];
  while (count <= N - 1) {
    count++;
    result.push(count);
  }
  return result;
}
```
