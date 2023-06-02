<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2023/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>16-May-2022</td><td>FECHA FIN:</td><td>20-May-2022</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">RECURSOS:
    <ul>
        <li>https://www.w3schools.com/python/python_reference.asp</li>
        <li>https://docs.python.org/3/tutorial/</li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE:
<ul>
<li>Ing. Anibal Sardon</li>
</ul>
</td>
</<tr>
<tr><td colspan="6">ALUMNO:
<ul>
<li>Roni Companocca Checco</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

# Python

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

#

## OBJETIVOS TEMAS Y COMPETENCIAS

## 1. Competencias del curso

-   General: C.c. Dise ̃na responsablemente aplicaciones web, sus componentes o procesos para satisfacer necesidades dentro de restricciones realistas: econ ́omicas, medio ambientales, sociales, pol ıticas,  ́eticas, de salud, de seguridad, manufacturaci ́on y sostenibilidad.
-   Especıfica: C.m. Construye responsablemente soluciones con tecnolog ́ıa web siguiendo un proceso adecuado llevando a cabo las pruebas ajustada a los recursos disponibles del cliente.
- Especıfica: C.p. Aplica de forma flexible t ́ecnicas, m ́etodos, principios, normas, est ́andares y herramientas del desarrollo web necesarias para la construcci ́on de aplicaciones web e implementaci ́on de estos sistemas en una organizaci ́on.

## 2. Resultado del estudiante

-   La capacidad de crear, seleccionar y utilizar t ́ecnicas, habilidades, recursos y herramientas modernas de ingenier ́ıa y tecnolog ́ıas de la informaci ́on, incluyendo la predicci ́on y el modelamiento, con una comprensi ́on de las limitaciones.

## 3. Equipos, materiales y temas

- Sistema Operativo (GNU/Linux de preferencia).
- GNU Vim.
- Python 3.
- Git.
- Cuenta en Github con el correo institucional.
- Entorno virtual.

## 4. Directorio de trabajo

- Cree su directorio de trabajo.
- Luego, diríjase a este directorio, para clonar su repositorio y continuar sus practicas.


                         Listing 1: Creando directorio de trabajo

            $ mkdir -p $HOME/rescobedoq/


                         Listing 2: Dirij ́ıendonos al directorio de trabajo

            $ cd $HOME/rescobedoq/


                         Listing 3: Clonando repositorio GitHub

            $ git clone [URL_DE_SU_GITHUB_PRIVADO]


                         Listing 4: Creando directorio para laboratorio

            $ mkdir -p $HOME/rescobedoq/pw2-lab-c-23a/lab04/exercises/

