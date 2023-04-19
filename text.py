def delete_text(text):
    i = 0
    arr = []
    while i < len(text):
        if text[i] == '(':
            arr.append('(')
            text = text[:i] + text[i + 1:]
        if text[i] == ')':
            arr.pop()
            text = text[:i] + text[i + 1:]
        if len(arr) != 0:
            text = text[:i] + text[i + 1:]
        else:
            i = i + 1
    return text



