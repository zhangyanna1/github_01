class Ditie(object):
	def __init__(self):
		self.month_money = 0.00
		self.count = 2
		self.juli = 0
		self.every_money = 0.00

	def zuo_ditie(self):
		self.count = int(input('请输入坐了几次地铁'))
		self.juli = int(input('请输入距离'))

		for i in range(1,31):

			if self.juli <= 6:
				self.every_money = 1
			elif self.juli > 6 and self.juli <= 12:
				self.every_money = 4
			elif self.juli > 12 and self.juli <= 22:
				self.every_money = 5
			elif self.juli > 22 and self.juli <= 32:
				self.every_money = 6
			elif self.juli < 32:
				self.every_money = (juli-32)//20+6

			if self.month_money >= 100:
				self.every_money = self.every_money*0.8
			elif self.month_money >= 150:
				self.every_money = self.every_money*0.5
			#print(self.month_money)
			
			self.month_money += self.count*self.every_money
	
	def zuo_ditie2(self):
		while True:
			a = int(input('请选择功能1.乘坐　2.计算'))
			if a == 1:
				self.zuo_ditie()
			elif a == 2:
				
				#print('一天坐地铁花了%.2f'%(self.count*self.every_money))
				print('本月坐地铁花了%.2f'%self.month_money)

xiaoming = Ditie()
xiaoming.zuo_ditie2()
