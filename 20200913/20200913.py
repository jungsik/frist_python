# print("Snap")

"이스케이프 연습"
print("\tAAA")

"""[2.3.5]복제하기:*
    *연산자를 이용하여 문자열을 복제할 수 있다. 
"""
start = 'Na'*3 + '\n'
end = 'Goodbye'
print(start + end)

letters = 'abcdefg'
print(letters[-3:-1])


# replace
name = 'kim'
name=name.replace('k','m')
print(name)

name='k'+name[1:]
print(name)

#split()

todos = 'kim,jung,sik'
todos=todos.split(',') # 문자열 리스트로 출력한다.['kim', 'jung', 'sik']
print(todos)
todos = ''.join(todos) # 문자열 리스트을 다음과 같이 출력 kimjungsik
print(todos)
