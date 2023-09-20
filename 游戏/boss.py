import pygame

class Boss():
	def __init__(self,ai_settings,screen):
		self.screen=screen
		self.ai_settings=ai_settings
		self.image=pygame.image.load('./pictures/boss.bmp')
		self.image=pygame.transform.scale(self.image,(ai_settings.screen_width-100,ai_settings.screen_height//5))
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.y=self.y=float(self.rect.y)
		self.rect.top=self.screen_rect.top
		
	def update(self):
		self.y+=self.ai_settings.boss_speed_factor*self.ai_settings.boss_directiony
		self.rect.y=self.y
			
	def check_edges(self):
		if self.rect.top<=0 and self.ai_settings.boss_directiony==-1:	return 1
		if self.rect.bottom>=self.ai_settings.screen_height//3 and self.ai_settings.boss_directiony==1:	return 2
		
	def blitme(self):
		self.screen.blit(self.image,self.rect)
