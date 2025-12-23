import re
import csv
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://msk.spravker.ru/avtoservisy-avtotehcentry/'

response = urllib.request.urlopen(url)
html_content = response.read().decode()

base_pattern = r'<div\s*class=\"widgets-list__item\">.+?\n{2}'
name_pattern = r'(?:class=\"org-widget-header__title-link\">)(?P<name>[^<\n]+)'
address_pattern = r'(?:class=\"org-widget-header__meta org-widget-header__meta--location\")>[^\S]*(?P<adress>[^<\n]+)'
phone_pattern = r'(?:class=\"org-widget__spec\")(?:.+?)(?:class=\"spec__value\">)(?P<phone>[^<\n]+)'
worktime_pattern = r'(?:class=\"org-widget__spec\")(?:.+?)(?:class=\"spec__value\">)(?:.+?)(?:class=\"spec__value\">)(?P<worktime>[^<\n]+)'
review_pattern = r'(?:class=\"org-widget-feedback__comment\">[^<]+<p>[^\S]*)(?P<review>[^<\n]+)'

regex_base = re.compile(base_pattern, re.DOTALL)
regex_name = re.compile(name_pattern, re.DOTALL)
regex_address = re.compile(address_pattern, re.DOTALL)
regex_phone = re.compile(phone_pattern, re.DOTALL)
regex_worktime = re.compile(worktime_pattern, re.DOTALL)
regex_review = re.compile(review_pattern, re.DOTALL)

match_base = re.findall(regex_base, html_content)
match_name = re.findall(regex_name, html_content)
match_address = re.findall(regex_address, html_content)
match_phone = re.findall(regex_phone, html_content)
match_worktime = re.findall(regex_worktime, html_content)
match = []

match_review = []
for base in match_base:
    review = re.search(regex_review, base)
    if review:
        match_review.append(review.group('review'))
match_review.append(review)

for name, address, phone, worktime, review in zip(match_name, match_address, match_phone, match_worktime, match_review):
    match.append((name, address, phone, worktime, review))

with open(file='data.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Phone', 'Worktime', 'Review'])

    for row in match:
        writer.writerow(row)