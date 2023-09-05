#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text.isspace():
        for i in range(len(text)):
            if text[i] == " " and (text[i + 1].isupper() or (text[i + 1].islower() and text[i - 1] == ":")) and (text[i - 1] == "." or text[i - 1] == "?" or text[i - 1] == ":"):
                    try:
                            text[i].replace(" ", "")
                    except IndexError:
                            print("Index out of range")
            elif text[i] == "?" or  text[i] == "." or text[i] == ":":
                print(f"{text[i]}\n")
            else:
                    print(text[i], end="")