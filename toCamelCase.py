def to_camel_case(text):
    text = text.replace("_", "-") 
    text = text.split("-")
    for i in range(1,len(text)):
        text[i] = text[i].replace(text[i][0], text[i][0].upper())
    Result = ''.join(text)
    return Result