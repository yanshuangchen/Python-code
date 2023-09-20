import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		self.screen=screen
		self.ai_settings=ai_settings
		self.image=pygame.image.load('./pictures/ship.bmp')
		self.image=pygame.transform.scale(self.image,(25,50))
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.center=float(self.rect.centerx)
		self.rect.bottom=self.screen_rect.bottom
		
		#self.speed_delta=0.1  # 设置速度变化量
        #self.current_speed=self.ai_settings.ship_speed_factor  # 记录当前速度
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=False
		
	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.rect.centerx+=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:	
			self.rect.centerx-=self.ai_settings.ship_speed_factor+0.5
		if self.moving_up and self.rect.bottom>50:
			self.rect.bottom-=self.ai_settings.ship_speed_factor+0.5
		if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
			self.rect.bottom+=self.ai_settings.ship_speed_factor
			
	def center_ship(self):
		self.center=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)
