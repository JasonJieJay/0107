#coding=utf-8
file=open('/home/heygor/passwd','r')

for i in file:
	print(i)

file.close()

'''
str1='hello simida!!!!'
file=open('/home/heygor/0114/test','w')
file.write(str1)
file.close()
'''
file=open('/home/heygor/0114/test','a')
file.write('\n come on baby!')
file.close()

print('succed')
