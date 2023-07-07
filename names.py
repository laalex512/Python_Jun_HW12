class Names:
    '''Дескриптор для проверки текста на функции, переданные кортежем при инициализации'''

    def __init__(self, functions: tuple):
        self.functions = functions

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        is_fit = True
        for i in self.functions:
            if not i(value):
                is_fit = False
                break
        if is_fit:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f"{value} don't fit")

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
