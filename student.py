import csv

from names import Names


class Student:
    names_functions = (str.istitle, str.isalpha)

    first_name = Names(names_functions)
    second_name = Names(names_functions)
    last_name = Names(names_functions)

    def __init__(self, first_name, second_name, last_name, user_id):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.user_id = user_id

        self.performance = {}
        filename = f'users_data/{user_id}.csv'

        with open(filename, 'r', encoding='utf-8') as f:
            csv_read = csv.reader(f, delimiter=';')
            next(csv_read)
            for line in csv_read:
                if line:
                    self.performance.setdefault(line[0], {
                        'Ratings': [],
                        'TestResults': []
                    })
                    self.performance[line[0]]['Ratings'] = self.text_to_list(line[1])
                    self.performance[line[0]]['TestResults'] = self.text_to_list(line[2])

        print(self.performance)  # для наглядности, не для кода, и не забыл убрать)

    def text_to_list(self, text):
        result_list = []
        for i in text.split(','):
            result_list.append(int(i))
        return result_list

    def avg_ratings(self):
        values = []
        for discipline in self.performance.values():
            for rating in discipline['Ratings']:
                values.append(rating)
        return sum(values) / len(values)

    def avg_tests(self):
        for discipline, value in self.performance.items():
            result_line = f'{discipline}: average result = '
            result_line += str(sum(value['TestResults']) / len(value['TestResults']))
            print(result_line)


if __name__ == '__main__':
    std1 = Student('Ivan', 'Ivanovich', 'Ivanov', '001')
    print(std1.avg_ratings())
    std1.avg_tests()

    std2 = Student('Petr', 'Petrovich', 'Petrov', '002')
    print(std2.avg_ratings())
    std2.avg_tests()

    # std3 = Student('petr', 'Petrovich', 'Petrov', '002') #ValueError: petr don't fit
    # std4 = Student('P22etr', 'Petrovich', 'Petrov', '002') #ValueError: P22etr don't fit
