import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'

response = urllib.request.urlopen(url)
html_content = response.read().decode()

with open(file='html_content_example.html', mode='w', encoding='utf-8') as file:
    file.write(html_content)


(?:<div\s*class=\"widgets-list__item\">)
(?:[\w\d\s=\"<>!\-]+?)
(?:<a[^>]*?class=\"org-widget-header__title-link\">)
(?P<name>[^<]+)
(?:</a>)
(?:[\w\d\s=\"<>!\-]+?)
(?:<span[^<]*</span>[^<]*<span[^<]*?class=\"org-widget-header__meta org-widget-header__meta--location\">)
(?P<address>[^<]+)
(?:</span>)
(?:[\w\d\s=\"<>!\-]+?)
(?:\n{2})