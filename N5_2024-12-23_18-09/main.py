def func(x11: int, x12: int, x21: int, x22: int) -> bool:
    return x21 <= x11 <= x22 or x11 <= x21 <= x12


def main() -> int:
    x1, y1, w1, h1 = map(int, input().split())
    x2, y2, w2, h2 = map(int, input().split())
    if func(x1, x1 + w1, x2, x2 + w2) and func(y1, y1 + h1, y2, y2 + h2):
        print("YES")
    else:
        print("NO")
    return 0


if __name__ == '__main__':
    main()
