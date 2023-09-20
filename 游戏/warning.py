import pygame

class Warn():
	def __init__(self,ai_settings,screen,centerx,boss):
		self.boss=boss
		self.ai_settings=ai_settings
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.image=pygame.image.load('./pictures/warning.bmp')
		self.image=pygame.transform.scale(self.image,(100,100))
		self.rect=self.image.get_rect()
		self.rect.centerx=centerx
		self.rect.top=boss.rect.centery
		self.y=float(self.rect.y)
	def update(self):
		self.y=self.boss.rect.centery
		self.rect.y=self.y
	def blitme(self):
		self.screen.blit(self.image,self.rect)
