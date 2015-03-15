def reduce_file_path(path):
    result = []
    for symbol in path.split("/"):
        if symbol != "." and symbol != "" and symbol != "..":
            result.append(symbol)
        if symbol == ".." and result != []:
            result.pop()
    if result == []:
        result.insert(0, "/")
    else:
        result.insert(0, "")
    return "/".join(result)
