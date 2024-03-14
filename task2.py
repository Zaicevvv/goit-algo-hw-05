from re import findall

def generator_numbers(text):
    if type(text) != str:
        return []
    nums = findall(r'\t?\d+\.\d+\t?', text)
    if not nums:
        return []
    for num in nums:
        yield float(num.strip())

def sum_profit(text, func):
    total = 0
    for num in func(text):
        total += num
    return total

text = 'qwe 10.36 fgh rrty к 3.11 кенн кен 4.86 jhgf hg hgf qwe 3.2 qwe qwe 11.8'

print(sum_profit(text, generator_numbers))