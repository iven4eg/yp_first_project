# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

# Загрузка переменных из .env
load_dotenv()

# Теперь переменные доступны через os.environ
def secret_key():
    secret_key = os.getenv('SECRET_KEY')
    return f'{secret_key}' # Выведет: 12345

def author():
    author = os.getenv('AUTHOR')
    return author
