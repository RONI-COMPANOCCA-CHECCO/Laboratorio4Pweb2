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

## 4. MARCO CONCEPTUAL

-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/

#### 4.1 Python

- Python es un lenguaje de programaci ́on interpretado no fuertemente tipado.

#### 4.2 Instalaci ́on en GNU/Linux

- Para instalar Python 3 en cualquier distribuci ́on GNU/Linux use sus mismos repositorios. Por ejemplo en sistemas operativos compatibles con GNU/Linux Debian use alguno de los dos comandos siguientes:

            
                         Listing 1: Instalar Python en GNU/Linux
            
            $ sudo apt-get install python3
            # apt-get install python3
            

#### 4.3 Instalaci ́on en MS Windows

- Para descarga en sistemas MS Windows https://www.python.org/downloads/windows/
- Descargar e instalar en sistemas operativos MS Windows, por lo general es muy sencillo. Adem ́as si usted es un usuario nativo de windows este proceso ser ́a casi intuitivo. No tenga miedo de instalar estos programas todo es software libre, asi que no necesitar ́a parches o cracks.

#### 4.4 Instalaci ́on en MacOS

- Para instalar Python 3 en sistemas MacOS puede descargar el instalador desde urlhttps://www.python.org/downloads/macos/ o usar brew:

            
                         Listing 2: Instalar Python en Mac
            #
            $ brew install python
            

#### 4.5 Comprobar versi ́on

- Debe comprobar que la instalaci ́on y el reconocimiento del compilador ya estan presentes en su sistema operativo:

            
                         Listing 3: Verificando versi ́on de Python
            
            $ python3 --version
            
#### 4.6 Directorio de trabajo

- Cree el directorio para estudiar ejercicios para este laboratorio.
- Luego, dir ́ıjase a este directorio y desarrolle diferentes ejercicicios de entrenamiento.

            
                         Listing 4: Creando directorio para ejercicios de este laboratorio
            
            $ mkdir -p $HOME/rescobedoq/pw2-lab-c-23a/lab04/exercises
            
#
            
                         Listing 5: Dirij ́ıendonos al directorio de ejercicios
            
            $ cd $HOME/rescobedoq/pw2-lab-c-23a/lab04/exercises
            

#### 4.7 Hola mundo

- Cree su primer ejercicio helloworld.py

            
                         Listing 6: Creando el archivo helloworld.py
            
            $ vim helloworld.py
            
#
            
                         Listing 7: helloworld.py
            
            print("Hello World!");
            

- Para ejecutar su script helloworld.py ejecute el siguiente comando:

            
                         Listing 8: Ejecutando el script helloworld.py
            
            $ python3 helloworld.py
            

#### 4.15 Estructura de un entorno virtual

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
            
### 5. Ejercicios

#### 5.1 Matriz escalar

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
        

- Pruebe el m ́etodo esEscalar()

        
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
        

#### 5.2 Matriz unitaria

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
        

### 6. Tarea

- En esta tarea usted pondr ́a en pr ́actica sus conocimientos de programaci ́on en Python para dibujar un tablero de Ajedrez.
- La parte gráfica ya est ́a programada, usted sólo tendr ́a que concentrarse en las estructuras de datos subyacentes.
- Con el código proporcionado usted dispondrá de varios objetos de tipo Picture para poder realizar su tarea:

><a href="https://imgbb.com/"><img src="https://i.ibb.co/svxt2F8/caballo-1.jpg" alt="caballo-1" border="0"></a>

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

><a href="https://imgbb.com/"><img src="https://i.ibb.co/WspwXzH/caballo-2.jpg" alt="caballo-2" border="0"></a>

- Ejercicios:
      • Para resolver los siguientes ejercicios s ́olo est ́a permitido usar ciclos, condicionales, definici ́on de listas por comprensi ́on, sublistas, map, join, (+), lambda, zip, append, pop, range.
      • Implemente los m ́etodos de la clase Picture. Se recomienda que implemente la clase picture por etapas, probando realizar los dibujos que se muestran en la siguiente preguntas.
      • Usando  ́unicamente los m ́etodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw):
- Pregunta: Explique el directorio pycache. 

><a href="https://ibb.co/N7cZ0Y2"><img src="https://i.ibb.co/1bF8C2G/caballo-3.jpg" alt="caballo-3" border="0"></a>
><a href="https://ibb.co/TPMbgbX"><img src="https://i.ibb.co/P1G969p/caballo-4.jpg" alt="caballo-4" border="0"></a>
><a href="https://ibb.co/v1mVJY2"><img src="https://i.ibb.co/0qZmftP/caballo-5.jpg" alt="caballo-5" border="0"></a>
><a href="https://ibb.co/vYwhwrW"><img src="https://i.ibb.co/TLv1vnG/caballo-6.jpg" alt="caballo-6" border="0"></a>
><a href="https://ibb.co/ynvsYgP"><img src="https://i.ibb.co/WW8KPB5/caballo-7.jpg" alt="caballo-7" border="0"></a>

### 7. Entregables
- En el informe siempre se debe agregar un enlace al directorio de su laboratorio en su repositorio Github privado donde se vea est ́e el c ́odigo fuente.
- No olvide que el profesor debe ser siempre colaborador a su repositorio (Usuario del profesor @rescobedoq).
- Para ser considerado con la calificaci ́on de m ́axima nota elab ́orelo en Latex.
- Usted debe describir los commits m ́as importantes que marcaron hitos en su trabajo, adjutando capturas de pantalla, del commit, del c ́odigo fuente, de sus ejecuciones y pruebas.
- En el informe siempre se debe explicar las im ́agenes (c ́odigo fuente, capturas de pantalla, commits, ejecuciones, pruebas, etc.) con descripciones puntuales pero precisas.
#### Cuestionario

-   ¿Qué son los archivos *.pyc?
-   ¿Para qué sirve el directorio __pycache__?
-   ¿Cuáles son los usos y lo que representa el subguión en Python?

#
### 8. Rúbrica

><a href="https://ibb.co/j5zftCx"><img src="https://i.ibb.co/X4DLHnd/caballo-8.jpg" alt="caballo-8" border="0"></a>

### 9. Referencias

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

### 10. Observaciones

- Observaciones que se consideran en la calificación.

><a href="https://ibb.co/qWsLL9C"><img src="https://i.ibb.co/KLqcc7D/caballo-9.jpg" alt="caballo-9" border="0"></a>