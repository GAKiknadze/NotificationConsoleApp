#   Автор: https://vk.com/idoooo3
#   Курсовая работа №8
#   Кодировка UTF-8
#   Перед использованием установите библиотеки "datetime" и "prettytable"
#   Инструкция по "Pretty Table": http://zetcode.com/python/prettytable/
import time
from prettytable import PrettyTable



class Diary:
    def __init__(self,file_name = 'log.txt'):
        self.file_name = file_name
        self.data = self.create_list()
        self.show_data()


    def create_list(self):
        '''
        Создает и заполняет список дел из файла с расписанием.
        :return:
        '''
        with open(self.file_name,'r',encoding='utf-8') as line:
            data = [[i for i in path.split('|')] for path in line.read().split('\n')]
            for l in data:
                try:
                    l[0] = float(l[0])
                except:
                    print('Ошибка чтения файла!!!')
        return data

    def show_data(self):
        '''
        Выводит расписание в консоль из списка "data".
        :return:
        '''
        i = 0
        table = PrettyTable()
        table.field_names = ['ИНДЕКС','ДАТА И ВРЕМЯ','ЗАГОЛОВОК','ОПИСАНИЕ']
        for line in self.data:
            try:
                table.add_row([i, time.asctime(time.localtime(float(line[0]))), line[1], line[2]])
            except:
                pass
            i += 1
        print(table)

    def create_new_record(self):
        '''
        Создает новую запись в ежедневнеке.
        :return:
        '''
        try:
            year = int(input('Введите год: '))
            month = int(input('Введите месяц: '))
            if month < 0 or month > 12:
                raise ValueError
            day = int(input('Введите день: '))
            if day < 1 or day > 31:
                raise ValueError
            hour = int(input('Введите часы: '))
            if hour < 0 or hour > 23:
                raise ValueError
            minute = int(input('Введите минуты: '))
            if minute < 0 or minute > 59:
                raise ValueError
            title = input('Введите заголовок: ')
            if title == '':
                raise ValueError
            description = input('Введите описание: ')
            self.data.append([time.mktime((year, month, day, hour, minute, 0, 0, 0, 0)), title, description])
            self.show_data()
        except ValueError:
            print('Ошибка ввода!!!')

    def sort_by_time(self):
        '''
        Сортирует список по дате и времени.
        :return:
        '''
        self.data.sort(key=lambda y: float(y[0]))

    def upgrade_record(self):
        '''
        Обновляет выбранную в списке запись.
        :return:
        '''
        try:
            choice_1 = int(input('Введите номер строки для изменения: '))
            if choice_1 < 0 and choice_1 > len(self.data):
                raise ValueError
            while True:
                l_data = list(time.struct_time(time.localtime(float(self.data[choice_1][0]))))
                choice_2 = int(input('''
Изменить:
1.\tГод;
2.\tМесяц;
3.\tЧисло;
4.\tЧасы;
5.\tМинуты;
6.\tЗаголовок;
7.\tОписание;
8.\tВыйти.
'''))
                if choice_2 == 1:
                    year = int(input('Введите год: '))
                    if year < 2018 or year > 2118:
                        raise ValueError
                    l_data[0] = year
                elif choice_2 == 2:
                    month = int(input('Введите месяц: '))
                    if month < 0 or month > 12:
                        raise ValueError
                    l_data[1] = month
                elif choice_2 == 3:
                    day = int(input('Введите день: '))
                    if day < 1 or day > 31:
                        raise ValueError
                    l_data[2] = day
                elif choice_2 == 4:
                    hour = int(input('Введите часы: '))
                    if hour < 0 or hour > 23:
                        raise ValueError
                    l_data[3] = hour
                elif choice_2 == 5:
                    minute = int(input('Введите минуты: '))
                    if minute < 0 or minute > 59:
                        raise ValueError
                    l_data[4] = minute
                elif choice_2 == 6:
                    title = input('Введите заголовок: ')
                    if title == '':
                        raise ValueError
                    self.data[choice_1][1] = title
                elif choice_2 == 7:
                    self.data[choice_1][2] = input('Введите описание: ')
                elif choice_2 == 8:
                    break
                else:
                    raise ValueError
                self.data[choice_1][0] = str(time.mktime(tuple(l_data)))
                self.show_data()
        except ValueError:
            print('Ошибка ввода!!!')

    def time_search(self):                                                          #   Реализовать функцию))))
        print('Этот раздел пока пуст))0)')

    def delete_record(self):
        '''
        Удаляет выбранную запись из списка .
        :return:
        '''
        try:
            choice_1 = int(input('Введите номер строки для удаления: '))
            if choice_1 < 0 and choice_1 > len(self.data):
                raise ValueError
            self.data.pop(choice_1)
        except ValueError:
            print('Ошибка!!!')

    def delete_all_records(self):
        '''
        Очищает список.
        :return:
        '''
        self.data = []

    def save_list(self):
        '''
        Сохраняет список в файл.
        :return:
        '''
        try:
            f = open(self.file_name,'w')
            h = int(len(self.data))
            for i in range(h-1):
                f.write('{}|{}|{}\n'.format(self.data[i][0],self.data[i][1],self.data[i][2]))
            f.write('{}|{}|{}'.format(self.data[h-1][0],self.data[h-1][1],self.data[h-1][2]))
            f.close()
        except:
            print('Ошибка записи в файл!!!')

k = Diary()
while True:
    try:
        print('''
Меню:
1.\tВывести список задач
2.\tСоздать новую запись
3.\tИзменить запись
4.\tОтметить как выполненное
5.\tПоиск по дате
6.\tОчистить список дел
7.\tВыход из программы
    ''')
        choice = int(input())
        if choice == 1:
            k.show_data()
        elif choice == 2:
            k.create_new_record()
            k.sort_by_time()
        elif choice == 3:
            k.upgrade_record()
            k.sort_by_time()
        elif choice == 4:
            k.delete_record()
            k.sort_by_time()
        elif choice == 5:
            k.time_search()
        elif choice == 6:
            k.delete_all_records()
        elif choice == 7:
            k.save_list()
            quit()
    except ValueError:
        print('Ошибка ввода!!!')
        continue