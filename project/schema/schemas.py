def indiviual_serial(todo):
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "complete": todo["complete"]
    }

def list_serial(todos):
    return [indiviual_serial(todo) for todo in todos]