import string
class PhoneNumber:
    def __init__(self, number):
        self.number = self.reformat(number)
        self.area_code = self.get_code(self.number)

    def reformat(self, number):
        number = ''.join(dgt for dgt in number if dgt in string.digits)
        if number[0] == '1':
            number = number[1::]
        if int(number[0]) < 2 or len(number) != 10:
            raise ValueError
        return number

    def get_code(self, number):
        code = number[:3:]
        return code

    # def pretty(self):
    #     if len(self) > 10 and len(self) == 11:
    #         self = self[]