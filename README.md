# Sglass
#### Glasses-Shop — SSR Ecommerce Project on Django (FBV)

Sglass - This is a online glasses store offering basic features for users. The project is built on an SSR architecture and includes four applications: products, users, orders, and uses Function-Based Views (FBV).

#### Stack:
 - Pyhton
 - Django
 - PostgreSQL

And other small libraries specified in `requirements.txt`.

## Project Setup on Windows

### - Stack Installing
To begin, install: [Python](https://www.python.org/downloads/) | [PostgreSQL](https://www.postgresql.org/)
<br>
Links are provided to the latest version of the tools.

### - Cloning a Project from GitHub
Create a root directory on your computer, then open it in your code editor or terminal.
<br>
Next, write this command into the command line:
```powershell
https://github.com/S0fft/Sglass-Shop.git .
```
You will see the project files appear in your directory.

### - Creating Virtual Environment
Create virtual environment:
```powershell
python -m venv .venv
```

And activate it:

```powershell
.venv\Scripts\Activate
```

### - Installing Requirements
Next, install packages:

```powershell
python.exe -m pip install --upgrade pip
```
```powershell
pip install -r requirements.txt
```

### Applying Migrations
Using Migrations to Create a Database Structure

```powershell
python manage.py migrate
```

### Server Rise
Then, run server:

```powershell
python manage.py runserver
```

<details>
<summary><h2> Project Setup on Unix-Like Systems </h2></summary>
These commands do the same thing as described above but only on Unix systems:
<br>

### - Stack Installing
Install: [Python](https://www.python.org/downloads/) | [PostgreSQL](https://www.postgresql.org/)
<br>
Link are provided to the latest version of the tools.

### - Cloning a Project from GitHub
Create a root directory on your computer, then open it in your code editor or terminal.
<br>
Next, write this command into the command line:
```powershell
https://github.com/S0fft/Sglass-Shop.git .
```
You will see the project files appear in your directory.

### - Creating Virtual Environment
```bash
python3 -m venv ../venv
```

```bash
source ../venv/bin/activate
```

### - Installing Requirements
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
### Applying Migrations
Using Migrations to Create a Database Structure

```powershell
python3 manage.py migrate
```

### Server Rise
```powershell
python3 manage.py runserver
```
