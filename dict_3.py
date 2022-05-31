def count_alphabets_digits(s):
    d={'Digits':0,'Alphabets':0}
    for ch in s:
        if ch.isalpha():
            d['Alphabets']+=1
        elif ch.isdigit():
            d['Digits']+=1
        else:
            pass
    return(d)
d= count_alphabets_digits('James Bond 007')
print(d)
d= count_alphabets_digits('Kholi number 420')
print(d)
