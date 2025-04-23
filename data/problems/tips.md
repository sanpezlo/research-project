# Tips

## Por haer

```
TODO: comentario
```

## Generacion automatica

expandir codigo (`++`, `--`, `+=`, `-=`, ...)
cambiar el nombre de las funciones
cambiar el nombre de las variables
cambiar el orden de parametros????????????

## Generacion manual

### correct

Cambiar nombre de las variables y del parametro

Cambiar orden de declaracion de variables

Cambiar de ascendente a descendente (si se puede), aveces se borra el `i`, sino se establece el `i = n`

Cambiar operador logico del `while` (`<` - `<=`) o (`>` - `>=`)

Cambiar valores iniciales de variables (si se puede)

Agregar variables in-necesarias (de transformacion) ejem `count` (cuenta elementos del array) y `i` (index), son lo mismo

===

Agrupar por `transformation`, luego por `initial` y por `final`.

### initial

````
```initial
  // code
```
````

Cambiar las precondiciones `if`, cambiando de `<` a `<=` o `>` a `>=` y viceversa, en algunos casos pasan todos los test, por lo que no es una solucion valida.

Cambiar las precondiciones `if`, cambiando de Cambiar de `<` a `>` o `<=` a `>=` y viceversa.

Borrar las precondiciones `if`.

NO CAMBIAR: el valor de `i`.

Cambiar la el valor de la iniciaion de variables, en algunos casos pasan todos los test, por lo que no es una solucion valida.

### transformation

````
```transformation
  // code
```
````

Contenido del `while`:

- Borrar transformacion (si no genera un loop infinito).
- Cambiar valorles del contenido del `while`, si es `sum += i` cambiar a `sum += n`.
- Cambiar transformacion de operaciones, de `+=` a `-=`, `*=`, `/=` o cualquiera de las combinaciones.

`======`

loop infinito

Duplicar anterior

agregar `#(ignore-test)` en `final` si son todas o en cada codigo.

- Transformacion vacia
- Añadir transformacion correcta (si era `+=` dejar `+=`) y eliminar `i++;` o `i--;`

### final

````
```final
  // code
```
````

````
```js
  while (/* condicion */) {
    // code
  }
```
````

- Borrar retorno.
- Cambiar valor de retorno.

`======`

Duplicar anterior

cambion en el `while`

- Colocar retorno correcto.
- Cambiar de `<` a `<=` o `>` a `>=` y viceversa, en algunos casos pasan todos los test, por lo que no es una solucion valida.

`======`

loop infinito

Duplicar anterior

Agregar `#(ignore-test)` en `final` de todas.

Cambiar de `<` a `>` o `<=` a `>=` y viceversa.

<!-- Duplicar las soluciones y cambiar de `<` a `<=` o `>` a `>=` y viceversa. -->

===

## Estado inicial

Son las precondiciones necesarias para que un ciclo funcione correctamente, define las condiciones que deben cumplirse antes de que el bucle comience.

La funcion del estado inicial es que el propósito del ciclo (invariante) se cumpla antes del ciclo (y al menos en la primera iteracion ?????).

## Transformación de estado

Son las modificaciones necesarias para que el propósito del ciclo (invariante) se cumpla en cada iteración.

## Estado final

Define en que momento el ciclo termina, y que transformaciones debe realizar para cumplir con el propósito del ciclo (funcion).

---

En el estado inicial modifico el valor inicial de `i` ???
esto es un error de estado inicial o de transformacion o de estado final

ejemplo:

```js
function Sum1toN(n) {
  let i = 0; // si modifico a `i = 20`
  let sum = 0;
  while (i <= n) {
    sum += i;
    i++;
  }
  return sum;
}
```

resultado:

```js
function Sum1toN(n) {
  let i = 20; // 1
  let sum = 0;
  while (i - 20 <= n /* 2*/) {
    sum += i - 20; // 3
    i++;
  }
  return sum;
}
```

Esto sigue funcionando correctamente.

Aqui hay un problema de clasificacion, ya que hay una relacion entre modificar el estado inicial, la transformacion y el estado final. Donde la mayoria (no todas) de las modificacion del estado inicial, se pueden correguir en la transformacion o en el estado final.

entonces como clasificar si realizo todas las pisibles combinaciones?????

porque si solo esta el cambio `1` lo clasifico como `estado inicial` o `[transformacion de estaso, estado final]`, asi para las demas. Porque lo que tendria que ser error de `[estado inicial, transformacion de estado, estado final]` en verdad es una solucion valida.

