#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    items = dir(hidden_4)
    for item in items:
        if not item.startswith("__"):
            print(item)
