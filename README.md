# PRE-PROYECTO-FINAL
En este proyecto armé una web para mi mismo. Comienza en la pestaña 'inicio' donde se puede ver información sobre mi carrera artistica como músico y más.
Dentro del proyecto, en la app 'App' cree 3 clases en models (Lanzamientos, Inscripcion, Programa), cada una de ellas cumple un rol distinto.
La clase 'Lanzamientos' tiene 3 atributos. Utilizando DB Browser cargué datos a dichos atributos para utilizarlos y mostrarlos en pantalla;
Luego cree la vista 'buscar_tracks' para ese modelo, en la cual importo todos los datos guardados en la base de datos y formo una lista con dichos datos.
Esto me permite crear una tabla dentro de un archivo .html, 'Biblioteca' en mi caso, para mostrar los datos que contienen los atributos de la clase 'Lanzamientos'.
Otra vista que se conecta con el mismo modelo es 'resultados_busqueda_canciones'. Aquí cree un formulario para buscar algun dato que perteneza a 'Lanzamientos';
En este caso se permite buscar el atributo 'nombre_del_lanzamiento'. Esto se realiza de la siguiente manera:
1. En el template 'biblioteca.html' hay un <form> en el cual podes ingresar 'Nombre del lanzamiento o cancion' y presionar el boton 'Buscar',
luego el action="{% url 'web-biblioteca-resultado' %}" te redirige a otro template 'resultados_busqueda.html' en el cual, sí la view 'resultado_busqueda_canciones'
comprueba que lo ingresado en el formulario está en la base de datos de la clase 'Lanzamientos' entonces guarda en una nueva variable el dato, luego en el template
utilizando la herramienta 'for i in list' buscamos el dato guardado por la view y lo mostramos en pantalla.

De manera analoga se realiza la busqueda en la base de datos para el modelo 'Programa'.

En el template 'creacionToolz' se pueden guardar datos en la base de datos conectada al modelo 'Inscripcion' y al formulario 'UsuarioFormulario'.
Primero cree la clase 'Inscripcion' con 3 atributos. Luego cree el formulario 'UsuarioFormulario' con los mismos atributos que la clase.
Desde una vista nueva llamada 'creacion_usuario' conecto el formulario y el modelo. Aquí le digo a la vista que los datos ingresados en el formulario
sean guardados en la base de datos del modelo.
