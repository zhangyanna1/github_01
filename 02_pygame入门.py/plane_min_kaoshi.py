import pygame
from plane_sprites_kaoshi import *
from pygame.font import *

#时间标号
HERO_FIRE_EVENT = pygame.USEREVENT + 1
HERO_BULLET_EVENT = pygame.USEREVENT +2
FJD_BULLET_EVENT = pygame.USEREVENT +2
FJD2_BULLET_EVENT = pygame.USEREVENT +2

#音乐
pygame.mixer.init()
#传入音乐路径
pygame.mixer.music.load('./images/林俊杰 - 醉赤壁.mp3')
#播放音乐
pygame.mixer.music.play()



#飞机大战主文件
class PlaneGame(object):
	def __init__(self):
		self.life = 5
		self.score2 = 0
		self.life1 = 5
		self.score3 = 0		

		self.my_if = False
		self.my_if1 = False
		self.fuji_1 = False
		self.fuji_2 = False

		pygame.init()
		print('游戏初始化')

		#每隔0.5秒发射一次子弹	
		pygame.time.set_timer(HERO_FIRE_EVENT,800)

		#辅机自动发子弹
		pygame.time.set_timer(FJD_BULLET_EVENT,1000)
		pygame.time.set_timer(FJD2_BULLET_EVENT,1000)

		#定时器,每秒创造一个飞机
		pygame.time.set_timer(CREATE_ENEMY_EVENT,500)

		#创建游戏窗口
		self.screen = pygame.display.set_mode((SCREEN_RECT.size))
		#创建时钟,控制针率
		self.clock = pygame.time.Clock()
		#创精灵和精灵组
		self.__create_sprites()



	def __create_sprites(self):
		'''精灵组'''
		#背景组
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
		#敌机组
		self.enemy_group = pygame.sprite.Group()

		#我方英雄组
		self.hero = Hero('./images/hero1.png',650,150)
		self.hero2 = Hero('./images/hero2.png',650,260)
		self.hero_group = pygame.sprite.Group(self.hero,self.hero2)
		#辅机组
		self.fuji = Fuji('./images/wwww.png',0,0)
		self.fuji2 = Fuji('./images/wwww.png',0,0)
		self.fuji_group = pygame.sprite.Group(self.fuji,self.fuji2)		

	def strart_game(self):
		print('开始游戏')
		while True:
			#刷新频率
			self.clock.tick(60)
			pygame.display.set_caption('~美少女战士~')
			#事件的监听
			self.__even_hand()
			#碰撞检测
			self.__check_collide()
			#更新精灵组
			self.__update_sprites()
			#更新屏幕显示
			pygame.display.update()


	def __even_hand(self):
		'''事件的监听'''
		for even in pygame.event.get():
			if even.type == pygame.QUIT:
				self.__game_over(self)
			elif even.type == CREATE_ENEMY_EVENT:
				print('敌机出场....')
				self.enemy_group.add(Enemy())

			#获取按键飞机的上下左右	
			keys_pressed = pygame.key.get_pressed()
			
			if keys_pressed[pygame.K_RIGHT]:
				self.hero.speed1 = 6
			elif keys_pressed[pygame.K_LEFT]:
				self.hero.speed1 = -6
			
			elif keys_pressed[pygame.K_UP]:
				self.hero.speed = -6	
			elif keys_pressed[pygame.K_DOWN]:
				self.hero.speed = 6
			else:
				self.hero.speed1 = 0 
				self.hero.speed = 0 
			#自动发弹
			if even.type == HERO_BULLET_EVENT and not self.my_if:
				self.hero.fire()

			elif keys_pressed[pygame.K_d]:
				self.hero2.speed1 = 6
			elif keys_pressed[pygame.K_a]:
				self.hero2.speed1 = -6

			elif keys_pressed[pygame.K_w]:
				self.hero2.speed = -6	
			elif keys_pressed[pygame.K_s]:
				self.hero2.speed = 6
			else:
				self.hero2.speed1 = 0 
				self.hero2.speed = 0 
			#按空格发子弹
			if keys_pressed[pygame.K_SPACE] and not self.my_if1:
				self.hero2.fire()

			#辅机自动发子弹
			if even.type == FJD_BULLET_EVENT:
				self.fuji.fire()
			if even.type == FJD2_BULLET_EVENT:
				self.fuji2.fire()


	def __check_collide(self):
		'''碰撞检测'''
		
		fuji_if = pygame.sprite.spritecollide(self.fuji,self.enemy_group,True)
		fuji_if2 = pygame.sprite.spritecollide(self.fuji2,self.enemy_group,True)

		fuji_bullets = pygame.sprite.groupcollide(self.fuji.bullets,self.enemy_group,True,True)
		fuji2_bullets = pygame.sprite.groupcollide(self.fuji2.bullets,self.enemy_group,True,True)

		enemy_if1 = pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
		enemy_if2 = pygame.sprite.groupcollide(self.hero2.bullets,self.enemy_group,True,True)


		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		enemies1 = pygame.sprite.spritecollide(self.hero2,self.enemy_group,True)

		if len(fuji_bullets):
			self.score2 +=1
		if len(fuji2_bullets):
			self.score2 +=1


		
		if len(fuji_if):
			self.fuji.kill()
			self.fuji_1 = True
			self.fuji.rect.x = 2500
			self.fuji.rect.y = 2500
			
		if len(fuji_if2):
			self.fuji2.kill() 
			self.fuji_2 = True
			self.fuji2.rect.y = 2500
			self.fuji2.rect.x = 2500
		


		if len(enemy_if1):
			self.score2 +=1
		if len(enemy_if2):
			self.score3 +=1


		if len(enemies) > 0:
			self.life -=1
			if self.life < 1:
				self.hero.kill()
				self.hero.rect.x = 2500
				self.hero.rect.y = 2500
				self.fuji.kill()
				self.fuji2.kill()
				print('英雄死亡')
				self.my_if = True
				self.fuji_1 = True
				self.fuji_2 = True



		if len(enemies1) > 0:
			self.life1 -=1
			if self.life1 < 1:
				self.hero2.kill()
				self.hero2.rect.x = 2500
				self.hero2.rect.y = 2500
				print('英雄死亡')
				self.my_if1 = True

		if self.my_if and self.my_if1:
			self.__game_over(self)
			
			 
		

	def __update_sprites(self):
		'''更新精灵组'''
		#更新敌机组，背景组，英雄组

		for a in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullets,self.hero2.bullets,self.fuji_group,self.fuji.bullets,self.fuji2.bullets]:
			if self.my_if1 and a == self.hero2.bullets:
				continue
			elif self.my_if and a == self.hero.bullets:
				continue
			elif self.fuji_1 and a == self.fuji.bullets:
				continue
			elif self.fuji_2 and a == self.fuji2.bullets:
				continue
			else:
				
				a.update()
				a.draw(self.screen)	

		self.fuji.pos(self.hero.rect.x,self.hero.rect.y - 30,self.fuji_1)
		self.fuji2.pos(self.hero.rect.x ,self.hero.rect.bottom +30,self.fuji_2)
		self.show_life()
	@staticmethod
	def __game_over(self):
		print('游戏结束')
		exit()
		pygame.quit()

	def show_life(self):
		pygame.font.init()
		pos1 = (0,0)
		pos2 = (0,30)
		pos3 = (400,0)
		pos4 = (400,30)
		color = (225,0,225)
		text1 = 'LIFE:' + str(self.life)
		text2 = 'SCORE:'+ str(self.score2)
		text3 = 'LIFE1:' + str(self.life1)
		text4 = 'SCORE1:' + str(self.score3)
		cur_font = pygame.font.SysFont("楷体",40)
		text_fmt1 = cur_font.render(text1,1,color)
		text_fmt2 = cur_font.render(text2,1,color)
		text_fmt3 = cur_font.render(text3,1,color)
		text_fmt4 = cur_font.render(text4,1,color)
		self.screen.blit(text_fmt1,pos1)
		self.screen.blit(text_fmt2,pos2)
		self.screen.blit(text_fmt3,pos3)
		self.screen.blit(text_fmt4,pos4)





game = PlaneGame()
game.strart_game()
