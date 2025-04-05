---
Write a JavaScript function that returns whether a number is perfect using a "while" loop.
---

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 0;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 0;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 0;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 0;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 0;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 0;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 1) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 1) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 1) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n + 1 <= 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n + 1 <= 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n + 1 <= 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 0;
  while (i <= n * 0.5) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i <= n ** 0.5) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum - n == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let sum = 0;
  let i = 1;
  while (i <= Math.sqrt(n)) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum - n == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (i * i <= n) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let sum = 1;
  let i = 2;
  while (Math.pow(i, 2) <= n) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 0;
  let sum = 0;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let i = 0;
  let sum = 0;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 0;
  let sum = 0;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let i = 0;
  let sum = 0;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 0;
  let sum = 0;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let i = 0;
  let sum = 0;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 1) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 1) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 1) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 1) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n + 1 <= 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i <= n / 2) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n + 1 <= 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i < n) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n + 1 <= 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i <= n - 1) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 0;
  let sum = 0;
  while (i <= n * 0.5) {
    if (n % i == 0) {
      sum += i;
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i <= n ** 0.5) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum - n == n;
}
```

```js
function isPerfect(n) {
  if (n <= 0) {
    return false;
  }

  let i = 1;
  let sum = 0;
  while (i <= Math.sqrt(n)) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum - n == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (i * i <= n) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(n) {
  if (n < 2) {
    return false;
  }

  let i = 2;
  let sum = 1;
  while (Math.pow(i, 2) <= n) {
    if (n % i == 0) {
      sum += i;
      if (i !== n / i) {
        sum += n / i;
      }
    }
    i++;
  }
  return sum == n;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 0;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let result = 0;
  let index = 0;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 0;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let result = 0;
  let index = 0;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 0;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let result = 0;
  let index = 0;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 1) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 1) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 1) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N + 1 <= 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N + 1 <= 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N + 1 <= 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 0;
  while (index <= N * 0.5) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index <= N ** 0.5) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result - N == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let result = 0;
  let index = 1;
  while (index <= Math.sqrt(N)) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result - N == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (index * index <= N) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let result = 1;
  let index = 2;
  while (Math.pow(index, 2) <= N) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 0;
  let result = 0;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let index = 0;
  let result = 0;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 0;
  let result = 0;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let index = 0;
  let result = 0;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 0;
  let result = 0;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let index = 0;
  let result = 0;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 1) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 1) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 1) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 1) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N + 1 <= 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index <= N / 2) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N + 1 <= 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index < N) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N + 1 <= 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index <= N - 1) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 0;
  let result = 0;
  while (index <= N * 0.5) {
    if (N % index == 0) {
      result += index;
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index <= N ** 0.5) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result - N == N;
}
```

```js
function isPerfect(N) {
  if (N <= 0) {
    return false;
  }

  let index = 1;
  let result = 0;
  while (index <= Math.sqrt(N)) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result - N == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (index * index <= N) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result == N;
}
```

```js
function isPerfect(N) {
  if (N < 2) {
    return false;
  }

  let index = 2;
  let result = 1;
  while (Math.pow(index, 2) <= N) {
    if (N % index == 0) {
      result += index;
      if (index !== N / index) {
        result += N / index;
      }
    }
    index++;
  }
  return result == N;
}
```
