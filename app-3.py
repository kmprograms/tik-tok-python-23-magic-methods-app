class Message:
    def __init__(self, text: str):
        self.text = text

    def __call__(self, idx_from: int, idx_to: int) -> str:
        return self.text[idx_from: idx_to + 1]

    def __add__(self, other):
        return Message(f'{self.text} {other.text}') if isinstance(other, Message) else Message(self.text)

    def __iadd__(self, other):
        self.text += other.text
        return self

    def __str__(self):
        return self.text

    """
        +	object.__add__(self, other)
        -	object.__sub__(self, other)
        *	object.__mul__(self, other)
        //	object.__floordiv__(self, other)
        /	object.__truediv__(self, other)
        %	object.__mod__(self, other)
        **	object.__pow__(self, other[, modulo])
        <<	object.__lshift__(self, other)
        >>	object.__rshift__(self, other)
        &	object.__and__(self, other)
        ^	object.__xor__(self, other)
        |	object.__or__(self, other)
    """

    """
        +=	object.__iadd__(self, other)
        -=	object.__isub__(self, other)
        *=	object.__imul__(self, other)
        /=	object.__idiv__(self, other)
        //=	object.__ifloordiv__(self, other)
        %=	object.__imod__(self, other)
        **=	object.__ipow__(self, other[, modulo])
        <<=	object.__ilshift__(self, other)
        >>=	object.__irshift__(self, other)
        &=	object.__iand__(self, other)
        ^=	object.__ixor__(self, other)
        |=	object.__ior__(self, other)
    """

    """
        -	object.__neg__(self)
        +	object.__pos__(self)
        abs()	object.__abs__(self)
        ~	object.__invert__(self)
        complex()	object.__complex__(self)
        int()	object.__int__(self)
        long()	object.__long__(self)
        float()	object.__float__(self)
        oct()	object.__oct__(self)
        hex()	object.__hex__(self)
    """


def main() -> None:

    print('---------------------------- (1) ----------------------------')
    m1 = Message('kmprograms')
    print(m1(1, 3))

    print('---------------------------- (2) ----------------------------')
    m2 = Message('python')
    m3 = m1 + m2
    print(m1)
    print(m2)
    print(m3)

    print('---------------------------- (3) ----------------------------')
    m4 = Message('km')
    m5 = Message('programs')
    m4 += m5
    print(m4)
    print(m5)

if __name__ == '__main__':
    main()