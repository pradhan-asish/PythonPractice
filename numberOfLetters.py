import pprint
message = 'I am very serious and I am casual as well'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)
