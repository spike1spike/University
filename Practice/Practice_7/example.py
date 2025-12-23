import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'

response = urllib.request.urlopen(url)
html_content = response.read().decode()

with open(file='html_content_example.html', mode='w', encoding='utf-8') as file:
    file.write(html_content)


pattern = r'''
    (?:.+?)                                                           # Начало html-файла
    (?:<div[^>]+?class\s*=\s*"[^"]+?list__item">)
    (?:.+?class\s*=\s*"[^"]+?title-link">)                              # Начало названия магазина
    (?P<name>[^<]+)                                                     # Название магазина
    (?:<.+?class\s*=\s*"[^"]+?location">)                               # Начало адреса
    (?P<address>[^<]+)                                                  # Адрес
    (?:<.+?class\s*=\s*"[^"]+?value">)                                  # Начало телефона
    (?P<phone>[^<]+)                                                    # Телефон
    (?:<.+?class\s*=\s*"[^"]+?value">)                                  # Начало часов работы
    (?P<workhours>[^<]+)                                                # Часы работы
    ((?:<.+?class\s*=\s*"[^"]+?feedback__comment">[^>]+>)(?P<review>[^<]+))?
    (?:<.+?(?:(?:</dl>\s+)|(?:</p>\s+))(?:</div>\s+)+)
'''