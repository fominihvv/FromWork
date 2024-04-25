def choose_plural(amount, declensions):
    selector = {
        amount % 10 == 1: 0,
        amount % 10 in [2, 3, 4]: 1,
        amount % 10 in [0, 5, 6, 7, 8, 9]: 2,
        amount % 100 in range(11, 15) : 2
    }
    print(selector)
    return f'{amount} {declensions[selector[True]]}'

def choose_plural1(amount,declensions):
    if amount % 10 == 1 and amount % 100 not in [11, 12, 13, 14]: return(f'{amount} {declensions[0]}')
    elif amount % 10 in [2, 3, 4] and amount % 100 not in [11, 12, 13, 14]: return(f'{amount} {declensions[1]}') 
    else: return(f'{amount} {declensions[2]}')

print(choose_plural(91, ('пример', 'примера', 'примеров')))