def pacienteEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "apellidos":item["apellidos"],
        "correo":item["correo"],
        "telefono":item["telefono"]
    }


def pacientesEntity(entity) -> list:
    return [pacienteEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]