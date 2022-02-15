orbitals = [
    {"periods": "1234567", "size": 2, "name": "s"},
    {"periods": "234567", "size": 6, "name": "p"},
    {"periods": "3456", "size": 10, "name": "d"},
    {"periods": "45", "size": 14, "name": "f"},
]

SUPERSCRIPT_TABLE = str.maketrans("1234567890", "¹²³⁴⁵⁶⁷⁸⁹⁰")

def get_orbitals(atomic_number):
    output = ""
    for i in range(1, 8):
        x = min(i, 4)
        y = max(i - 3, 1)
        while x > 0 and y < 7:
            orbital = orbitals[x - 1]
            try:
                orbital["periods"].index(str(y))
            except ValueError:
                pass
            else:
                if not min(atomic_number, orbital["size"]) == 0:
                    output += str(y)
                    output += orbital["name"]
                    output += str(min(atomic_number, orbital["size"])).translate(SUPERSCRIPT_TABLE)
                if atomic_number < orbital["size"]:
                    return output.strip()
                atomic_number -= orbital["size"]
                output += " "
            x -= 1
            y += 1


# For debugging purposes
# from rich.traceback import install
# install(show_locals=True)

if __name__ == "__main__":
    import sys

    print(get_orbitals(int(sys.argv[1])))
