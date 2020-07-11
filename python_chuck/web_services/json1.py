import json
data = '''{
    "name" : "Jan",
    "phone" : {
        "type" : "intl",
        "number" : "0987828211"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
#print(info)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
