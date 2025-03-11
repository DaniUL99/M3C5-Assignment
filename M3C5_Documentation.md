***
# 1.- ¿Qué es un condicional?
Es un tipo de código que nos da una respuesta dependiendo de si una condición es verdadera o falsa.

__Sintaxis:__
```python
if condición:
    respuesta
```

__Por ejemplo:__\
*Queremos que si el número es par nos devuelva un texto que diga que es par.*
```python
number = 8

if number % 2 == 0:
    print("it's an even number")
```

Aunque podamos crear un condicional funcional solo con `if`, si queremos crear un condicional más dinámico que nos ofrezca y tenga en cuenta más opciones, podemos combinar `if` con `elif` y/o `else`.

- `if` sirve para introducir una condición.
- `elif` (`else if` en otros lenguajes) sirve para introducir una nueva condición (y respuesta) en el caso de que no se cumpliera la anterior.
- `else` sirve para ofrecer una respuesta alternativa en el caso de no cumplir ninguna de las condiciones anteriores.

__Sintaxis:__
```python
if condición:
    respuesta
elif condición:
    respuesta
else:
    respuesta
```
__Por ejemplo:__\
*Queremos que responda de formas diferentes dependiendo de si el numero es más grande, más pequeño o igual a 10.*
```python
number = 6

if number > 10:
    print("it's bigger")
elif number < 10:
    print("it's smaller")
else:
    print("it's equal")
```		

### Ternary operators
Nos permiten crear un condicional `if else` en una sola línea, y de implementarse de forma correcta, hace que el código sea más fácil de leer.
No es recomendable usarla con condicionales muy complejos.

__Sintaxis:__
```python
valor_si_verdadero if condición else valor_si_falso
```
__Por ejemplo:__\
*Queremos crear un condicional que nos devuelva si podemos conducir o no dependiendo de si tenemos 18 años o más.*
```python
age = 20

# Sin operadores ternarios
if age >= 18:
drive = “can drive”
else:
drive = “cannot drive”

# Con operadores ternarios
drive = “can drive” if age >= 18 else “cannot drive”
```

### Algunos operadores que podemos usar con condicionales:

Operadores de comparación:
- `==` los elementos tienen igual valor
- `!=` los elementos no tienen igual valor
- `>` el primer elemento es mayor que el segundo
- `<` el primer elemento es menor que el segundo
- `>=` el primer elemento es igual o mayor que el segundo
- `<=` el primer elemento es igual o menor que el segundo

Otros operadores:
- `in`
Sirve para crear una condición en la que x valor tendrá que encontrarse en la variable.

__Sintaxis:__
```python
if valor_a_buscar in variable:
    respuesta
```
__Por ejemplo:__\
*Queremos que busque la palabra "apple" en la lista y que si la encuentra devuelva una cosa y si no otra.*
```python
fruits = ['banana', 'orange', 'apple', 'pear']

if "apple" in fruits:
    print("found it!")
else:
    print("couldn't find it")
```
- `and`
Hace que se tengan que cumplir todas las condiciones para que sea Verdadero.

__Sintaxis:__
```python
if condición and condición:
    respuesta
```
__Por ejemplo:__\
*Queremos que mire si el número es múltiplo de 3 y mayor que diez, y dependiendo de si cumple estas dos condiciones, la respuesta sea "Verdadero" o "Falso".*
```python
number = 6

if number % 3 == 0 and number > 10:
    print(True)
else:
    print(False)

# En este caso solo cumple una de las condiciones, así que la respuesta será "False"
```
- `or`
Hace que se tengan que cumplir al menos una de las condiciones para que sea Verdadero.

__Sintaxis:__
```python
if condición or condición:
    respuesta
```
__Por ejemplo:__\
*Queremos que mire si el número es múltiplo de 3 y mayor que diez, y dependiendo de si cumple al menos una de estas dos condiciones, la respuesta sea "Verdadero" o "Falso".*
```python
number = 6

if number % 3 == 0 or number > 10:
    print(True)
else:
    print(False)

# En este caso cumple al menos una de las condiciones, así que la respuesta será "True"
```
- `and not`
Hace que la primera condición deba ser verdadera y la segunda falsa para que sea Verdadero.

