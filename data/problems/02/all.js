const functions = [];

function f0(n) {
  let sum = 0;
  let i = 1;
  while (i <= n) {
    sum += i;
    i++;
  }
  return sum;
}
functions.push(f0);
function f1(n) {
  let sum = 0;
  let i = 0;
  while (i < n) {
    sum += i + 1;
    i++;
  }
  return sum;
}
functions.push(f1);
function f2(n) {
  let sum = 0;
  while (n > 0) {
    sum += n;
    n--;
  }
  return sum;
}
functions.push(f2);
function f3(n) {
  let sum = 0;
  while (n >= 0) {
    sum += n;
    n--;
  }
  return sum;
}
functions.push(f3);
function f4(n) {
  let sum = 0;
  let i = n;
  while (i > 0) {
    sum += i;
    i--;
  }
  return sum;
}
functions.push(f4);
function f5(n) {
  let sum = 0;
  let i = n;
  while (i >= 0) {
    sum += i;
    i--;
  }
  return sum;
}
functions.push(f5);
function f6(n) {
  let i = 1;
  let sum = 0;
  while (i <= n) {
    sum += i;
    i++;
  }
  return sum;
}
functions.push(f6);
function f7(n) {
  let i = 0;
  let sum = 0;
  while (i < n) {
    sum += i + 1;
    i++;
  }
  return sum;
}
functions.push(f7);
function f8(n) {
  let i = n;
  let sum = 0;
  while (i > 0) {
    sum += i;
    i--;
  }
  return sum;
}
functions.push(f8);
function f9(n) {
  let i = n;
  let sum = 0;
  while (i >= 0) {
    sum += i;
    i--;
  }
  return sum;
}
functions.push(f9);
function f10(n) {
  let sum = 0;
  let i = 0;
  while (i < n) {
    i++;
    sum += i;
  }
  return sum;
}
functions.push(f10);
function f11(n) {
  let sum = 0;
  let i = 0;
  while (i <= n - 1) {
    i++;
    sum += i;
  }
  return sum;
}
functions.push(f11);
function f12(n) {
  let sum = 0;
  let i = n + 1;
  while (i > 0) {
    i--;
    sum += i;
  }
  return sum;
}
functions.push(f12);
function f13(n) {
  let sum = 0;
  let i = n + 1;
  while (i >= 1) {
    i--;
    sum += i;
  }
  return sum;
}
functions.push(f13);
function f14(n) {
  let i = 0;
  let sum = 0;
  while (i < n) {
    i++;
    sum += i;
  }
  return sum;
}
functions.push(f14);
function f15(n) {
  let i = 0;
  let sum = 0;
  while (i <= n - 1) {
    i++;
    sum += i;
  }
  return sum;
}
functions.push(f15);
function f16(n) {
  let i = n + 1;
  let sum = 0;
  while (i > 0) {
    i--;
    sum += i;
  }
  return sum;
}
functions.push(f16);
function f17(n) {
  let i = n + 1;
  let sum = 0;
  while (i >= 1) {
    i--;
    sum += i;
  }
  return sum;
}
functions.push(f17);
function f18(n) {
  let sum = 0;
  let i = 0;
  while (true) {
    sum += i;
    i++;
    if (i > n) {
      break;
    }
  }
  return sum;
}
functions.push(f18);
function f19(n) {
  let sum = 0;
  let i = n;
  while (true) {
    sum += i;
    i--;
    if (i < 1) {
      break;
    }
  }
  return sum;
}
functions.push(f19);
function f20(n) {
  let sum = 0;
  while (true) {
    sum += n;
    n--;
    if (n < 1) {
      break;
    }
  }
  return sum;
}
functions.push(f20);
function f21(n) {
  let sum = 0;
  let i = n;
  while (true) {
    sum += i;
    i--;
    if (i < 0) {
      break;
    }
  }
  return sum;
}
functions.push(f21);
function f22(n) {
  let sum = 0;
  while (true) {
    sum += n;
    n--;
    if (n < 0) {
      break;
    }
  }
  return sum;
}
functions.push(f22);
function f23(n) {
  let sum = 0;
  let i = n;
  while (true) {
    sum += i;
    i--;
    if (i <= 0) {
      break;
    }
  }
  return sum;
}
functions.push(f23);
function f24(n) {
  let sum = 0;
  while (true) {
    sum += n;
    n--;
    if (n <= 0) {
      break;
    }
  }
  return sum;
}
functions.push(f24);
function f25(n) {
  let i = 0;
  let sum = 0;
  while (true) {
    sum += i;
    i++;
    if (i > n) {
      break;
    }
  }
  return sum;
}
functions.push(f25);
function f26(n) {
  let i = n;
  let sum = 0;
  while (true) {
    sum += i;
    i--;
    if (i < 1) {
      break;
    }
  }
  return sum;
}
functions.push(f26);
function f27(n) {
  let i = n;
  let sum = 0;
  while (true) {
    sum += i;
    i--;
    if (i < 0) {
      break;
    }
  }
  return sum;
}
functions.push(f27);
function f28(n) {
  let i = n;
  let sum = 0;
  while (true) {
    sum += i;
    i--;
    if (i <= 0) {
      break;
    }
  }
  return sum;
}
functions.push(f28);
function f29(n) {
  let sum = n;
  while (n > 0) {
    n--;
    sum += n;
  }
  return sum;
}
functions.push(f29);
function f30(n) {
  let sum = n;
  while (n >= 1) {
    n--;
    sum += n;
  }
  return sum;
}
functions.push(f30);
function all() {
  for (let i = 0; i < functions.length; i++) {
    const f = functions[i];

    const tests = [];
    tests.push(test(f, 0, 0));
    tests.push(test(f, 1, 1));
    tests.push(test(f, 2, 3));
    tests.push(test(f, 3, 6));
    tests.push(test(f, 4, 10));
    tests.push(test(f, 100, 5050));

    if (!tests.every(Boolean)) {
      console.log(i, tests);
    }
  }
}

function test(f, input, output) {
  return f(input) == output;
}

all();
