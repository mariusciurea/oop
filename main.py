
class NaturalNumber(int):
    nb_obj = 0
    max_obj = 3

    def __new__(cls, nb):
        # print('obj created!')
        if cls.nb_obj >= cls.max_obj - 1:
            raise ValueError
        cls.nb_obj += 1
        # print(cls.nb_obj)
        print(abs(nb))
        # return super().__new__(cls, abs(nb))


if __name__ == '__main__':
    x = NaturalNumber(-4)
    y = NaturalNumber(-4)
    z = NaturalNumber(-4)

    print(x)