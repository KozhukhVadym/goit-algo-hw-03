from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначення дати наступного дня народження
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначення різниці в днях між сьогоднішньою датою та днем народження
        days_until_birthday = (birthday_this_year - today).days

        # Перенесення дати привітання на наступний понеділок, якщо день народження припадає на вихідний
        if days_until_birthday <= 7:
            weekday = birthday_this_year.weekday()
            if weekday == 5:  # Субота
                birthday_this_year += timedelta(days=2)
            elif weekday == 6:  # Неділя
                birthday_this_year += timedelta(days=1)

            # Додавання інформації про користувача та дату привітання у список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Run Function
users = [
    {"name": "John Doe", "birthday": "2024.04.20"},
    {"name": "Jane Smith", "birthday": "2024.04.23"},
    {"name": "Bob Marley", "birthday": "2024.04.27"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)