# https://www.codewars.com/kata/52724507b149fa120600031d/train/python


Solution #1

# d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
# 6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
# 11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
# 16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
# 20:'twenty',30:'thirty',40:'forty',50:'fifty',
# 60:'sixty',70:'seventy',80:'eighty',90:'ninety',
# 100:'hundred',1000:'thousand'}
# def number2words(n):
#     """ works for numbers between 0 and 999999 """
#     if 0<=n<=20:return d[n]
#     if 20<n<=99 and n%10:return d[10*(n//10)]+'-'+d[n%10]
#     if 20<n<99:return d[10*(n//10)]
#     if n<1000 and n%100==0:return d[n//100]+' '+d[100]
#     if 100<n<=999:return d[n//100]+' '+d[100]+' '+number2words(n%100)
#     if n%1000==0:return d[n//1000]+' '+d[1000]
#     return number2words(n//1000)+' '+d[1000]+' '+number2words(n%1000)



Solution #2

words = "zero one two three four five six seven eight nine" + \
" ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
" thirty forty fifty sixty seventy eighty ninety"
words = words.split(" ")

def number2words(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    elif n < 1000:
        return number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else '')
    elif n < 1000000:
        return number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else '')
