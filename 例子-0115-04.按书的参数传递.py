#coding=utf-8
def animal(pet1,pet2):
	print(pet1+' wang!'+pet2+' miao')
animal('dog','cat')
animal('cat','dog')

print('-----')
def animal(pet1,pet2):
	print(pet1+' wang!'+pet2+' miao')

animal(pet2='cat',pet1='dog')
print('-------------')

def animal(pet2,pet1='2ha'):
	print(pet1+' wang!'+pet2+' miao')
animal('bosi')
animal('pig','out man')


print('-------------')
def test(x,y,*args):
	print(x,y,args)
test(1,2,'heygor','o8ma')

def test1(x,y,**args):
	print(x,y,args)
test1(1,2,a=9,b=20,c='simida')










