class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    #     def __add__(self, other):
    #         if not isinstance(other, Clock):
    #             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #         return Clock(self.sec + other.sec)
    #
    #     def __eq__(self, other):
    #         if not isinstance(other, Clock):
    #             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #         return self.sec == other.sec
    #
    # c1 = Clock(100)
    # c2 = Clock(200)
    #
    # if c1 == c2:
    #     print("Время равно")
    # else:
    #     print("Время разное")
    #
    # c3 = c1 + c2
    # print(c1.get_format_time())
    # print(c2.get_format_time())
    # print(c3.get_format_time())

    #     def __sub__(self, other):
    #       if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #       return Clock(self.sec - other.sec)
    #
    #
    #     def __eq__(self, other):
    #      if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #      return self.sec == other.sec
    #
    #
    # c1 = Clock(500)
    # c2 = Clock(200)
    #
    # if c1 == c2:
    #     print("Время равно")
    # else:
    #     print("Время разное")
    #
    # c3 = c1 - c2
    # print(c1.get_format_time())
    # print(c2.get_format_time())
    # print(c3.get_format_time())

    #     def __mul__(self, other):
    #       if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #       return Clock(self.sec * other.sec)
    #
    #
    #     def __eq__(self, other):
    #      if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом данных Clock")
    #      return self.sec == other.sec
    #
    #
    # c1 = Clock(500)
    # c2 = Clock(200)
    #
    # if c1 == c2:
    #     print("Время равно")
    # else:
    #     print("Время разное")
    #
    # c3 = c1 * c2
    # print(c1.get_format_time())
    # print(c2.get_format_time())
    # print(c3.get_format_time())

#     def __floordiv__(self, other):
#           if not isinstance(other, Clock):
#                 raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#           return Clock(self.sec // other.sec)
#
#     def __eq__(self, other):
#          if not isinstance(other, Clock):
#              raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#          return self.sec == other.sec
#
#
# c1 = Clock(500)
# c2 = Clock(2000)
#
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
#
# c3 = c2 // c1
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())


    def __mod__(self, other):
          if not isinstance(other, Clock):
                raise ArithmeticError("Правый операнд должен быть типом данных Clock")
          return Clock(self.sec % other.sec)

    def __eq__(self, other):
         if not isinstance(other, Clock):
             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
         return self.sec == other.sec


c1 = Clock(500)
c2 = Clock(2000)

if c1 == c2:
    print("Время равно")
else:
    print("Время разное")

c3 = c2 % c1
print(c1.get_format_time())
print(c2.get_format_time())
print(c3.get_format_time())