__Sintaxis:__
```python
if condición_a_cumplir and not condición_a_no_cumplir:
    respuesta		
```
__Por ejemplo:__\
*Queremos que mire si el número es múltiplo de 3 y no mayor que diez, y dependiendo de si cumple estas condiciones, la respuesta sera "Verdadero" o "Falso".*
```python
number = 6

if number % 3 == 0 and not number > 10:
    print(True)
else:
    print(False)

# En este caso cumple la primera condicion y la segunda no, así que la respuesta será "True"
```

***
# 2.- ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?
Los bucles (loops) sirven para repetir un bloque de código varias veces. Al no tener que repetir la misma tarea una y otra vez, ayudan a crear un código más eficiente y limpio.\
Hay dos tipos de bucles: `for` y `while`.

### Bucles `for`
Los bucles `for` (tambien llamados bucles "for-in") ejecutan el código tantas veces como elementos haya en la secuencia/iterable. 

__Sintaxis:__
```python
for elemento in secuencia/iterable:
    respuesta
```

__Por ejemplo, con una lista de nombres:__\
*Queremos hacer un bucle que nos devuelva todos los nombres que hay en la lista, de uno en uno.*
```python
birds = ["magpie", "blackbird", "robin", "sparrow"]

for bird in birds:
    print(bird)
```
***
__Nota__\
Aunque en realidad se pueda usar cualquier palabra, se considera una buena práctica que en el caso de que el nombre de la colección sea un plural (en este caso *"birds"*), que la forma para referirse a los elementos o la variable iterante sea el mismo nombre pero en singular (*"bird"*).
***

Si utilizamos un bucle `for` con un string (cadena), este nos devolvera el string de elemento a elemento (como deletrado).

__Por ejemplo, con un string:__\
*Queremos que nos deletree la palabra que tenemos en el string.*

```python
string = "Daniel"

for letter in string:
    print(letter)
```

### Bucles `while`
Los bucles `while` siguen ejecutando el código siempre que se siga cumpliendo la condición. Si no se fijan limites puede seguir funcionando de forma infinita, por lo que hay que tener cuidado.
```python
while condición:
respuesta
```

__Por ejemplo:__\
*Queremos que coja el número y mire si es mayor que 10, si no es mayor de diez queremos que lo imprima y que le sume 1, y que vuelva a repetir el código hasta que el número sea mayor que 10.*
```python
number = 0

while number < 10:
    print(number)
    number += 1
```
***
# 3.- ¿Qué es una lista por comprensión en Python?
Una lista por comprensión (comprehension list) es una herramienta que nos permite crear una nueva lista basada en otra lista o rango usando una sola línea de código. 

__Sintaxis:__
```python
variable = [expresión/operación for elemento in secuencia/iterable]
```

__Por ejemplo, con una lista de nombres:__\
*Queremos crear una nueva lista con los nombres de pájaros de la lista “birds”, pero queremos que los nombres estén en mayúsculas.*
```python
birds = ["magpie", "blackbird", "robin", "sparrow"]

# Sin lista por comprensión
upper_birds = []
for bird in birds:
    upper_birds.append(bird.upper())

# Con lista por comprensión
upper_birds = [bird.upper() for bird in birds]
```

__Por ejemplo, con un rango:__\
*Queremos crear una nueva lista usando el rango de números de 1 a 10, pero queremos que cada número este multiplicado por 2.*
```python
numbers = range(1,11)

# Sin lista por comprensión
mult_numbers = []
for num in numbers:
    mult_numbers.append(num * 2)

# Con lista por comprensión
mult_numbers = [num * 2 for num in numbers]
```

### Condicional
Si usamos una condicional en la lista por comprensión, podremos hacer que la nueva lista solo tenga los valores que cumplan esa condición. 

