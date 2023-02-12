from preprocess.preprocess import cleaning
#from persiantools import digits
from persian_tools import digits


Toman_words = ['تومان','تومن','ت','T','t']
Rial_words = ['R','ریال','r']
million_words = ['میلیون', 'ملیون']
Numeric_words = {'هزار' : digits.convert_to_fa('000') , 'میلیون' : digits.convert_to_fa('000000')}

def currency_converter(text,currency):
    """
        text: a text that hopefully contains some amount of money 
        currency: the currency we want to have. for now [rial or toman]

        returns the money in desired currency
    """
    numbers = digits.convert_to_fa('0123456789')
    
    text = cleaning(text)
    tokens = text.split()
    out = ''
    
    nums = '0123456789'
    current = 'Toman' # if there is no indicator in text, we assume its in toman
    for t in Toman_words:
        if t in text.split():
            current = 'Toman'
    for t in Rial_words:
        if t in text.split():
            current = 'Rial'
    
    for txt in text.split():
        # if txt.isdigit():
        if txt[0] in numbers:
            out += txt

    if out[-3:] != str(digits.convert_to_fa('000')):
        if len(out) < 5:
            out += str(digits.convert_to_fa('000'))

    for num_word in million_words:
        if num_word in text: 
            while(len(out)<7):
                out += str(digits.convert_to_fa('000'))

    if "میلیارد" in text:
        while(len(out)<10):
            out += str(digits.convert_to_fa('000'))

    if current != currency:
        if currency == 'Rial':
            out = int(out) * 10
        if currency == 'Toman':
            out = int(out) / 10
            
    return int(digits.convert_to_en(out))
