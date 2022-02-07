## D.E.A.

### El sitio web permitirá gestionar usuarios y buscar DEAs en base a la geolocalización del usuario
**BBDD** SQLite3</br>
<a href="https://pypi.org/project/geopy/">**geopy**</a></br>
* El API será privada y gestionará usuarios y DEAs
* "CREATE TABLE users (id TEXT PRIMARY KEY UNIQUE, email TEXT UNIQUE, pwd TEXT, token TEXT);"

### Autenticar usuarios:
1. Esquema de los usuarios: </br>
    id TEXT </br>
    email TEXT </br>
    pwd TEXT </br>
    token TEXT  </br>
2. Autorización: </br> 
    **A** El token será guardado en una cookie | **TOKEN:** SECRET + Random</br>
    **B** Función **gen_token()** </br>
    **C** Decorador **@token** </br>
    * **NOTAS:**
    * make_response()</br>
    * set_cookie(<key:str>, <value:str>)
    * cookies() --> InmutableMultiDict

### Buscar DEA
* Esquema DEA: </br>
    * id TEXT</br>
    * name TEXT</br>
    * address TEXT</br>
    * X REAL</br>
    * Y REAL</br>
1. Una vez logueado el usuario, en la sección /find se listarán los 5 DEAs más a cercanos a su posición

* window.navigator.geolocation.getCurrentPosition()