__Sintaxis:__
```python
variable = [elemento for elemento in secuencia/iterable if condición]
```

__Por ejemplo, con una lista de nombres:__\
*Queremos crear una nueva lista con los nombres de pájaros de la lista “birds”, pero solo queremos nombres que contengan la letra “a”.*
```python
birds = ["magpie", "blackbird", "robin", "sparrow"]

# Sin lista por comprensión
a_birds = []
for bird in birds:
    if "a" in bird:
        a_birds.append(bird)

# Con lista por comprensión
a_birds = [bird for bird in birds if "a" in bird]
```

__Por ejemplo, con un rango:__\
*Queremos crear una nueva lista usando el rango de números de 1 a 10, pero solo queremos los números que sean múltiplos de 3.*
```python
numbers = range(1,11)

# Sin lista por comprensión
numbers_three = []
for num in numbers:
    if num % 3 == 0:
        numbers_three.append(num)

# Con lista por comprensión
numbers_three = [num for num in numbers if num % 3 == 0]
```
***

# 4.- ¿Qué es un argumento en Python?
Un argumento es un valor que se pasa a la función al llamarlo. Aunque argumento y parámetro suelan utilizarse como sinónimos, en realidad los parámetros son los nombres listados en la definición de la función (los que van entre los paréntesis), y los argumentos son los valores que recibe la función, los valores asignados a cada parámetro.

```python
def nombre_funcion(parametros):
    respuesta

nombre_funcion(argumentos)
```

### Argumentos posicionales
Este tipo de argumentos se pasan a la función según el orden en el que están definidos. Si en la función el argumento está en la primera posición, al pasarlo también tendremos que ponerlo el primero, y así sucesivamente.

__Por ejemplo:__
```python
def full_name(first, last):
  print(f'{first} {last}')

full_name('Daniel', 'Unamuno')
```

### Argumentos predeterminados
Este tipo de argumento sirve para que la función reciba un valor predeterminado en el caso de que no se le pase un argumento a la hora de llamarlo. Si le pasamos un argumento se utilizara este.

```python
def nombre_funcion(parametro = valor_predeterminado):
	respuesta
```
__Por ejemplo:__
```python
def greeting(name = 'Guest'):
  print(f'Hi {name}!')

# No pasamos nada en el argumento, usará el predeterminado y devolverá "Hi Guest!"
greeting()

# Pasamos un valor en el argumento, devolverá "Hi Dani!"
greeting('Dani')
```

__¡Muy importante!__\
Nunca se debe usar una lista o cualquier otro tipo de dato mutable como argumento predeterminado.

### Argumentos nombrados
En este tipo de argumento, en vez de poner solo los valores asignados a cada argumento, utilizaremos también los nombres que hemos definido en la función. Esto nos permitirá pasar los argumentos sin tener que preocuparnos por el orden.
```python
def nombre_funcion(arg_a, arg_b):
    respuesta

nombre_funcion(arg_b = valor, arg_a = valor)
```
__Por ejemplo:__\
```python
def full_name(first, last):
  print(f'{first} {last}')

full_name(last = 'Unamuno', first = 'Daniel')
```

### Argumentos arbitrarios
Es un tipo de argumento muy útil para cuando no se sabe cuántos argumentos se van a pasar a la función. Basta con poner `*args` donde irían los parámetros de la función, y devolverá los argumentos como tuplas.
Aunque en realidad se pueda usar cualquier nombre después de la *, se considera buena práctica utilizar `*args`.

```python
def nombre_funcion(*args):
    respuesta

nombre_funcion(argumentos)
```
__Por ejemplo:__\
```python
def dog_names(*args):
    print(dog_names)

dog_names('Nika', 'Indi', 'Kuba', 'Argi')
```
También podemos poner otros parámetros antes del `*args`, pero tendremos que asegurarnos de que cuando vayamos a pasar los argumentos lo hagamos en el orden adecuado o nombrando el que no queremos que sea parte del `*args`.

