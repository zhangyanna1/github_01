import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,800,550)
#敌机随机出厂事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
		

class GameSprite(pygame.sprite.Sprite):
	'''游戏精灵类'''
	def __init__(self,image_name,speed=1):
		super().__init__()
		#贴图
		self.image = pygame.image.load(image_name)
		#记录尺寸
		self.rect = self.image.get_rect()
		#记录速度
		self.speed = speed
	def update(self,*args):
		#垂直移动
		self.rect.y += self.speed
				

#背景
class Background(GameSprite):
	
	def __init__(self,is_alt=False):
		image_name = './images/背景.png'
		super().__init__(image_name)
		if is_alt:
			self.rect.x = SCREEN_RECT.width
	def update(self):
		self.rect.x -= 2
		
		if self.rect.x <= -SCREEN_RECT.width:
			self.rect.x = SCREEN_RECT.width



#敌机精灵
class Enemy(GameSprite):
	
	def __init__(self):
		#调用父类方法，创建敌机，并加入图像
		super().__init__('./images/enemy.png')
		#　敌机的初始速度是1~3
		self.speed = random.randint(3,5)
		#设置敌机的随机移动速度
		self.rect.bottom = 0
		
		y = SCREEN_RECT.bottom - self.rect.bottom - 60
		self.rect.y = random.randint(0,y)
		self.rect.x = SCREEN_RECT.width

	def update(self):
		self.rect.x -= self.speed
		#让敌机垂直运动
		if self.rect.x <= SCREEN_RECT.left:
			#print('敌机飞出屏幕')
			#删除精灵
			self.kill()

	def __del__(self):
		print('敌机挂了')		


#英雄精灵
class Hero(GameSprite):
	def __init__(self,images_name,x,y):
		super().__init__(images_name,0)
		#设置初始位置
		self.rect.bottom = y
		self.rect.centerx = x
		#创建一个子弹精灵组
		self.bullets = pygame.sprite.Group()
		self.speed1 = 0
	def update(self):
		self.rect.y += self.speed
		self.rect.x += self.speed1
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.bottom > SCREEN_RECT.bottom:
			self.rect.bottom = SCREEN_RECT.bottom
		if self.rect.y < 0:
			self.rect.y = 0
	def fire(self):
		self.bullet = hero_Bullet()
		self.bullet2 = hero_Bullet()
		for i in (1,2,3):
			#创建子弹的位置
			self.bullet.rect.left = self.rect.right - 30
			self.bullet.rect.centery = self.rect.centery -25
			self.bullet2.rect.left = self.rect.right - 30
			self.bullet2.rect.centery = self.rect.centery +25
			self.bullets.add(self.bullet,self.bullet2)

class hero_Bullet(GameSprite):


	def __init__(self):
		super().__init__('./images/ai.png',-3)
	def update(self):
		self.rect.x += 30
	
		#子弹超出屏幕删除
		if self.rect.bottom < 0:
			self.kill()
	


class Fuji(Hero):
	def pos(self,x,y,fuji_if):
		if not fuji_if:
			self.rect.centerx = x -30
			self.rect.centery = y
		else:
			self.rect.centerx = 2000
			self.rect.centery = 2000
			
		
	def fire(self):
		self.bullet = hero_Bullet()
		for i in (1,2,3):
			#创建子弹的位置
			self.bullet.rect.left = self.rect.right - 20
			self.bullet.rect.centery = self.rect.centery
			self.bullets.add(self.bullet)
			

		
	
	

		
 
