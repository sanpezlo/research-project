---
Write a JavaScript function that returns in an array the first N numbers of the Fibonacci sequence using a "while" loop.
---

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
  let i = 2;
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  const fib = [0, 1];
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
  let i = 2;
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  const fib = [0, 1];
```

```transformation
    fib.push(fib[i]);
    i++;
```

```transformation
    fib.push(fib[i - 1]);
    i++;
```

```transformation
    fib.push(fib[i - 2]);
    i++;
```

```transformation
    fib.push(fib[i - 1] + fib[i]);
    i++;
```

```transformation
    fib.push(fib[i] + fib[i - 1]);
    i++;
```

```transformation
    fib.push(fib[i] + fib[i - 2]);
    i++;
```

```transformation
    fib.push(fib[i - 2] + fib[i]);
    i++;
```

```transformation
    i++;
```

```final
  return fib;
```

```js
function fibonacci(n) {
  while (i < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  let i = 0;
  let j = 1;
  let count = 0;
  let fib = [];
```

```initial
  let fib = [];
  let i = 0;
  let j = 1;
  let count = 0;
```

```initial
  let count = 0;
  let fib = [];
  let i = 0;
  let j = 1;
```

```initial
  let j = 1;
  let count = 0;
  let fib = [];
  let i = 0;
```

```initial
  let i = 0;
  let j = 1;
  let count = 0;
  const fib = [];
```

```initial
  const fib = [];
  let i = 0;
  let j = 1;
  let count = 0;
```

```initial
  let count = 0;
  const fib = [];
  let i = 0;
  let j = 1;
```

```initial
  let j = 1;
  let count = 0;
  const fib = [];
  let i = 0;
```

```transformation
    let temp = i + j;
    i = j;
    j = temp;
    count++;
    fib.push(i);
```

```transformation
    let temp = i + j;
    i = j;
    fib.push(i);
    j = temp;
    count++;
```

```transformation
    fib.push(i);
    let temp = i + j;
    j = temp;
    i = j;
    count++;
```

```transformation
    fib.push(i);
    let temp = i - j;
    i = j;
    j = temp;
    count++;
```

```transformation
    fib.push(i);
    let temp = i * j;
    i = j;
    j = temp;
    count++;
```

```transformation
    fib.push(i);
    let temp = i / j;
    i = j;
    j = temp;
    count++;
```

```transformation
    count++;
```

```final
  return fib;
```

```js
function fibonacci(n) {
  while (count < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= count + 1) {
    //
  }
}
```

===

```initial
  let i = 0;
  let count = 0;
  let fib = [];
```

```initial
  let fib = [];
  let i = 0;
  let count = 0;
```

```initial
  let count = 0;
  let fib = [];
  let i = 0;
```

```initial
  let i = 0;
  let count = 0;
  const fib = [];
```

```initial
  const fib = [];
  let i = 0;
  let count = 0;
```

```initial
  let count = 0;
  const fib = [];
  let i = 0;
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i -= fib[count - 1];
    }
    count++;
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i *= fib[count - 1];
    }
    count++;
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i /= fib[count - 1];
    }
    count++;
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i += fib[count];
    }
    count++;
```

```transformation
    fib.push(i);
    if (i != 0) {
      i++;
    } else {
      i += fib[count - 1];
    }
    count++;
```

```transformation
    count++;
```

```final
  return fib;
```

```js
function fibonacci(n) {
  while (count < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= count + 1) {
    //
  }
}
```

===

```initial
  let i = 0;
  let fib = [];
```

```initial
  let fib = [];
  let i = 0;
```

```initial
  let i = 0;
  const fib = [];
```

```initial
  const fib = [];
  let i = 0;
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1]);
    }
    i++;
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2]);
    }
    i++;
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i]);
    }
    i++;
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i] + fib[i - 1]);
    }
    i++;
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i]);
    }
    i++;
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i] + fib[i - 2]);
    }
    i++;
```

```transformation
    if (i == 0) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i - 2]);
    }
    i++;
```

```transformation
    if (i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i - 1]);
    }
    i++;
```

```transformation
    i++;
```

```final
  return fib;