```python
def nombre_funcion(arg_1, *args):
    respuesta

nombre_funcion(arg_1 = valor, argumentos)
```

__Por ejemplo:__\
*Queremos pasar un día de la semana y uno o varios nombres/apellidos, y que nos devuelva un saludo.*
```python
def greeting(weekday, *args):
    print(f"Good {weekday}, {' '.join(args)}!")

greeting('Monday', 'Daniel', 'Unamuno')
```

### Argumentos keyword (palabra clave)
Funcionan de forma parecida a los argumentos arbitrarios, pero utilizan la palabra `**kwargs` en vez de `*args`, y recogen argumentos nombrados y devuelven diccionarios.
```python
def nombre_funcion(**kwargs):
    respuesta

nombre_funcion(llave = valor, llave = valor)
```

__Por ejemplo:__\
*Queremos pasar nombre y apellido, y que nos los devuelva como diccionario.*
```python
def greeting(**kwargs):
    print(kwargs)

greeting(first = 'Daniel', last = 'Unamuno')
```

***
# 5.- ¿Qué es una función Lambda en Python?
Es un tipo de función que utiliza la palabra clave `lambda`, se escribe en una sola línea de código, y suele ser más simple y fácil de leer que una función convencional.

Una de sus diferencias más importantes comparada con una función convencional es que aunque pueda tener más de un argumento, solo puede tener una sola expresión.

__Sintaxis:__
```python
variable = lambda argumentos : expresión

print(variable(argumentos))
```
__Por ejemplo:__\
*Queremos crear una función que tome 3 argumentos y devuelva la suma de los 3.*
```python
# Función convencional
def suma(num_one, num_two, num_three):
    print(num_one + num_two + num_three) 

suma(1, 2, 3)

# Función lambda
suma_dos = lambda num_one, num_two, num_three: num_one + num_two + num_three

print(suma(1, 2, 3))
```

Las funciones lambda deberían usarse sólo para funciones simples y cuando su uso facilite la lectura y comprensión del código, para funciones más complejas es mejor usar la forma convencional.
***
# 6.- ¿Qué es un paquete pip?
Un paquete pip es una colección de módulos de código Python que requiere el uso del gestor de paquetes pip para ser instalado. Python tiene funciones que se pueden usar directamente (built-in), otros que están en la biblioteca estándar pero que hay que importar (como math), y otros que hay que importar de fuera de Python (los paquetes pip). Todos estos paquetes sirven para agregar funciones y herramientas a Python, dándole versatilidad y eficiencia al código.

[Python Package Index](https://pypi.org/), también conocido como PyPI o Python Cheese Shop, es un repositorio de paquetes Python y lo podemos utilizar para buscar paquetes que instalaremos con pip. 

### Instalar pip
Si has instalado Python mediante la página de [python.org](python.org), ya deberías de tener pip instalado. Para comprobar que pip esté instalado y saber qué versión es, escribiremos esto en la terminal:
```
pip --version
```
Esto debería devolver qué versión de pip está instalada y en qué carpeta (asegúrate de que esté instalada en la carpeta de python). 

Si ves que no está instalada, la opción más simple es instalar una nueva versión de Python desde la página de [python.org](python.org), y este ya debería de traer pip consigo.

Para actualizar la versión de pip basta con poner esto en la terminal:
```
pip install --upgrade pip
```

### Instalar paquete pip

Para instalar un paquete usando pip, primero buscamos el paquete que queremos instalar en [PyPI](https://pypi.org/), y después ponemos este código con el nombre del paquete donde pone “sample”:
```
pip install sample
```
Para comprobar que se ha instalado correctamente, podemos volver a poner el mismo código y nos debería de poner que el requisito ya está satisfecho y en qué carpeta está instalado.

Para actualizar un paquete pondremos esto:
```
pip install --upgrade sample
```

Y para desinstalarlo esto:
```
pip uninstall sample
```

Después, cuando queramos utilizar el paquete que hemos instalado, simplemente tendremos que importarlo al repl de Python:
```python
import sample
```
***
