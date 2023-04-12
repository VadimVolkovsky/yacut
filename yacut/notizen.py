import random  
import string  



def generate_sting(letter_count=3, digit_count=3): 
    """Генерирурет строку из заданного количества символов""" 
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))
  
    letters_and_digits = list(str1)
    random.shuffle(letters_and_digits)  
    custom_id = ''.join(letters_and_digits)
    return custom_id   


def create_short_link(custom_id=None):
    main_url = 'http://127.0.0.1:5000/'
    if custom_id is None:
        custom_id = generate_sting()
    short_url = main_url + custom_id
    return short_url


a = create_short_link()
print(a)