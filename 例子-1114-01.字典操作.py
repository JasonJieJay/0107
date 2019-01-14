#coding=utf-8
dic={'name':'8jie','age':30}
print(dic)
dic['age']=100
print(dic)
dic['name']='big chui'
print(dic)
print('_________________')
dic1={'name':'heygor','QQ':914338492}
print(dic1)
dic1.clear()
print(dic1)
#del dic1['QQ']
#print(dic1)
#del dic1
#print(dic1)
print('_________________')

dic={'name':'rulai','age':800}
print(dic['name'])
print(dic['age'])
print('----')
print(dic.keys())
for i in dic.keys():
	print(i)
print(dic.values())
for i in  dic.values():
	print(i)

for i,j in dic.items():
	print(i,j)

