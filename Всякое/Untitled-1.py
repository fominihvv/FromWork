from requests import *

base_dir = 'https://stepik.org/media/attachments/course67/3.6.3/'

with open('input.txt','r',encoding = 'utf-8') as fi:
    addr = get(fi.read()).text

while addr.split()[0] != 'We':
    addr = get(base_dir+addr).text
    
print(addr)

#resp = get(addr)
#print(len(resp.text.splitlines()))

#with open('input.txt','r',encoding = 'utf-8') as fi:
#    print(len(get(fi.read()).text.splitlines()))
