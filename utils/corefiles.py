import json
import os
from typing import Dict, List, Optional
from app.config import JEIEQUIPOS

def readJson(ruta):
    import os
    import json
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def writeJson(ruta, data):
    import json
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def updateJson(data : Dict, path: Optional[List[str]] = None) -> None:
    currentData = readJson()

    if not path:
        currentData.update(data)
    else:
        current = currentData
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)
    
    writeJson(currentData)

def deleteJson(path: List[str])->bool:
    data = readJson()
    if not data:
        return False
    
    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]
    
    if path and path[-1] in current:
        del current[path[-1]]
        writeJson(data)
        return True
    return False

def initializeJson(initialStructure:Dict)->None:
    if not os.path.isfile(JEIEQUIPOS):
        writeJson(initialStructure)
    else:
        currentData = readJson()
        for key, value in initialStructure.items():
            if key not in currentData:
                currentData[key] = value
        writeJson(currentData)