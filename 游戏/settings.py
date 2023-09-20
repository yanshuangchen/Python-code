import pygame
class Settings():	#默认设置
	def __init__(self):
		self.screen_width=1200
		self.screen_height=800
		
		self.ship_speed_factor=1.5
		self.ship_limit=4
		self.punishment=0
		
		self.alien_speed_factor=1
		
		self.fleet_drop_speed=20
		self.fleet_direction=1	#1表示向右移动,-1表示向左移动

		self.bullet_speed_factor=3
		self.bullet_width=3
		self.bullet_height=10
		self.bullet_color=255,165,0
		self.bullets_allowed=2
		self.skill_bullet_speed_factor=5
		self.skill_bullet_width=300
		self.skill_bullet_color=255,0,0
		self.skill_bullet_limit=0
		self.count1=0
		self.c_limit=True
		
		self.boss_speed_factor=0.1
		self.boss_directiony=1	#1表示向下移动,-1表示向上移动
		self.boss_blood=1200
		self.missile1_width=5
		self.missile1_height=20
		self.missile12_speed_factor=1
		self.missile1_color=255,255,255
		self.missile3_speed_factor=0.2
		
		self.round=0

		self.alien1_points=100
		self.alien2_points=200
		self.alien3_points=300
