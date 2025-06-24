def insert_soft_hyphens(text, max_length=8):
    if not text or not isinstance(text, str):
        return text
    words = text.split()
    result = []
    for word in words:
        if len(word) > max_length:
            new_word = ""
            for i in range(0, len(word), max_length):
                new_word += word[i:i+max_length] + "\u00AD"
            result.append(new_word.rstrip("\u00AD"))
        else:
            result.append(word)
    return " ".join(result)