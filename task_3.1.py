import re

def normalize_phone(phone_number):
  # Remove all characters except numbers 
    normalized_number = re.sub(r'\D', '', phone_number)
  # Trim 10 last digit 
    trimmed_number = normalized_number[-10:]
  # Add international number for Ukraine  
    result = '+38' + trimmed_number

    return result

# Run Function
print(normalize_phone("    +38(050)123-32-34"))            
print(normalize_phone("     0503451234"))         
print(normalize_phone("(050)8889900"))    
print(normalize_phone("38050-111-22-22"))  
print(normalize_phone("38050 111 22 11   "))         
  
# найпростіший варіант вирішення задачі з нормалізації номерів. Але не відповідає Вимогам до завдання
# task_3.2.py відповідає усім вимогам до завдання