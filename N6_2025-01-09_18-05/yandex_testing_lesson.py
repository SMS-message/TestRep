class Rectangle:
    def __init__(self, width: int, height: int):
        if not isinstance(width, int):
            raise TypeError(f"Expected int, got {type(width)} instead")
        if not isinstance(height, int):
            raise TypeError(f"Expected int, got {type(height)} instead")
        if width < 0:
            raise ValueError(f"Expected positive number, got {width} instead")
        if height < 0:
            raise ValueError(f"Expected positive number, got {width} instead")
        self.w = width
        self.h = height

    def get_area(self) -> int:
        return self.w * self.h

    def get_perimeter(self) -> int:
        return 2 * (self.w + self.h)


def reverse(s: str):
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s)} instead")
    return s[::-1]


def count_chars(s: str):
    if not isinstance(s, str):
        raise TypeError(f"Expected str, got {type(s)} instead")
    dct = {}
    while s:
        if s[0] not in dct:
            dct[s[0]] = 1
        else:
            dct[s[0]] += 1
        s = s[1:]

    return dct


def is_under_queen_attack(*args, **kwargs) -> bool:
    ...
