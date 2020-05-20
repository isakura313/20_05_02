class Validate:
    @staticmethod
    def validate_name(name):
        # здесь могли быть ваши регулярные выражения
        if name == "X-AF-12":
            print("Вы сын Илона Маска")
        else:
            print("НУ не сын и не сын")
