import requests
import json


j = {
    "a1":"ahahahsasdwdqd",
    "a2":"qwvgdknm",
    "an":{
        "b1":"qbwciencwcn",
        "bn":{
            "c1":"whndkenoneowf",
            "c2":"qndqwnoqwxmwoqdmx"
        }
    },
    "d1":"asdadasd",
    "d2":"bcnwiecnoweic",
    "dn":{
        "e1":"asdsadasdad",
        "en":{"f1":"wadwjdmowcm"},
        "gn":{"h1":"adniqwniwecnij"}
    },
    "h1":"djwicknweicwicne"
}

def JsonEach(j:dict):
    re = []
    for i in j:
        if type(j[i]) == str:
            re.append(i)
            re.append(j[i])
        if type(j[i]) == dict:
            re.append(i)
            for ii in JsonEach(j[i]):
                re.append(ii)
    return re



r = requests.get(
    url="http://127.0.0.1:5000/user",
    headers={"Client-TTY":"PythonAPI"},
    params={"guid":"xxxxxxxxxxxx"},
    #data={"user":"yk","pwd":"asdasdasd"},
    #json=j,
    verify=False
)
print(r.status_code)
print(r.text)
