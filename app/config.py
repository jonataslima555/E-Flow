from dotenv import find_dotenv, load_dotenv
from os import getenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())

# Garantir que DB_NAME sempre tenha um valor string
db_name = getenv('DB_NAME')
if db_name is None:
    raise ValueError("A variável de ambiente 'DB_NAME' não está definida.")
DB_NAME: str = db_name

