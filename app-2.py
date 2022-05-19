class Numbers:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)


def main() -> None:
    n = Numbers([1, 2, 3, 4])
    print(len(n))
    print(2 in n)
    print(12 in n)
    print(12 not in n)


if __name__ == '__main__':
    main()