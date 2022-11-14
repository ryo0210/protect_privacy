import re

phone_num_pattern = "\d{3}-\d{4}-\d{4}"
phone_num_pattern = re.compile(phone_num_pattern)
text = '電話番号：090-0000-0000'
print(phone_num_pattern.findall(text))

address_pattern = "\d{3}-\d{4}"
address_pattern = re.compile(address_pattern)
text = '123-4567'
print(address_pattern.findall(text))