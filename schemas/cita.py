def citaEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "medico":item["medico"],
        "fecha":item["fecha"],
        "hora":item["hora"],
        "confirmacion":item["confirmacion"],
        "codigo":item["codigo"]
    }


def citasEntity(entity) -> list:
    return [citaEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]