---

## Mi conclusion

Si hago las modificaciones mencionadas (no todas), hace que el ciclo no se repita las veces correctas (sea porque no le falta o porque se pasa). Esto le perteneceria al estado final (a la condicion), que es el encargado de detener (o iniciar) el ciclo cuando se cumple la cantidad de itereciones.

Lo que estaba haciendo es solo modificar aqullas condiciones o valores iniciales que NO se pueden correguir en las demas secciones (de forma logica o razonable).

```js
function Sum1toN(n) {
  let i = 0;
  let sum = 0; // modificar a `sum = 1`
  while (i <= n) {
    sum += i;
    i++;
  }
  return sum;
}
```

Esto fallara aunque modifique las demas secciones ya que cuando `n = 0` retorna `1` y no `0`.

### Modificacion no razonable.

```js
function Sum1toN(n) {
  let i = 0;
  let sum = 1;
  while (i <= n) {
    if (i == 0) {
      sum = 0;
    }>
    sum += i;
    i++;
  }
  return sum;
}
```

Otra solucion sera que no sea posible combinar las clasificaciones, asi estara claro a que categoria pertenece.

---

Lo que daba por hecho es que las categorias definia la estructura del codigo, de la siguiente manera:

```js
function f1(n) {
  // estado inicial
  while ( /* estado final */) {
    // transformacion de estado
  }
  // estado final (esto estoy en duda ver, ## duda estado final)
}
```

Por eso el "lenguaje" que uso lo definia asi mismo. Hasta que me encontre con el siguiente codigo:

```js
function isPrime(num) {
  // inicial
  if (num <= 1) {
    return false;
  }
  let i = 2;
  // inicial

  while (i < num /* final */) {
    // transformacion
    if (num % i == 0) {
      return false;
    }
    i++;
    // transformacion
  }

  // final
  return true;
  // final
}
```

El codigo es correcto y funciona correctamente, pero si quiero definir un error de estado final, debo modificar la seccion de transformacion, ya que el `if` es el que determina cuando se detiene el ciclo (si el output esperado es `false`). la conducion del `while` tambien se involucra en detener el ciclo (si el output esperado es `true`).

Esto es problematico al automatizar las diferentes combinaciones de errores. Si fuciono los errores de estado de transformacion y estado final, lo que pensaba tomar era el bloque `transformation` de `transformation.md` y los bloques `js` y `final` de `final.md`.

Esto de nuevo, se soluciona si solo se permite una categoria, quitando por completo la multi-clasificacion de errores.

No considero viable realizar las difrentes combinaciones de errores manualmente (obviamente usando el "lenguaje"), es decir sin realizar un script que combine las secciones (Con las diferentes combinacines son 8 etiquetas).

---

## duda estado final

Lo que va en la seccion `final` la mayoria, por no decir todas las veces, es el `return` de la funcion.

Pero lo que estamos clasificacion son los ciclos no las funciones, por lo que retorne o no la funcion, no afectaria en la definicion de si es correcto o no el ciclo. Obviamente el `return` es muy importante en este sistema, ya que permite realizar tests automatizados.

```js
function average(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let avg = 0;
  let i = 0;
  while (i < numbers.length) {
    avg += numbers[i] / numbers.length;
    i++;
  }
  return avg;
}
```

El codigo anterior es correcto y el `return` es indiferente, ya que el ciclo realiza su proposito que es calcular el promedio de los numeros, lo que haga la funcion sobrepasa su scope (no es de su incumbencia).

```js
function average(numbers) {
  if (numbers.length == 0) {
    return null;
  }

  let sum = 0;
  let i = 0;
  while (i < numbers.length) {
    sum += numbers[i]; // 1
    i++;
  }
  return sum / numbers.length; // 2
}
```

Sin embargo en el codigo anterior, el `return` es importante ya que el ciclo no realiza su proposito, solo suma los numeros, por lo que el `return` es necesario para que se calcule el promedio de los numeros.

---

TODO: el problema 4, en final, hay una seccion vacia, porque no hay errores finales posibles cambiando los operadores del while, por lo tanto a la hora de hacer las mezclas de los diferentes tipos de errores, deben verificar que no esten vacios.

```
===

===
```

ejem (error initial con error final), al hacer esto sin verificar daria algunos con solo (error initial) y no combiandos.
