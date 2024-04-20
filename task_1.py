from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert the string in the format 'YYYY-MM-DD' into a datetime object
        input_date = datetime.strptime(date, '%Y-%m-%d')

        # Get current date
        current_date = datetime.now().date()

        # Calculate the difference between the input date and the current one
        shift = current_date - input_date.date()

        # Return the number of days (without time)
        return shift.days
    except ValueError:
        print("Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'.")


# Run function
print(get_days_from_today('2020-01-01')) 
print(get_days_from_today('2024-04-25'))  
print(get_days_from_today('20-04-20')) # Wrong input_date format
