import re

def normalize_phone(phone_number):
  # Remove all characters except numbers and symbol '+'
    normalized_number = re.sub(r'[^\d+]', '', phone_number)

    # Якщо рядок починається з '0' додаємо '+38'
    if normalized_number.startswith("0"):
        normalized_number = "+38" + normalized_number[0:]
    
    # Якщо рядок починається з 380
    elif normalized_number.startswith("380"):
        normalized_number = "+" + normalized_number

    return normalized_number

# Run Function
print(normalize_phone("    +38(050)123-32-34"))            
print(normalize_phone("     0503451234"))         
print(normalize_phone("(050)8889900"))    
print(normalize_phone("38050-111-22-22"))  
print(normalize_phone("38050 111 22 11   "))         