# Tips

## Por haer

```
TODO: comentario
```

## Generacion automatica

expandir codigo (`++`, `--`, `+=`, `-=`, ...)
cambiar el nombre de las funciones

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

agregar `#(ignore-test)` en `final` si son todas o en cada codigo.

- Añadir transformacion correcta (si era `+=` dejar `+=`) y eliminar `i++;` o `i--;`
- Transformacion vacia

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

- Colocar retorno correcto.
- Cambiar de `<` a `<=` o `>` a `>=` y viceversa, en algunos casos pasan todos los test, por lo que no es una solucion valida.

`======`

loop infinito

Duplicar anterior

Agregar `#(ignore-test)` en `final` de todas.

Cambiar de `<` a `>` o `<=` a `>=` y viceversa.

Duplicar las soluciones y cambiar de `<` a `<=` o `>` a `>=` y viceversa.
