from preprocess.preprocess import cleaning
#from persiantools import digits
from persian_tools import digits


Toman_words = ['تومان','تومن','ت','T','t']
Rial_words = ['R','ریال','r']
million_words = ['میلیون', 'ملیون']
thousand = 'هزار'

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
    
    current = 'Toman' # if there is no indicator in text, we assume its in toman
    for t in Toman_words:
        if t in text.split():
            current = 'Toman'
    for t in Rial_words:
        if t in text.split():
            current = 'Rial'
    
    for txt in tokens:
        # if txt.isdigit():
        if txt[0] in numbers:
            out += txt

    if out[-3:] != str(digits.convert_to_fa('000')) or thousand in tokens:
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


def Size_converter(text):
    """
        text: a text that hopefully contains size

        returns number and letter size
    """
    letters = ["l","xl","xxl","فری","بزرگ", "کوچک" ,"لارج","m","2xl","s","بلند","کوتاه","اسمال","مدیوم","ایکس", "کوچیک"]
    notallowed = ["سایزبندی","بندی","سایز"]
    # TODO year and age as letters not numerically separated
    # TODO 2xl, ... 
    nums = digits.convert_to_fa('0123456789')
    out = {"letter":[],"number":[]}
    text = text.lower()
    tokens = text.split()

    if "سال" in tokens or "ماه" in tokens:
        outs = ''
        for t in tokens:
            if t not in notallowed:
                outs += t + ' '
        out["letter"] = outs

    for i in range(len(tokens)):
        if tokens[i] in letters:
            out["letter"].append(token)
        else:
            if tokens[i][0] in nums:
                if tokens[i] in ["2","3"] and tokens[i+1] in ["xl","ایکس"]:
                    out["letter"].append(tokens[i] + tokens[i+1])
                    i += 1
                else:
                    out["number"].append(digits.convert_from_word(tokens[i]))
    return out
