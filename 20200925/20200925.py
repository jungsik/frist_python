lot = [('a','b'),('c','d')]
a = dict(lot)
print(a)

pythons ={
    'a':1,
    'b':2,
    'c':2,    
}
print(pythons['a'])

pythons['a']=1000000000

print(pythons)

# del pythons['a']
# print(pythons)

# pythons.clear()

# print(pythons)

print('a' in pythons)

print(pythons.get('n','Not a pythos'))