import re
batRegex = re.compile(r'Bat(Man|Woman|Mobile|Copter)')
bat = batRegex.findall('I am BatMan. Likes ride BatMobile')
print(bat[0])
print(bat[1])
print(bat)
print(len(bat))
b = batRegex.search('I am BatMan. Likes ride BatMobile')
print(b.group(0))
print(b.group(1))
