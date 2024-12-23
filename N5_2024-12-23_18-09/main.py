def main() -> int:
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return 0


if __name__ == '__main__':
    main()
