import json
import zipfile

def is_correct_json(json_str: str)-> bool:
    try:
        json.loads(json_str)
        return True
    except:
        return False

d = None
data = None
with zipfile.ZipFile("data.zip", "r") as z:
    for filename in z.namelist():
        with z.open(filename) as f:
            data = f.read()
            if is_correct_json(data):
                d = json.loads(data.decode("utf-8"))
                print(filename)
                print(d)