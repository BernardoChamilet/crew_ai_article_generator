from dotenv import load_dotenv
import os
from pathlib import Path

# Caminho absoluto até o diretório principal onde o .env está localizado
env_path = Path(__file__).resolve().parent.parent.parent / '.env'

# Carregando variáveis de ambiente
load_dotenv(dotenv_path=env_path)

secret_key = os.getenv('SECRET_KEY')

debug = bool(os.getenv('DEBUG'))

port = int(os.getenv('PORT'))