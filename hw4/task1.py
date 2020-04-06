class Vector:
    def __init__(self, lst):
        self._data = list(lst)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, new_value):
        self._data[key] = new_value

    def __iadd__(self, other):
        if len(self) != len(other):
            raise TypeError(f"incorrect sizes")
        else:
            for i, val in enumerate(other):
                self._data[i] += val
            return self

    def __isub__(self, other):
        if len(self) != len(other):
            raise TypeError(f"incorrect sizes")
        else:
            for i, val in enumerate(other):
                self._data[i] -= val
            return self

    def __add__(self, other):
        if len(self) != len(other):
            raise TypeError(f"incorrect sizes")
        else:
            new_vec = Vector(self._data)
            new_vec += other
            return new_vec

    def __sub__(self, other):
        if len(self) != len(other):
            raise TypeError(f"incorrect sizes")
        else:
            new_vec = Vector(self._data)
            new_vec -= other
            return new_vec

    def __eq__(self, other):
        return self._data == other._data

    def __ne__(self, other):
        return not self == other

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise TypeError(f"incorrect sizes")
            else:
                result = 0
                for i in range(len(self._data)):
                    result += self._data[i] * other._data[i]
                return result
        result = Vector(self._data)
        result *= other
        return result

    def __imul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise TypeError(f"incorrect sizes")
            else:
                result = 0
                for i in range(len(self._data)):
                    result += self._data[i] * other._data[i]
                return result
        for i in range(len(self)):
            self._data[i] *= other
        return self

    def __rmul__(self, num):
        return self * num

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"Vector({str(self._data)})"
