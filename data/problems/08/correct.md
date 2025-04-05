---
Write a JavaScript function that returns in an array the first N numbers of the Fibonacci sequence using a "while" loop.
---

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
  while (i < n) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
  while (i <= n - 1) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let j = 1;
  let count = 0;
  let fib = [];
  while (count < n) {
    fib.push(i);
    let temp = i + j;
    i = j;
    j = temp;
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let count = 0;
  let fib = [];
  while (count < n) {
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i += fib[count - 1];
    }
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let fib = [];
  while (i < n) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i - 2]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let fib = [];
  while (i < n) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i - 1]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let j = 1;
  let count = 0;
  let fib = [];
  while (count <= n - 1) {
    fib.push(i);
    let temp = i + j;
    i = j;
    j = temp;
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let count = 0;
  let fib = [];
  while (count <= n - 1) {
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i += fib[count - 1];
    }
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let fib = [];
  while (i <= n - 1) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i - 2]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let fib = [];
  while (i <= n - 1) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i - 1]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (i < n) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (i < n) {
    fib.push(fib[i - 2] + fib[i - 1]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  while (fib.length < n) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  while (fib.length < n) {
    fib.push(fib[fib.length - 2] + fib[fib.length - 1]);
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (i <= n - 1) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (i <= n - 1) {
    fib.push(fib[i - 2] + fib[i - 1]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  while (fib.length <= n - 1) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  while (fib.length <= n - 1) {
    fib.push(fib[fib.length - 2] + fib[fib.length - 1]);
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
  while (fib.length < n) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
  while (fib.length <= n - 1) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (i < n) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (i <= n - 1) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let fib = [];
  let count = 0;
  let j = 1;
  let i = 0;
  while (count < n) {
    fib.push(i);
    let temp = i + j;
    i = j;
    j = temp;
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let fib = [];
  let count = 0;
  while (count < n) {
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i += fib[count - 1];
    }
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  const fib = [];
  let i = 0;
  while (i < n) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i - 2]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let fib = [];
  let i = 0;
  while (i < n) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i - 1]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let i = 0;
  let fib = [];
  let j = 1;
  let count = 0;
  while (count <= n - 1) {
    fib.push(i);
    let temp = i + j;
    i = j;
    j = temp;
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let fib = [];
  let count = 0;
  let i = 0;
  while (count <= n - 1) {
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i += fib[count - 1];
    }
    count++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let fib = [];
  let i = 0;
  while (i <= n - 1) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i - 2]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  let fib = [];
  let i = 0;
  while (i <= n - 1) {
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i - 1]);
    }
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
  while (i < n) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
  while (i < n) {
    fib.push(fib[i - 2] + fib[i - 1]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
  while (i <= n - 1) {
    fib.push(fib[i - 1] + fib[i - 2]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
  let i = 2;
  while (i <= n - 1) {
    fib.push(fib[i - 2] + fib[i - 1]);
    i++;
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (fib.length < n) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  }
  return fib;
}
```

```js
function fibonacci(n) {
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
  while (fib.length <= n - 1) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
  }
  return fib;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (a < numbers) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (a <= numbers - 1) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  let b = 1;
  let i = 0;
  const result = [];
  while (i < numbers) {
    result.push(a);
    const temp = a + b;
    a = b;
    b = temp;
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  let i = 0;
  const result = [];
  while (i < numbers) {
    result.push(a);
    if (a == 0) {
      a++;
    } else {
      a += result[i - 1];
    }
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  const result = [];
  while (a < numbers) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 1] + result[a - 2]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  const result = [];
  while (a < numbers) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 2] + result[a - 1]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  let b = 1;
  let i = 0;
  const result = [];
  while (i <= numbers - 1) {
    result.push(a);
    const temp = a + b;
    a = b;
    b = temp;
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  let i = 0;
  const result = [];
  while (i <= numbers - 1) {
    result.push(a);
    if (a == 0) {
      a++;
    } else {
      a += result[i - 1];
    }
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  const result = [];
  while (a <= numbers - 1) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 1] + result[a - 2]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  const result = [];
  while (a <= numbers - 1) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 2] + result[a - 1]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (a < numbers) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (a < numbers) {
    result.push(result[a - 2] + result[a - 1]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  while (result.length < numbers) {
    result.push(result[result.length - 1] + result[result.length - 2]);
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  while (result.length < numbers) {
    result.push(result[result.length - 2] + result[result.length - 1]);
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (a <= numbers - 1) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (a <= numbers - 1) {
    result.push(result[a - 2] + result[a - 1]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  while (result.length <= numbers - 1) {
    result.push(result[result.length - 1] + result[result.length - 2]);
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  while (result.length <= numbers - 1) {
    result.push(result[result.length - 2] + result[result.length - 1]);
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (result.length < numbers) {
    result.push(result[result.length - 1] + result[result.length - 2]);
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (result.length <= numbers - 1) {
    result.push(result[result.length - 1] + result[result.length - 2]);
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (a < numbers) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (a <= numbers - 1) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  const result = [];
  let i = 0;
  let b = 1;
  let a = 0;
  while (i < numbers) {
    result.push(a);
    const temp = a + b;
    a = b;
    b = temp;
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  const result = [];
  let i = 0;
  while (i < numbers) {
    result.push(a);
    if (a == 0) {
      a++;
    } else {
      a += result[i - 1];
    }
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  const result = [];
  let a = 0;
  while (a < numbers) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 1] + result[a - 2]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  const result = [];
  let a = 0;
  while (a < numbers) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 2] + result[a - 1]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  let a = 0;
  const result = [];
  let b = 1;
  let i = 0;
  while (i <= numbers - 1) {
    result.push(a);
    const temp = a + b;
    a = b;
    b = temp;
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  const result = [];
  let i = 0;
  let a = 0;
  while (i <= numbers - 1) {
    result.push(a);
    if (a == 0) {
      a++;
    } else {
      a += result[i - 1];
    }
    i++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  const result = [];
  let a = 0;
  while (a <= numbers - 1) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 1] + result[a - 2]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  const result = [];
  let a = 0;
  while (a <= numbers - 1) {
    if (a == 0 || a == 1) {
      result.push(a);
    } else {
      result.push(result[a - 2] + result[a - 1]);
    }
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (a < numbers) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (a < numbers) {
    result.push(result[a - 2] + result[a - 1]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (a <= numbers - 1) {
    result.push(result[a - 1] + result[a - 2]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers == 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  const result = [0, 1];
  let a = 2;
  while (a <= numbers - 1) {
    result.push(result[a - 2] + result[a - 1]);
    a++;
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (result.length < numbers) {
    result.push(result[result.length - 1] + result[result.length - 2]);
  }
  return result;
}
```

```js
function fibonacci(numbers) {
  if (numbers <= 0) {
    return [];
  }
  if (numbers == 1) {
    return [0];
  }

  let a = 2;
  const result = [0, 1];
  while (result.length <= numbers - 1) {
    result.push(result[result.length - 1] + result[result.length - 2]);
  }
  return result;
}
```
