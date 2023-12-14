# Реалізувати функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.

from collections import defaultdict
from datetime import datetime, date


def get_birthdays_per_week(users):

    birthday_users = defaultdict(list)

    for user in users:

        name = user["name"]
        
        # Конвертуємо до типу date, обрізаємо час
        birthday = user["birthday"].date()  
        today = date.today()
        birthday_this_year = birthday.replace(year=today.year)
        # print(birthday_this_year)

        # Перевіряємо, чи вже минув день народження цього року
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Визначаємо різницю між днем народження та поточним днем, щоб знайти дні народження на тиждень вперед
        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            birthday = birthday_this_year.strftime('%A')
            if birthday in ('Saturday', 'Sunday'):
                birthday_users['Monday'].append(name)
            else:
                birthday_users[birthday].append(name)
            
   
    for key, value in birthday_users.items():
        print(f"{key}: {', '.join(value)}")

    return birthday_users
        

if __name__ == "__main__":

    users = [{"name": "Bill Gates", "birthday": datetime(1955, 12, 18)}, 
                {"name": "Jill Valentine", "birthday": datetime(1955, 12, 15)}, 
                {"name": "Kim Kardashian", "birthday": datetime(1955, 12, 16)},
                {"name": "Jan Koum", "birthday": datetime(1955, 12, 17)},
                {"name": "Alex", "birthday": datetime(1955, 12, 11)},
                {"name": "Maria", "birthday": datetime(1955, 12, 30)}
            ]
    
    get_birthdays_per_week(users)