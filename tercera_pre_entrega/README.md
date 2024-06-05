# Proyecto Django - Blog con Categorías y Etiquetas

Este proyecto es una aplicación web básica de blog desarrollada con Django. Permite crear y listar publicaciones (posts) junto con categorías y autores. También permite buscar posts por título, por autor y por categoría.

## Requisitos

- Python 3.6+
- Django 3.2+

## Instalación

1. Clona el repositorio:
    ```
    git clone https://github.com/tu_usuario/mi_proyecto.git
    cd mi_proyecto
    ```

2. Crea un entorno virtual y actívalo:
    ```
    pip install pipenv
    pipenv shell
    pip3 install Django


3. Realiza las migraciones:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo:
    ```
    python manage.py runserver
    ```

## Secciones y funcionalidades
El sistema cuenta con las siguientes secciones, cuyas funcionalidades serán brevemente comentadas a continuación: Ver Post, Crear Post, Crear Autor, Crear Categoria

### Página de Inicio

- Clickeando sobre Mi Blog  usted podrá dirigirse a la página de inicio, sin importar en que sección se encuentre.

### Ver Posts

- Podrás ver una lista de todos los posts.

### Crear un Nuevo Post

- Encontrarás un formulario donde podrás crear un post, pero ya tiene que estar creado autor y  categoría.

### Crear un Nuevo Autor

- Encontrarás un formulario donde podrás crar un nuevo autor.

### Crear una Nueva Categoría

- Encontrarás un formulario donde podrás crear una nueva categoría.

### Buscar Posts podes hacerlo por titulo, autor o categoria

- Navega a http://127.0.0.1:8000/blog/busqueda_post para buscar posts por título.
- Navega a http://127.0.0.1:8000/blog/busqueda_autor para buscar posts por autor.
- Navega a http://127.0.0.1:8000/blog/busqueda_categoria para buscar posts por categoria.



