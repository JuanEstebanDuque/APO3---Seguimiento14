### Base de conocimiento

La base de conocimiento estará conformada por: las carreras de la universidad ICESI, con su precio, las aptitudes, debilidades y habilidades del usuario. Pero no solo esto, sino las reglas que asociarán las diferentes selecciones del usuario con la respuesta necesesaria.

Para plantear estas reglas, debemos definir cada una de las variables que vamos a usar. Para los aptitudes tenemos:

1. Creatividad y pensamiento innovador.
2. Habilidad para el diseño visual.
3. Pensamiento lógico.
4. Destreza en matemáticas.
5. Capacidad para identificar oportunidades.
6. Pensamiento analítico.
7. Capacidad para resolver problemas.
8. Capacidad para tomar decisiones basadas en datos.
9. Capacidad para argumentar persuasivamente.
10. Capacidad de negociación.
11. Habilidades empáticas y de escucha activa.
12. Capacidad para comprender el comportamiento humano.

Para las habilidades tenemos:

1. Comunicación Efectiva
2. Resolución de Problemas
3. Pensamiento Crítico
4. Creatividad
5. Capacidad de Aprendizaje Continuo
6. Trabajo en equipo
7. Adaptabilidad

Para las debilidades tenemos:

1. Falta de Paciencia
2. Timidez Extrema
3. Falta de Organización
4. Baja Tolerancia al Estrés
5. Poca Adaptabilidad al Cambio
6. Indecisión
7. Falta de enfoque

Por último, para las carreras tenemos:

1. Ingeniería en sistemas (12.960.000)
2. Diseño de medios interactivos (12.960.000)
3. Mercadeo internacional (13.580.000)
4. Finanzas (13.580.000)
5. Derecho (12.960.000)
6. Psicología (11.450.000)

### Reglas

Para la creación de cada regla primero analizaremos el gusto de la carrera que ingresó el usuario. Partiendo de eso, validaremos si las habilidades, debilidades y aptitudes coinciden con lo necesario para esa carrera que el usuario ingresó. Primero, se validará la primera habilidad ingresada. Luego, se empezarán a anidar las otras aptitudes marcadas, llevando así, a una carrera. Seguidamente se concatenan las habilidades y debilidades para retornar una carrera tomando en cuenta todo. Finalmente, se mostrará la primera opción ingresada (gusto), con las respuestas dadas por el sistema experto.

### Interfaz gráfica

Para la interfaz gráfica, primero se mostrará una ventana donde el usuario ingresará sus datos (nombre, apellido, edad y correo). Esto lo llevará a otra ventana que contendrá un input para que el usuario ingrese la opción de la carrera universitaría que tenía pensada. También habrá un menú desplegable que tendrá las carreras mencionadas, y 3 listas de checkboxes, habilidades, debilidades y aptitudes respectivamente. Ingresando esto, se dirigirá a otra ventana donde se mostrará el resultado, que contiene la opción de carrera universitaria digitada por el usuario al principio del proceso, y dos carreras recomendadas por el sistema experto.