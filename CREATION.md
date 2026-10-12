# Creamos venv

python -m venv .venv

# Activamos venv

source .venv/bin/activate

# Instalamos los requerimientos para la app

pip install -r requirements.txt

# Ejecutamos nuestra app

fastapi dev main.py
