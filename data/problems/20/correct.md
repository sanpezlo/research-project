---
Write a JavaScript function that returns in an array the first and last digit respectively of any number greater than or equal to 2 digits using a "while" loop.
---

```js
function firstLastDigit(num) {
  let lastDigit = num % 10;
  let firstDigit = num;
  while (firstDigit >= 10) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let lastDigit = num % 10;
  let firstDigit = num;
  while (firstDigit > 9) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let lastDigit = num % 10;
  let temp = num;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
  }
  let firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let lastDigit = num % 10;
  let temp = num;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
  }
  let firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let firstDigit = num;
  let lastDigit = num % 10;
  while (firstDigit >= 10) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let firstDigit = num;
  let lastDigit = num % 10;
  while (firstDigit > 9) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let temp = num;
  let lastDigit = num % 10;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
  }
  let firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let temp = num;
  let lastDigit = num % 10;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
  }
  let firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  const lastDigit = num % 10;
  let firstDigit = num;
  while (firstDigit >= 10) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  const lastDigit = num % 10;
  let firstDigit = num;
  while (firstDigit > 9) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  const lastDigit = num % 10;
  let temp = num;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
  }
  let firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  const lastDigit = num % 10;
  let temp = num;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
  }
  let firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let firstDigit = num;
  const lastDigit = num % 10;
  while (firstDigit >= 10) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let firstDigit = num;
  const lastDigit = num % 10;
  while (firstDigit > 9) {
    firstDigit = Math.floor(firstDigit / 10);
  }
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let temp = num;
  const lastDigit = num % 10;
  while (temp >= 10) {
    temp = Math.floor(temp / 10);
  }
  const firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(num) {
  let temp = num;
  const lastDigit = num % 10;
  while (temp > 9) {
    temp = Math.floor(temp / 10);
  }
  const firstDigit = temp;
  return [firstDigit, lastDigit];
}
```

```js
function firstLastDigit(n) {
  let last = n % 10;
  let first = n;
  while (first >= 10) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let last = n % 10;
  let first = n;
  while (first > 9) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let last = n % 10;
  let t = n;
  while (t >= 10) {
    t = Math.floor(t / 10);
  }
  let first = t;
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let last = n % 10;
  let t = n;
  while (t > 9) {
    t = Math.floor(t / 10);
  }
  let first = t;
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let first = n;
  let last = n % 10;
  while (first >= 10) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let first = n;
  let last = n % 10;
  while (first > 9) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let t = n;
  let last = n % 10;
  while (t >= 10) {
    t = Math.floor(t / 10);
  }
  let first = t;
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let t = n;
  let last = n % 10;
  while (t > 9) {
    t = Math.floor(t / 10);
  }
  let first = t;
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  const last = n % 10;
  let first = n;
  while (first >= 10) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  const last = n % 10;
  let first = n;
  while (first > 9) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  const last = n % 10;
  let t = n;
  while (t >= 10) {
    t = Math.floor(t / 10);
  }
  let first = t;
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  const last = n % 10;
  let t = n;
  while (t > 9) {
    t = Math.floor(t / 10);
  }
  let first = t;
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let first = n;
  const last = n % 10;
  while (first >= 10) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let first = n;
  const last = n % 10;
  while (first > 9) {
    first = Math.floor(first / 10);
  }
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let t = n;
  const last = n % 10;
  while (t >= 10) {
    t = Math.floor(t / 10);
  }
  const first = t;
  return [first, last];
}
```

```js
function firstLastDigit(n) {
  let t = n;
  const last = n % 10;
  while (t > 9) {
    t = Math.floor(t / 10);
  }
  const first = t;
  return [first, last];
}
```
