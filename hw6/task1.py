def to_snake_case(string):
    last = string[0]
    result = []
    for letter in string:
        if letter.isupper() and not last.isupper():
            low_letter = letter.lower()
            res = f"_{low_letter}"
        else:
            res = letter
        result.append(res)
        last = letter
    return "".join(result).lower()


class Pepifize(type):
    def __new__(mcs, name, bases, attrs, ignore, **kwargs):
        new_attrs = {}
        for i in attrs.keys():
            if i not in ignore and callable(attrs[i]):
                new_attrs[to_snake_case(i)] = attrs[i]
            else:
                new_attrs[i] = attrs[i]
        return super().__new__(mcs, name, bases, new_attrs)
