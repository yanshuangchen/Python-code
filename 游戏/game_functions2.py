import sys
import random

import pygame

from bullet import Bullet,Special_Bullet
from time import sleep
from missile1 import Missile1
from missile2 import Missile2
from missile3 import Missile3
from laser import Laser

def check_keydown_events(event,ai_settings,screen,ship,bullets,missiles1,missiles2,missiles3,lasers):
	if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:	fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_d:	ship.moving_right=True
	elif event.key==pygame.K_a:	ship.moving_left=True
	elif event.key==pygame.K_w:	ship.moving_up=True
	elif event.key==pygame.K_s:	ship.moving_down=True
	elif event.key==pygame.K_c and ai_settings.c_limit:	
		bullets.empty()
		missiles1.empty()
		missiles2.empty()
		missiles3.empty()
		lasers.empty()
		ai_settings.boss_blood-=0.5
		ai_settings.c_limit=False
	elif event.key==pygame.K_e:	fire_special_bullet(ai_settings,screen,ship,bullets)	#E键释放技能
	elif event.key==pygame.K_q:	sys.exit(0)	#按q退出
def check_keyup_events(event,ai_settings,screen,ship,bullets):
	if event.key==pygame.K_d:	ship.moving_right=False
	elif event.key==pygame.K_a:	ship.moving_left=False
	elif event.key==pygame.K_w:	ship.moving_up=False
	elif event.key==pygame.K_s:	ship.moving_down=False
def check_events(ai_settings,screen,ship,bullets,missiles1,missiles2,missiles3,lasers):	#响应按键和鼠标事件
	for event in pygame.event.get():
		if event.type==pygame.QUIT:	sys.exit(0)
		elif event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN and event.button==1:	
			check_keydown_events(event,ai_settings,screen,ship,bullets,missiles1,missiles2,missiles3,lasers)
		elif event.type==pygame.KEYUP:	check_keyup_events(event,ai_settings,screen,ship,bullets)


def update_screen(ai_settings,stats,screen,ship,boss,blood,bullets,missiles1,missiles2,missiles3,lasers):
	for bullet in bullets.sprites():	#sprites()是包含所有精灵对象的列表
		bullet.draw_bullet()
	for missile1 in missiles1.sprites():
		missile1.draw_missile1()
	missiles2.draw(screen)
	missiles3.draw(screen)
	lasers.draw(screen)
	ship.blitme()
	boss.blitme()
	blood.draw()
	if blood.rect.right<=0:	stats.game_win=False
	pygame.display.flip()
	
	
def ship_hit(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers):
	if stats.ship_left:
		stats.ship_left-=1
		ai_settings.punishment+=2
		sleep(0.5)
	else:	stats.game_active=False
	missiles1.empty()
	missiles2.empty()
	missiles3.empty()
	lasers.empty()
	ship.center_ship()
	sleep(0.5)


def check_boss_edges(ai_settings,boss):
	now=boss.check_edges()
	if now==1:	ai_settings.boss_directiony=1
	elif now==2:	ai_settings.boss_directiony=-1
def update_boss(ai_settings,stats,screen,ship,boss,bullets,missiles1,missiles2,missiles3,lasers):
	check_boss_edges(ai_settings,boss)
	boss.update()
	if pygame.sprite.collide_rect(ship,boss):	#一个精灵对象和另一个精灵对象相撞
		ship_hit(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)


def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
def fire_special_bullet(ai_settings,screen,ship,bullets):
	if ai_settings.skill_bullet_limit==0:
		new_bullet=Special_Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		ai_settings.skill_bullet_limit=10000
		ai_settings.count1=100
def update_bullets(ai_settings,screen,ship,boss,blood,bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	if pygame.sprite.spritecollideany(boss,bullets):	#一个精灵对象和一组精灵对象相撞
		harm=random.randint(0,20)
		if harm==0:	ai_settings.boss_blood-=0.3
		elif harm==1:	ai_settings.boss_blood-=0.2
		else:	ai_settings.boss_blood-=0.1
		blood.update()
		
def check_missiles1_ship_collisions(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers):
	if pygame.sprite.spritecollideany(ship,missiles1):
		ship_hit(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)
def update_missile1(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers):
	missiles1.update()
	for missile1 in missiles1.copy():
		if missile1.rect.top>=ai_settings.screen_height:
			missiles1.remove(missile1)
	check_missiles1_ship_collisions(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)
def create_missile1(ai_settings,screen,boss,missiles1):
	missiles1.add(Missile1(ai_settings,screen,boss))

def check_missiles2_ship_collisions(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers):
	if pygame.sprite.spritecollideany(ship,missiles2):
		ship_hit(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)
def update_missile2(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers):
	missiles2.update()
	for missile2 in missiles2.copy():
		if missile2.rect.top>=ai_settings.screen_height:
			missiles2.remove(missile2)
	check_missiles2_ship_collisions(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)
def create_missile2(ai_settings,screen,boss,missiles2):
	missiles2.add(Missile2(ai_settings,screen,boss))

def check_missiles3_ship_collisions(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers):
	if pygame.sprite.spritecollideany(ship,missiles3):
		ship_hit(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)
def update_missile3(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers):
	missiles3.update()
	for missile3 in missiles3.copy():
		if missile3.rect.top>=ai_settings.screen_height or missile3.rect.right<=0 or missile3.rect.left>=ai_settings.screen_width or missile3.rect.bottom<=0:
			missiles3.remove(missile3)
	check_missiles3_ship_collisions(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)
def create_missile3(ai_settings,screen,boss,missiles3):
	missiles3.add(Missile3(ai_settings,screen,boss))	


def check_bullets_missiles_collision(ai_settings,screen,bullets,missiles1,missiles2,missiles3):
	for missile1 in missiles1.copy():
		if pygame.sprite.spritecollideany(missile1,bullets):
			missiles1.remove(missile1)
	for missile2 in missiles2.copy():
		if pygame.sprite.spritecollideany(missile2,bullets):
			missiles2.remove(missile2)
	for missile3 in missiles3.copy():
		if pygame.sprite.spritecollideany(missile3,bullets):
			missiles3.remove(missile3)


def update_laser(ai_settings,stats,screen,ship,boss,missiles1,missiles2,missiles3,lasers,flag):
	if flag:
		lasers.update()
	else:	lasers.empty()
	if flag<=495 and pygame.sprite.spritecollideany(ship,lasers):
		ship_hit(ai_settings,stats,screen,ship,missiles1,missiles2,missiles3,lasers)
def create_laser(ai_settings,screen,lasers,laser_centerx,boss):
	lasers.add(Laser(ai_settings,screen,laser_centerx,boss))
