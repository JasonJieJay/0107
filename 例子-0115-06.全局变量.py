#coding=utf-8
'''
a=100
print('a的值是',a)

def test01():
	a=20
	print('test01中的a是',a)

def test02():
	print('test02中的a是',a)

test01()
test02()
'''
a=100
print('a的值是',a)

def test1():
	global a
	a=200
	print('test1中修改全局变量a',a)

def test2():
	print('test2中使用全局变量a',a)

test1()
test2()
