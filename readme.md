Aquí tienes el `README.md` actualizado con valores de prueba para el archivo `.env`:

```markdown
# Book Management
Este es un proyecto para la gestión de libros, permitiendo a los usuarios añadir, editar, eliminar y visualizar libros desde una base de datos.

## Tecnologías
- **Django**: Framework web de alto nivel para Python.
- **Django REST Framework**: Extensión de Django para construir APIs RESTful.
- **MongoDB**: Base de datos NoSQL utilizada para almacenar los datos de los libros.
- **Python**: Lenguaje de programación utilizado para el desarrollo del backend.

## Instalación
Clona el repositorio:
```bash
git clone https://github.com/huacre1997/book_management.git
```
Navega al directorio del proyecto:
```bash
cd book_management
```
Instala las dependencias:
```bash
pip install -r requirements.txt
```

Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente formato:

```env
DJANGO_SECRET_KEY='test-django-secret-key'
MONGO_HOST='mongodb+srv://test.mongodb.net/?retryWrites=true&w=majority'
MONGO_USERNAME='test_user'
MONGO_PASSWORD='test_password'
MONGO_NAME='test_book_management'
```

## Uso
Ejecuta las migraciones:
```bash
python manage.py migrate
```
Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```
Accede a la aplicación en `http://127.0.0.1:8000`.

Para llenar la base de datos con datos de ejemplo, ejecuta el comando:
```bash
python manage.py insert_data
```

