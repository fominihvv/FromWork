def choose_plural(amount: int, period: int)-> str:
    '���������� ���������. �������� (111, 0) -> 111 ����'
    
    declensions = {0:['����', '���', '����'], 1:['���', '����', '�����'], 2:['������', '������', '�����']}
    if amount % 10 == 1 and amount % 100 not in [11, 12, 13, 14]: return(f'{amount} {declensions[period][0]}')
    elif amount % 10 in [2, 3, 4] and amount % 100 not in [11, 12, 13, 14]: return(f'{amount} {declensions[period][1]}') 
    else: return(f'{amount} {declensions[period][2]}')
