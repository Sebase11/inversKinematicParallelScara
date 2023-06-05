import json

file = open('paralell scara\conf.json')
data = json.load(file)

barm = str(input("what is the length of the arms nearest to the motors (mm): "))
farm = str(input("what is the length of the arms fuhrtest away from the motors (mm): "))
d = str(input("what is the distance betwen the two motors (mm): "))

data['Frontarm']['length'] = farm
data['Backarm']['length'] = barm
data['distance']['value'] = d

with open('paralell scara\conf.json', 'w') as file:
    json.dump(data, file, indent=4)


print("Setup sucsesfull")