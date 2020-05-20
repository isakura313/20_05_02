
from collections import OrderedDict
favorite_languages = {'phil': '', 'edward':'', 'jen':'', 'sarah': ''}

favorite_languages['sarah'] = 'c'
favorite_languages['phil'] = 'golang'
favorite_languages['edward'] = 'ruby'
favorite_languages['jen'] = 'python'

print(favorite_languages)
new_order = OrderedDict(favorite_languages)
favorite_languages['semen'] = 'php'
new_order['semen'] = 'php'
print(new_order)
print(favorite_languages)
