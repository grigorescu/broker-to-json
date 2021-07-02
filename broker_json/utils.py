# These utilities do NOT need Broker bindings.


def get_index_types(type_name):
    if not ("[" in type_name and "]" in type_name):
        return []

    if type_name.startswith("vector of"):
        return []

    type_name = type_name.replace("['", "[")
    type_name = type_name.replace("']", "]")

    # e.g. table[count,port] of table[foo,bar]
    return type_name.split("[")[1].split("]")[0].replace(", ", ",").split(",")


def get_yield_type(type_name):
    if " of " not in type_name:
        return None
    return type_name.split(" of ", 1)[1]


def get_record_types(type_name):
    if type_name.startswith("record { "):
        type_name = type_name.split(" { ", 1)[1].rsplit(" }", 1)[0]

    data = []

    while type_name:
        type_name = type_name.lstrip(" ")
        field_name, type_name = type_name.split(":", 1)
        field_type = ""

        depth = 0
        i = 0
        for i in range(len(type_name)):
            if type_name[i] == ";" and depth == 0:
                break
            if type_name[i:].startswith("record { "):
                depth += 1
            elif type_name[i] == "}":
                depth -= 1
            field_type += type_name[i]
        type_name = type_name[i + 1 :]

        data.append({"field_name": field_name, "field_type": field_type})

    return data