- Siempre evalue utilizar un archivo .gitignore para no considerar algunos archivo innecesarios sobre todo para el repositorio GitHub.
- Pueden haber varios de estos archivos, ubicados estrat ́egicamente, por ejemplo sólo para un laboratorio particular.


                         Listing 5: Creando .gitignore
   
            $ vim $HOME/rescobedoq/pw2-lab-c-23a/lab04/.gitignore


                         Listing 6: Ejemplo de .gitignore

            my_env/bin/*
            my_env/lib/*
            my_env/src/__pycache__/*
            *.pyc
            Tarea-del-Ajedrez/__pycache__/*

## 5. Marco teórico

-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/

### 5.1 Python

- Python es un lenguaje de programaci ́on interpretado no fuertemente tipado.

### 5.2 Instalación en GNU/Linux

- Para instalar Python 3 en cualquier distribución GNU/Linux use sus mismos repositorios. Por ejemplo en sistemas operativos compatibles con GNU/Linux Debian use alguno de los dos comandos siguientes:

            
                         Listing 1: Instalar Python en GNU/Linux
            
            $ sudo apt-get install python3
            # apt-get install python3
            

### 5.3 Instalación en MS Windows

- Para descarga en sistemas MS Windows https://www.python.org/downloads/windows/
- Descargar e instalar en sistemas operativos MS Windows, por lo general es muy sencillo. Además si usted es un usuario nativo de windows este proceso será casi intuitivo. No tenga miedo de instalar estos programas todo es software libre, asi que no necesitará parches o cracks.

***Instalación en Windows 10 - 64 bits***
<a href="https://ibb.co/DRJ9qns"><img src="https://i.ibb.co/G56WhjB/aistalacion.jpg" alt="aistalacion" border="0"></a>

### 5.4 Instalación en MacOS

- Para instalar Python 3 en sistemas MacOS puede descargar el instalador desde urlhttps://www.python.org/downloads/macos/ o usar brew:

            
                         Listing 2: Instalar Python en Mac
            
            $ brew install python
            

### 5.5 Comprobar versión

- Debe comprobar que la instalación y el reconocimiento del compilador ya estan presentes en su sistema operativo:

            
                         Listing 3: Verificando versión de Python
            
            $ python3 --version

***Versión***
#
<a href="https://ibb.co/TYnbh1F"><img src="https://i.ibb.co/0mWFJKd/tabla-1.jpg" alt="tabla-1" border="0"></a>
            
### 5.6 Directorio de trabajo

- Cree el directorio para estudiar ejercicios para este laboratorio.
- Luego, dir ́ıjase a este directorio y desarrolle diferentes ejercicicios de entrenamiento.

            
                         Listing 4: Creando directorio para ejercicios de este laboratorio
            
            $ mkdir -p $HOME/rescobedoq/pw2-lab-c-23a/lab04/exercises
            
#
            
                         Listing 5: Dirijíendonos al directorio de ejercicios
            
            $ cd $HOME/rescobedoq/pw2-lab-c-23a/lab04/exercises
            
<a href="https://imgbb.com/"><img src="https://i.ibb.co/KLwhvDN/tabla-2.jpg" alt="tabla-2" border="0"></a>

### 5.7 Hola mundo

- Cree su primer ejercicio helloworld.py

            
                         Listing 6: Creando el archivo helloworld.py
            
            $ vim helloworld.py
            
#
            
                         Listing 7: helloworld.py
            
            print("Hello World!");
            

- Para ejecutar su script helloworld.py ejecute el siguiente comando:

            
                         Listing 8: Ejecutando el script helloworld.py
            
            $ python3 helloworld.py

***Creando el archivo helloworld.py***
#
<a href="https://imgbb.com/"><img src="https://i.ibb.co/mNdb6Mx/aistall-2.jpg" alt="aistall-2" border="0"></a>

***Ejecutando el script helloworld.py***
#
<a href="https://imgbb.com/"><img src="https://i.ibb.co/2y394Jk/aistall-1.jpg" alt="aistall-1" border="0"></a>

***Corriendo nuestro primer ejemplo python ¡Hola Mundo!***      
<a href="https://ibb.co/qkP60Lz"><img src="https://i.ibb.co/Ln2KQDM/python-2.jpg" alt="python-2" border="0"></a>

***Commit para agregar el ejemplo python a nuestro repositorio remoto***
<a href="https://ibb.co/HNZB3MT"><img src="https://i.ibb.co/28JWHL3/python-3.jpg" alt="python-3" border="0"></a>

### 5.8 Comentarios en Python

- Los comentarios en Python sólo se aplican por cada línea.
- Pero usted puede utilizar várias técnicas para comentar en el editor Vim.


                         Listing 9: Comentar rango de líneas 5-10

            :3,5s/^/#


                         Listing 10: Comentar todas las líneas que tengan la palabra print

            :g/print/s/^/#

***Comentarios en python***
#
<a href="https://imgbb.com/"><img src="https://i.ibb.co/z4pLQD6/aimag1.jpg" alt="aimag1" border="0"></a>

***Commit para ir guardando los cambios de los comentarios***
<a href="https://imgbb.com/"><img src="https://i.ibb.co/Wt2qDqc/aimag2.jpg" alt="aimag2" border="0"></a>

### 5.9 Virtual Environment

- La reutilización de código fuente (paquetes, librerias, plugins, etc.) de terceros nos permite construir software más complejo, sobre todo con menos tiempo.
- En NodeJS se usaban paquetes instalados en el directorio de trabajo y no de manera global, registrando estos paquetes en sus versiones en el archivo package.json.
- Por eso este modo de trabajo nos permite tener distintos proyectos con distintas bibliotecas, de distintas versiones, en la misma máquina, sin que existan conflictos.
- Para compartir el proyecto se debe compartir el archivo package.json y luego llamar a ”npm install” para instalar las bibliotecas adecuadas para el proyecto.
- Java usa ant y maven, junto con archivos xml para realizar estas tareas.
- Python tiene virtualenv, para crear este espacio de trabajo.
- Python utiliza el manejador de paquetes pip.

### 5.10 Pip

- Instalemos pip, una herramienta que instalará y administrará los paquetes de programación que queramos usar en nuestros proyectos de desarrollo.


                         Listing 11: Instalación de pip

            $ sudo apt-get install -y python3-pip

### 5.11 Garantizando configuraci ́on para entorno virtual

- Paquetes y herramientas de desarrollo más para instalar para garantizar que tengamos una configuración sólida para nuestro entorno de programación.


                         Listing 12: Instalaci ́ones previas para entorno virtual

            $ sudo apt-get install build-essential libssl-dev libffi-dev python3-dev

### 5.12 Configurando entorno virtual

- Los entornos virtuales permiten tener un espacio aislado en los proyectos Python
- Garantizando que cada proyecto pueda tener su propio conjunto de dependencias que no interrumpir ́an a otros proyectos.
- Manejando diferentes versiones de los paquetes. Esto es especialmente importante cuando se trabaja con paquetes de terceros.
- Puede varios entornos de programación.
- Cada entorno es un directorio en la que se ubicaran sus scripts.
- Usaremos el módulo venv , que es parte de la biblioteca est ́andar de Python.
- Instalemos venv escribiendo:


                         Listing 13: Instalación del entorno virtual

            $ sudo apt install -y python3-venv

### 5.13 Crear un directorio para entorno virtual

- Para crear un ambiente elija en qué directorio se va trabajar con entorno virtual.


                         Listing 14: Creando directorio para entorno virtual

            $ mkdir -p $HOME/rescobedoq/pw2-lab-c-23a/lab04/exercises/my_env

### 5.14 Crear entorno virtual en un directorio

- En el directorio crea un entorno virtual ejecutando el siguiente comando:


                         Listing 15: Creando entorno virtual
            
            $ cd $HOME/rescobedoq/pw2-lab-c-23a/lab04/exercises/my_env
            $ virtualenv -p python3 .

### 5.15 Estructura de un entorno virtual

- Estudie la estructura del entorno virtual.
- Dentro del directorio para el entorno virtual se debi ́o crear un subdirectorio src/ con el siguiente contenido:
    
            
            .
            ├── bin
            │   ├── activate
            │   ├── activate.csh
            │   ├── activate.fish
            │   ├── activate.nu
            │   ├── activate.ps1
            │   ├── activate_this.py
            │   ├── deactivate.nu
            │   ├── pip
            │   ├── pip3
            │   ├── pip-3.9
            │   ├── pip3.9
            │   ├── python -> /usr/bin/python3
            │   ├── python3 -> python
            │   ├── python3.9 -> python
            │   ├── wheel
            │   ├── wheel3
            │   ├── wheel-3.9
            │   └── wheel3.9
            ├── lib
            │   └── python3.9
            ├── pyvenv.cfg
            └── src
            
## 6. Ejercicios

### 6.1 Matriz escalar

- Ejercicios sobre matrices de tama ̃no NxN.
- Determine si una matriz es escalar:

        
                     Listing 18: esEscalar.py
        
        def esEscalar(m):
            d = m[0][0]
            for i in range(len(m)):
                for j in range(len(m)):
                    if i != j:
                        if m[i][j] != 0:
                            print(m[i][j])
                            return False
                    elif m[i][j] != d:
                        print(m[i][j])
                        return False
            return True
        

- Pruebe el método esEscalar()

        
                     Listing 19: testEsEscalar.py
        
        import esEscalar as fu

        def prueba(M):
            if (fu.esEscalar(M)):
                print("Si es escalar")
            else:
                print("No es escalar")

        #Z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        #Z = [[1, 2, 3], [4, 1, 6], [7, 8, 1]]
        Z = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        prueba(Z)
        

### 6.2 Matriz unitaria

- Ejercicios sobre matrices de tama ̃no NxN.
- Determine si una matriz es unitaria:

        
                     Listing 20: esUnitaria.py
        
        import esEscalar as fu

        def esUnitaria(m):
            return m[0][0] == 1 and fu.esEscalar(m)
        

- Pruebe el m ́etodo esUnitaria()

        
                     Listing 21: testEsUnitaria.py
        
        import esUnitaria as fu

        def prueba(M):
            if (fu.esUnitaria(M)):
                print("Si es unitaria")
            else:
                print("No es unitaria")

        #Z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        #Z = [[1, 2, 3], [4, 1, 6], [7, 8, 1]]
        Z = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
        #Z = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        prueba(Z)
        

## 7. Tarea

- En esta tarea usted pondr ́a en pr ́actica sus conocimientos de programaci ́on en Python para dibujar un tablero de Ajedrez.
- La parte gráfica ya est ́a programada, usted sólo tendr ́a que concentrarse en las estructuras de datos subyacentes.
- Con el código proporcionado usted dispondrá de varios objetos de tipo Picture para poder realizar su tarea:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/svxt2F8/caballo-1.jpg" alt="caballo-1" border="0"></a>

- Estos objetos estar ́an disponibles importando la biblioteca: chessPictures y estar ́an internamente representados con arreglos de strings que podr ́a revisar en el archivo pieces.py
- La clase Picture tiene un s ́olo atributo: el arreglo de strings img, el cual contendr ́a la representaci ́on en caracteres de la figura que se desea dibujar.
- La clase Picture ya cuenta con una funci ́on implementada, no debe modificarla, pero si puede usarla para implementar sus otras funciones:
- invColor: recibe un color como un caracter de texto y devuelve su color negativo, tambi ́en como texto, deber ́a revisar el archivo colors.py para conocer los valores negativos de cada caracter.
- La clase Picture contar ́a adem ́as con varios m ́etodos que usted deber ́a implementar:

      • verticalMirror: Devuelve el espejo vertical de la imagen

      • horizontalMirror: Devuelve el espejo horizontal de la imagen

      • negative: Devuelve un negativo de la imagen

      • join: Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual

      • up: Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual

      • under: Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual

      • horizontalRepeat: Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n

      • verticalRepeat: Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de n

- Tenga en cuenta que para implementar todos estos m ́etodos, s ́olo deber ́a trabajar sobre la representaci ́on interna de un Picture, es decir su atributo img.
- Para dibujar una objeto Picture bastar ́a importar el m ́etodo draw de la biblioteca interpreter y usarlo de la siguiente manera:

             Listing 22: Importando en método draw() de interpreter

    $ python3
    Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
    [GCC 10.2.1 20210110] on linux
    Type "help", "copyright", "credits" or "license" for more information.

    >>> from chessPictures import *
    >>> from interpreter import draw
    pygame 1.9.6
    Hello from the pygame community. https://www.pygame.org/contribute.html
    >>> draw(rock)

<a href="https://imgbb.com/"><img src="https://i.ibb.co/WspwXzH/caballo-2.jpg" alt="caballo-2" border="0"></a>

- Ejercicios:
      • Para resolver los siguientes ejercicios s ́olo est ́a permitido usar ciclos, condicionales, definici ́on de listas por comprensi ́on, sublistas, map, join, (+), lambda, zip, append, pop, range.
      • Implemente los m ́etodos de la clase Picture. Se recomienda que implemente la clase picture por etapas, probando realizar los dibujos que se muestran en la siguiente preguntas.
      • Usando  ́unicamente los m ́etodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw):
- Pregunta: Explique el directorio pycache. 

<a href="https://ibb.co/N7cZ0Y2"><img src="https://i.ibb.co/1bF8C2G/caballo-3.jpg" alt="caballo-3" border="0"></a>
<a href="https://ibb.co/TPMbgbX"><img src="https://i.ibb.co/P1G969p/caballo-4.jpg" alt="caballo-4" border="0"></a>
<a href="https://ibb.co/v1mVJY2"><img src="https://i.ibb.co/0qZmftP/caballo-5.jpg" alt="caballo-5" border="0"></a>
<a href="https://ibb.co/vYwhwrW"><img src="https://i.ibb.co/TLv1vnG/caballo-6.jpg" alt="caballo-6" border="0"></a>
<a href="https://ibb.co/ynvsYgP"><img src="https://i.ibb.co/WW8KPB5/caballo-7.jpg" alt="caballo-7" border="0"></a>

## 8. Entregables

- En el informe siempre se debe agregar un enlace al directorio de su laboratorio en su repositorio Github privado donde se vea est ́e el c ́odigo fuente.
- No olvide que el profesor debe ser siempre colaborador a su repositorio (Usuario del profesor @rescobedoq).
- Para ser considerado con la calificaci ́on de m ́axima nota elab ́orelo en Latex.
- Usted debe describir los commits m ́as importantes que marcaron hitos en su trabajo, adjutando capturas de pantalla, del commit, del c ́odigo fuente, de sus ejecuciones y pruebas.
- En el informe siempre se debe explicar las im ́agenes (c ́odigo fuente, capturas de pantalla, commits, ejecuciones, pruebas, etc.) con descripciones puntuales pero precisas.

### Cuestionario

-   ¿Qué son los archivos *.pyc?
-   ¿Para qué sirve el directorio __pycache__?
-   ¿Cuáles son los usos y lo que representa el subguión en Python?

#
## 9. Rúbrica

### 9.1. Rúbrica para entregable Informe

   - Tabla 1: Rúbrica para tipo de Informe
<a href="https://ibb.co/MGDbC9d"><img src="https://i.ibb.co/CM5qHWL/tabla-3.jpg" alt="tabla-3" border="0"></a>

### 9.2. Rúbrica para el contenido del Informe y demostración

- El alumno debe marcar o dejar en blanco en celdas de la columna Checklist si cumplio con el ítem correspondiente.
- Si un alumno supera la fecha de entrega, su calificaci ́on ser ́a sobre la nota m ́ınima aprobada, siempre y cuando cumpla con todos lo items.
- El alumno debe autocalificarse en la columna Estudiante de acuerdo a la siguiente tabla:

    - Tabla 2: Niveles de desempeño

<a href="https://ibb.co/jzD7QzQ"><img src="https://i.ibb.co/vhk2ThT/tabla-4.jpg" alt="tabla-4" border="0"></a>

    - Tabla 3: Rúbrica para contenido del Informe y demostración

<a href="https://ibb.co/bb9PQfM"><img src="https://i.ibb.co/8YZ0NhL/tabla-5.jpg" alt="tabla-5" border="0"></a>

## 10. Referencias

-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
