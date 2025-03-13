# LoginRegisterHashing
### En esta App se realizó en Python🐍 con las siguientes herramientas:
- **Tkinter:** Interfaz gráfica.
  > pip install tkinter
- **bcrypt:** Hashing.
  > pip install bcrypt
- **SQLite3:** Base de datos.
  > pip install db-sqlite3

Consiste en un **programa** de *login* y *registro* con **encriptación de contraseñas** y **base de datos**.

Realizado con la finalidad de **aprender más** sobre la *seguridad de las contraseñas* y **saber cómo funciona** la *encriptación*, la *decodificación* y la *unión con la base de datos*.

# 📌 Explicación del Código

## 📁 Interfaz Gráfica

Es una única **GUI** hecha en **Tkinter** para el login y el registro que contiene un Entry de Usuario y Contraseña, y botones de Iniciar Sesión y Registrarse.

![alt text](asd/1.png)

## 📁 Base de Datos

La **base de datos** está en **SQLite3** y solo contiene la tabla de *Usuarios* con las columnas de *Id*, *Usuario* y *Contraseña*.
Es una conexión a una base de datos **muy simple** para este ejemplo de *Login* y *Register*.

### ❗ La columna de contraseñas está guardada como BLOB ❗
> Esto significa que la base de datos **no guarda las contraseñas en texto plano**, sino que las **almacena en un formato especial llamado BLOB** *(Binary Large Object)*, que **es una secuencia de bytes**.

![alt text](asd/2.png)

## 📁 Login y Register

Se comprueba que estén todos los campos rellenos y se aplica el **método de Hashing** a la contraseña.

![alt text](asd/3.png)

### Sobre bcrypt

**bcrypt** es una librería de hashing que se usa para almacenar contraseñas de **manera segura**.

> No es un algoritmo de cifrado, sino un método de hashing diseñado para proteger contraseñas contra ataques de fuerza bruta y diccionarios.

### Funcionalidad de bcrypt

#### 🔒 Encriptación / Registrar

1️⃣ Se obtiene el valor de la contraseña.  
2️⃣ Se aplica el algoritmo de *hashing*, agregando un **salt**.  
> El **salt** es un **valor aleatorio** que se agrega a la contraseña antes de ser hasheada, con la finalidad de que el **hash sea único**, *incluso si hay dos usuarios con la misma contraseña*.

![alt text](asd/4.png)

##### 🔍 Ejemplo sin salt (inseguro):

Si dos personas usan la contraseña "123456" y la hasheamos **sin salt**, ambos hashes serán idénticos:

| Usuario | Contraseña | Hash sin Salt |
|---------|------------|---------------|
| Juan    | 123456     | abc123        |
| Pedro   | 123456     | abc123        |

👉 ❗❕ Esto es **peligroso** porque permite identificar usuarios con la misma contraseña ❕❗

##### 🔐 Ejemplo con salt (seguro):

Ahora, si generamos un **salt aleatorio** para cada usuario:

| Usuario | Contraseña | **Salt** | Hash Con Salt |
|---------|------------|------|---------------|
| Juan    | 123456     | xyz  | abc987        |
| Pedro   | 123456     | pqr  | lmn654        |

##### 👉 Con el Salt se puede evitar: 🛑
- Ataques tipo *rainbow tables* (listas precalculadas de hashes de contraseñas comunes).
- Repetición de contraseñas.
- Ataques basados en diccionarios.
- Obtención de contraseñas por base de datos robada.

3️⃣ Se ingresa el hash a la base de datos.

![alt text](asd/5.png)

#### 🔑 Verificación / Iniciar Sesión

1️⃣ Se obtiene el valor de la contraseña a través de la búsqueda del usuario.  
2️⃣ Se verifica que la contraseña ingresada sea igual al hash almacenado en la base de datos, utilizando `bcrypt.checkpw()` y `.encode()`.  

![alt text](asd/6.png)

> **bcrypt.checkpw()** recupera la contraseña hasheada en la base de datos y la **compara** con la contraseña ingresada.  
> **bcrypt.encode()** convierte la contraseña a **bytes** para compararla con el hash almacenado en la base de datos.  

👉 ❗❕**Solo repite el proceso de hashing**❕❗  
> **No desencripta el hash porque los hashes son unidireccionales y no se pueden revertir***.  

3️⃣ Una vez comprobado que la contraseña ingresada es igual al hash almacenado en la base de datos, la condicional hace su trabajo.

![alt text](7.png)

# 📌 Conclusiones

Estoy seguro de que no es la única forma segura de almacenar contraseñas, pero es una buena herramienta para **aprender** sobre la seguridad de las contraseñas y el hashing.

Me surgió la **duda** de cómo podía aplicar una contraseña completamente segura, o al menos que sea mínimamente segura, a una base de datos y pudiese realizar un login y register.

Con esto me di cuenta de que las contraseñas hasheadas no se encriptan ni se desencriptan, sino que se utiliza el mismo método a la contraseña ingresada y se compara. Entonces, lo de encriptar y desencriptar es por pura comodidad **:P**.

[Sobre seguridad en Hashing](https://underc0de.org/foro/noticias-informaticas-120/tiempo-que-tardan-los-hackers-en-descifrar-algoritmos-de-hashing-modernos/msg163360/#msg163360)

[Sobre bcrypt](https://github.com/pyca/bcrypt)