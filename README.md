ESTRUCTURA DEL PROYECTO

```
├── PROYECTO FINAL/					<--- Carpeta del Repositorio
│ ├── blog/					    
│ │ ├── apps/	
│ │ │ ├── contacto/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── forms.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py	
│ │ │ ├── post/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── models.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ ├── user/
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── migrations/		    **Ignorada en el .gitignore**
│ │ │ │ ├── __init__.py
│ │ │ │ ├── admin.py
│ │ │ │ ├── apps.py
│ │ │ │ ├── forms.py
│ │ │ │ ├── models.py
│ │ │ │ ├── signals.py
│ │ │ │ ├── tests.py
│ │ │ │ ├── urls.py
│ │ │ │ └── views.py
│ │ │ └── ...
│ │ ├── blog/
│ │ │ ├── __pycache__/		    **Ignorada en el .gitignore**
│ │ │ ├── configurations/	    <--- Configuraciones django 
│ │ │ │ ├── __pycache__/	    **Ignorada en el .gitignore**
│ │ │ │ ├── local.py		    
│ │ │ │ ├── production.py	    
│ │ │ │ ├── settings.py		    
│ │ │ │ └── ...
│ │ │ ├── __init__.py
│ │ │ ├── asgi.py
│ │ │ ├── settings.py
│ │ │ ├── urls.py
│ │ │ ├── views.py
│ │ │ ├── wsgi.py
│ │ │ └── ...
│ │ ├── media/				    <--- Archivos multimedia - **gitignore
│ │ │ ├── post/
│ │ │ │ ├──cover/
│ │ │ │ └── ...
│ │ │ │ ├──default/
│ │ │ │ | ├──post_default.jpeg
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├──avatar/
│ │ │ │ └── ...
│ │ │ │ ├──default/
│ │ │ │ | ├──user_default.jpeg
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── static/				  
│ │ │ ├── assets/
│ │ │ │ ├── img/
│ │ │ │ └── ...
│ │ │ ├── css/
│ │ │ │ ├── style.css
│ │ │ │ └── ...
│ │ │ ├── js/
│ │ │ │ ├── main.js
│ │ │ │ └── tailwind.config.js
│ │ │ │ └── ...
│ │ │ └── ...
│ │ ├── templates/			  
│ │ │ ├── auth/
│ │ │ │ ├── auth_login.html
│ │ │ │ ├── auth_register.html
│ │ │ │ └── ...
│ │ │ ├── errors/
│ │ │ │ ├── not_found.html
│ │ │ │ ├── internal_error.html
│ │ │ │ └── ...
│ │ │ ├── Components/
│ │ │ │ ├── commons/
│ │ │ │ |  ├── footer.html
│ │ │ │ |  ├── header.html
│ │ │ │ └── ...
│ │ │ │ ├── ui/
│ │ │ │ |  ├── navbar.html
│ │ │ │ └── ...
│ │ │ ├── contacto/
│ │ │ │ ├── contacto.html
│ │ │ │ └── ...
│ │ │ ├── includes/
│ │ │ │ └── ...
│ │ │ ├── layout/
│ │ │ │ ├── auth_layout.html
│ │ │ │ ├── base_layout.html
│ │ │ │ ├── general_layout.html
│ │ │ │ ├── post_layout.html
│ │ │ │ └── ...
│ │ │ ├── post/
│ │ │ │ ├── post_delete.html
│ │ │ │ ├── post_detail.html
│ │ │ │ ├── post_list.html
│ │ │ │ ├── post_create.html
│ │ │ │ ├── post_update.html
│ │ │ │ └── ...
│ │ │ ├── user/
│ │ │ │ ├── user_profile.html
│ │ │ │ └── ...
│ │ │ ├── about.html
│ │ │ └── ...
│ │ │ ├── index.html
│ │ │ └── ...
│ │ ├── db.sqlite			    <--- Base de datos - **gitignore
│ │ ├── manage.py
│ │ └── ...
| ├── entorno/						<--- Carpeta del entorno - **gitignore
| │ ├── Scripts/
| │ │ ├── activate.bat
| │ │ ├── deactivate.bat
| │ │ └── ...
| │ └── ...
│ ├── .env
│ ├── .gitignore
│ ├── README.md				    <--- Archivo README.md - Describe el proyecto
│ ├── requeriments.txt		   
| └── ...
└── ...
```