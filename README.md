# Mi Proyecto Final (Django)

Proyecto Django listo para subir a un repositorio remoto.

Pasos rápidos para subir desde PowerShell:

1. Inicializar repo local y primer commit:

   git init
   git add .
   git commit -m "Primer commit"

2. Crear repositorio remoto en GitHub (desde web) y conectar:

   git remote add origin https://github.com/<tu-usuario>/<tu-repo>.git
   git branch -M main
   git push -u origin main

3. Si necesitas configurar usuario:

   git config --global user.name "Tu Nombre"
   git config --global user.email "tu@correo.com"

Notas:

- Asegúrate de excluir `db.sqlite3` y credenciales en `.gitignore`.
- Si prefieres usar SSH, sustituye la URL HTTPS por la SSH.
