import datetime as dt
import json  # импорт не используется


# много ошибкок связанных с оформлением кода, смотри pep8.
# Укажу на ошибку каждуого типа, только где она встречается первый раз
# не хватает пустых строк между классами и методами
class Record:
    def __init__(self, amount, comment, date=''):
        # между арифмитическими операциями и присваиванием необходимо ставить пробелы
        self.amount=amount
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment=comment
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records=[]
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        today_stats=0
        # Record плохое назваение для переменной,
        # во первыхз нельзя называть переменные с большой буквы(кроме констант)
        # во вторых оно совпадает с именем класса
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats+Record.amount
        return today_stats
    def get_week_stats(self):
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            # можно упростить до выражения if 7 > (today - record.date).days >= 0:
            # проверка на >= 0 не имеет смысла, тк если у нас есть запись в будущем это ошибка,
            # можно добавить проверки при создании записи: record.date <= dt.datetime.now().date()
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                week_stats +=record.amount
        return week_stats
class CaloriesCalculator(Calculator):
    # между кодом и коментарием необходимо 2 проблела если они находятся на одной строке
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        x=self.limit-self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
class CashCalculator(Calculator):
    # float не надежное число, то есть при точных вычислениях могут быть ошибки, лучше использовать decimal.Decimal
    USD_RATE=float(60) #Курс доллар США.
    EURO_RATE=float(70) #Курс Евро.

    # переменные USD_RATE можно было не передавать как параметры метода,
    # а сразу испольтзовать в методе через оператор доступа к классу self
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        if currency=='usd':
            cash_remained /= USD_RATE
            currency_type ='USD'
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            currency_type ='Euro'
        elif currency_type=='rub':
            # опечатка: ==, вместо /= получется сравнение.
            # Также на 1 можно вообще не делить, а оставить число прежним
            cash_remained == 1.00
            currency_type ='руб'
        # здесь не хватает пустой строки, чтобы логически разделить две if конструкции между собой
        if cash_remained > 0:
            # В f-строках не должно быть логических или арифметических операций, вызовов функций и подобной динамики.
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)

    # этот метод можно было не переопределять, тк в него не внесено изменений
    def get_week_stats(self):
        super().get_week_stats()


# нет конструкции if __name__ == ‘__main__’
# не хватает сценария работы кода
