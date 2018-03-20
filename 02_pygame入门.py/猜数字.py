import random

class number(object):
	def __init__(self):
		self.score = 0
		self.score_01 = 0

	def count(self):
		
		y = random.randint(0,99)
		print(y)
		self.score = 0 
		self.score_01 += 1

		while True:
			self.score +=1
			x = int(input('请输入一个整数'))
			if x > y and x > y:
				print('你猜的数字过大')
			elif x < y and x < y:
				print('你猜的数字小了')
			elif x == y:
				print('你猜中了')
				break
		print('一共猜了%s次游戏'%self.score)
		print('一共玩了%s局游戏'%self.score_01)				 



	def aa(self):
		self.count()
		try:
			while True:

				a = int(input("请选择继续：１、继续玩耍，任意键、退出: "))

				if a == 1 :
					self.count()
				else:
					print("game over")
					break
		except:
			print("game over")
		

zhangyanna = number()


zhangyanna.aa()
			

