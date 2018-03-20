import random

class number(object):
	def __init__(self):
		self.score = 0

	def count(self):
		
		y = random.randint(0,99)
		print(y)
		self.score = 0 

		while True:
			self.score +=1
			x = int(input('请输入一个整数'))
			if x > y and x == y:
				print('你猜的数字过大')
			elif x < y and x < y:
				print('你猜的数字小了')
			elif x == y:
				print('你猜中了')
				break
		print('一共玩了%s局游戏'%self.score)				 
		

zhangyanna = number()
zhangyanna.count()
			

