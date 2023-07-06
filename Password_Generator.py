import random #słuzy do losowania
import string #uzywamy zeby 'złapać' wszystkie małe i duze litery i znaki specjalne oraz cyfry

def generate_password(min_Length, numbers = True, special_characters = True): #paramerty, które potrzebuje zeby przekazać funckje kiedy ją wywołuje,
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation 

    characters = letters
    if numbers:
        characters += digits #jeśli wartosć numbers jest True to dodamy wszystkie digits oraz dodam je do ciągu liter
    if special_characters: 
        characters += special #jeśli mamy znaki specjalne dodajemy je do naszych znaków co pozwoli nam wybierać spośród nich podczas gernerowania. 

    pwd = '' #przechowujemy tu hasło
    meets_criteria = False  # jeśli ustawimy na True to conajmniej jednen z parametrów w generate_password musi byc True
    has_number = False #zmienna, która powie nam czy mamy w haśle numer
    has_special = False #zmienna, która powie nam czy mamy w haśle znak specjalny

    while not meets_criteria or len(pwd) < min_Length: #petla będzie sie potwarzała dopóki nie będziemy spełniać podanych warunków czyli meets_critera lub długos hasła będzie zbyt krótka
        new_char = random.choice(characters) #random został zaimportowany po to aby móc generwoać losowy 
        pwd += new_char

        if new_char in digits: #jeśi nowy znak istnieje  w  digits = string.digits
            has_number = True
        elif new_char in special: # i czy nowy znak istnieje w  special = string.punctuation
            has_special = True

        meets_criteria = True #uruchamiamy zmienna równą True i próbujemy udowodnic, ze jest False, a jeśli tak jest to ustawiam zmienną na False
        if numbers:
            meets_criteria = has_number #nie wazne czy to bedzie True or False 
        if special_characters: #
            meets_criteria = meets_criteria and has_special #jeśli nie mamy number lub special character to nie spełniamy criteria
    return pwd
    
pwd = generate_password(10)
print(pwd) #---------- hasło z minimalna długoscią 10 znaków zawiera cyfy jak i znaki specjalne #####jeśli dodalibyśmy po przecinku False wtedy mielibyśby tylko okresloną min dłiugoś hasła oraz znaki specjalne,


