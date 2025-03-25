# Visualizador de películas de IMDB

![imagen](https://github.com/user-attachments/assets/f99e2187-1cca-4527-824d-247346ff5109)

Esta es una aplicación web para explorar películas de la base de datos de IMDB.  
El backend está hecho con Flask y el frontend con React.

## Instalación de dependencias

### 1) Backend (Flask)

Para instalar las dependencias del backend: 
```bash
cd backend
pip install -r requirements.txt
```

### 2) Frontend (React)
Para instalar las dependencias del frontend y buildear la app:
```bash
cd frontend
npm install
npm run build
```
Eso creará una carpeta "/build" en el directorio frontend, que será accedida por el backend.

## Uso

Para correr la aplicación:
```bash
cd backend
python app.py
```

La aplicación correrá en http://127.0.0.1:8000.

Abre http://localhost:8000 en tu navegador y explora las películas.
