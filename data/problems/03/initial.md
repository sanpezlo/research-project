---
Write a JavaScript function that returns in an array the numbers from 1 to N using a "while" loop.
---

```initial
  let numbers = [0];
```

```initial
  let numbers = [n];
```

```js
function count(n) {
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
  while (i <= n - 1) {
    i++;
    numbers.push(i);
  }
  return numbers;
}
```

===

```initial
  const numbers = [0];
```

```initial
  const numbers = [n];
```

```js
function count(n) {
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
  let i = 1;
  while (i < n + 1) {
    numbers.push(i);
    i++;
  }
  return numbers;
}
```

===

```initial
  let result = [0];
```

```initial
  let result = [N];
```

```js
function count(N) {
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
  while (count <= N - 1) {
    count++;
    result.push(count);
  }
  return result;
}
```

===

```initial
  const result = [0];
```

```initial
  const result = [N];
```

```js
function count(N) {
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
  let count = 1;
  while (count < N + 1) {
    result.push(count);
    count++;
  }
  return result;
}
```
