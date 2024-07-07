#Задание 1: Получение данных
# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

parameter = {"q" : "html"}


reslt = requests.get('https://api.github.com/search/repositories', params=parameter)

print(reslt.status_code)

pprint.pprint(reslt.json())