```

```js
function fibonacci(n) {
  while (i < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
```

```transformation
    fib.push(fib[fib.length - 1] + fib[fib.length]);
```

```transformation
    fib.push(fib[fib.length] + fib[fib.length - 1]);
```

```transformation
    fib.push(fib[fib.length - 2] + fib[fib.length]);
```

```transformation
    fib.push(fib[fib.length] + fib[fib.length - 2]);
```

```transformation
    fib.push(fib[fib.length - 1]);
```

```transformation
    fib.push(fib[fib.length - 2]);
```

```final
  return fib;
```

```js
function fibonacci(n) {
  while (fib.length < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (fib.length <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (fib.length + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > fib.length) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= fib.length) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= fib.length + 1) {
    //
  }
}
```

======

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
  let i = 2;
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  let fib = [0, 1];
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
  let i = 2;
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  const fib = [0, 1];
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
  let i = 2;
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let i = 2;
  const fib = [0, 1];
```

```transformation
    fib.push(fib[i]);
```

```transformation
    fib.push(fib[i - 1]);
```

```transformation
    fib.push(fib[i - 2]);
```

```transformation
    fib.push(fib[i - 1] + fib[i]);
```

```transformation
    fib.push(fib[i] + fib[i - 1]);
```

```transformation
    fib.push(fib[i] + fib[i - 2]);
```

```transformation
    fib.push(fib[i - 2] + fib[i]);
```

```transformation
    fib.push(fib[i - 1] + fib[i - 2]);
```

```transformation
    fib.push(fib[i - 2] + fib[i - 1]);
```

```transformation

```

```final
  #(ignore-test)
  return fib;
```

```js
function fibonacci(n) {
  while (i < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  let i = 0;
  let j = 1;
  let count = 0;
  let fib = [];
```

```initial
  let fib = [];
  let i = 0;
  let j = 1;
  let count = 0;
```

```initial
  let count = 0;
  let fib = [];
  let i = 0;
  let j = 1;
```

```initial
  let j = 1;
  let count = 0;
  let fib = [];
  let i = 0;
```

```initial
  let i = 0;
  let j = 1;
  let count = 0;
  const fib = [];
```

```initial
  const fib = [];
  let i = 0;
  let j = 1;
  let count = 0;
```

```initial
  let count = 0;
  const fib = [];
  let i = 0;
  let j = 1;
```

```initial
  let j = 1;
  let count = 0;
  const fib = [];
  let i = 0;
```

```transformation
    let temp = i + j;
    i = j;
    j = temp;
    fib.push(i);
```

```transformation
    let temp = i + j;
    i = j;
    fib.push(i);
    j = temp;
```

```transformation
    fib.push(i);
    let temp = i + j;
    j = temp;
    i = j;
```

```transformation
    fib.push(i);
    let temp = i - j;
    i = j;
    j = temp;
```

```transformation
    fib.push(i);
    let temp = i * j;
    i = j;
    j = temp;
```

```transformation
    fib.push(i);
    let temp = i / j;
    i = j;
    j = temp;
```

```transformation
    fib.push(i);
    let temp = i + j;
    i = j;
    j = temp;
```

```transformation

```

```final
  #(ignore-test)
  return fib;
```

```js
function fibonacci(n) {
  while (count < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= count + 1) {
    //
  }
}
```

===

```initial
  let i = 0;
  let count = 0;
  let fib = [];
```

```initial
  let fib = [];
  let i = 0;
  let count = 0;
```

```initial
  let count = 0;
  let fib = [];
  let i = 0;
```

```initial
  let i = 0;
  let count = 0;
  const fib = [];
```

```initial
  const fib = [];
  let i = 0;
  let count = 0;
```

```initial
  let count = 0;
  const fib = [];
  let i = 0;
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i -= fib[count - 1];
    }
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i *= fib[count - 1];
    }
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i /= fib[count - 1];
    }
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i += fib[count];
    }
```

```transformation
    fib.push(i);
    if (i != 0) {
      i++;
    } else {
      i += fib[count - 1];
    }
```

```transformation
    fib.push(i);
    if (i == 0) {
      i++;
    } else {
      i += fib[count - 1];
    }
```

```transformation

```

```final
  #(ignore-test)
  return fib;
```

```js
function fibonacci(n) {
  while (count < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (count + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= count) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= count + 1) {
    //
  }
}
```

===

```initial
  let i = 0;
  let fib = [];
```

```initial
  let fib = [];
  let i = 0;
```

```initial
  let i = 0;
  const fib = [];
```

```initial
  const fib = [];
  let i = 0;
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1]);
    }
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2]);
    }
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i]);
    }
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i] + fib[i - 1]);
    }
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i]);
    }
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i] + fib[i - 2]);
    }
```

```transformation
    if (i == 0) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i - 2]);
    }
```

```transformation
    if (i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i - 1]);
    }
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 1] + fib[i - 2]);
    }
```

```transformation
    if (i == 0 || i == 1) {
      fib.push(i);
    } else {
      fib.push(fib[i - 2] + fib[i - 1]);
    }
```

```transformation

```

```final
  #(ignore-test)
  return fib;
```

```js
function fibonacci(n) {
  while (i < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (i + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= i) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= i + 1) {
    //
  }
}
```

===

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  let fib = [0, 1];
```

```initial
  if (n == 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
```

```initial
  if (n <= 0) {
    return [];
  }
  if (n == 1) {
    return [0];
  }

  const fib = [0, 1];
```

```transformation

```

```final
  #(ignore-test)
  return fib;
```

```js
function fibonacci(n) {
  while (fib.length < n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (fib.length <= n - 1) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (fib.length + 1 <= n) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n > fib.length) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n - 1 >= fib.length) {
    //
  }
}
```

```js
function fibonacci(n) {
  while (n >= fib.length + 1) {
    //
  }
}
```
