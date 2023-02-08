def getKey(obj: dict):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('either multiple keys or empty dict found')
    else:
        return keys[0]

def getNestedValue(obj: dict, key: str):
    if type(obj) is not dict :
        return None
    if (key in obj.keys()) :
        if type(obj[key]) is dict:
            return getNestedValue(obj[key], getKey(obj[key]))
        else:
            # print(f'obj[getKey(obj)]: {obj[getKey(obj)]}')
            return obj[getKey(obj)]
    else:
        nestedKey = getKey(obj)
        return getNestedValue(obj[nestedKey], key)

if __name__ == '__main__':
    obj = {'x': {'y': {'z': 'a'}}}
    value = getNestedValue(obj, 'x')
    print(value)
