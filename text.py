def delete_text(text):
    i = 0
    while i < len(text):
        if text[i] == '(':
            while text[i] != ')':
                text = text[:i] + text[i+1:]
            text = text[:i] + text[i + 1:]
        i = i + 1
    return text

