import sys
import random
from time import sleep

import pygame

from bullet import Bullet,Special_Bullet
from alien import Alien1,Alien2,Alien3
from missile1 import Missile1_
from missile2 import Missile2_
from missile3 import Missile3_


def ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	if stats.ship_left:
		stats.ship_left-=1
		sleep(0.5)
	else:	stats.game_active=False
	aliens1.empty()
	aliens2.empty()
	aliens3.empty()
	missiles1.empty()
	missiles2.empty()
	missiles3.empty()
	bullets.empty()
	ship.center_ship()
	sb.prep_left()
	sleep(0.5)
	
	
def update_screen(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	sb.show_score()
	for bullet in bullets.sprites():	#sprites()是包含所有精灵对象的列表
		bullet.draw_bullet()
	ship.blitme()
	aliens1.draw(screen)
	aliens2.draw(screen)
	aliens3.draw(screen)
	for missile1 in missiles1.sprites():
		missile1.draw_missile1()
	missiles2.draw(screen)
	missiles3.draw(screen)
	pygame.display.flip()
	

def check_keydown_events(event,ai_settings,screen,ship,bullets,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3):
	if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:	fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_d:	ship.moving_right=True
	elif event.key==pygame.K_a:	ship.moving_left=True
	elif event.key==pygame.K_w:	ship.moving_up=True
	elif event.key==pygame.K_s:	ship.moving_down=True
	elif event.key==pygame.K_c and ai_settings.c_limit:	
		bullets.empty()
		aliens1.empty()
		aliens2.empty()
		aliens3.empty()
		missiles1.empty()
		missiles2.empty()
		missiles3.empty()
		ai_settings.c_limit=False
	elif event.key==pygame.K_e:	fire_special_bullet(ai_settings,screen,ship,bullets)	#E键释放技能
	elif event.key==pygame.K_q:	sys.exit(0)	#按q退出
def check_keyup_events(event,ai_settings,screen,ship,bullets):
	if event.key==pygame.K_d:	ship.moving_right=False
	elif event.key==pygame.K_a:	ship.moving_left=False
	elif event.key==pygame.K_w:	ship.moving_up=False
	elif event.key==pygame.K_s:	ship.moving_down=False
def check_events(ai_settings,screen,ship,bullets,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3):	#响应按键和鼠标事件
	for event in pygame.event.get():
		if event.type==pygame.QUIT:	sys.exit(0)
		elif event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN and event.button==1:	
			check_keydown_events(event,ai_settings,screen,ship,bullets,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3)
		elif event.type==pygame.KEYUP:	check_keyup_events(event,ai_settings,screen,ship,bullets)
		
	
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets)<ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
def fire_special_bullet(ai_settings,screen,ship,bullets):
	if ai_settings.skill_bullet_limit==0:
		new_bullet=Special_Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		ai_settings.skill_bullet_limit=10000
		ai_settings.count1=150
	

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	if ai_settings.count1>0:
		collisions1=pygame.sprite.groupcollide(bullets,aliens1,False,True)
		collisions2=pygame.sprite.groupcollide(bullets,aliens2,False,True)
		collisions3=pygame.sprite.groupcollide(bullets,aliens3,False,True)
		for missile1 in missiles1.copy():
			if pygame.sprite.spritecollideany(missile1,bullets):
				missiles1.remove(missile1)
		for missile2 in missiles2.copy():
			if pygame.sprite.spritecollideany(missile2,bullets):
				missiles2.remove(missile2)
		for missile3 in missiles3.copy():
			if pygame.sprite.spritecollideany(missile3,bullets):
				missiles3.remove(missile3)
	else:
		collisions1=pygame.sprite.groupcollide(bullets,aliens1,True,True)	#一组精灵对象和另一组精灵对象相撞
		collisions2=pygame.sprite.groupcollide(bullets,aliens2,True,True)
		collisions3=pygame.sprite.groupcollide(bullets,aliens3,True,True)
	if collisions1:
		for alien1 in collisions1.values():
			stats.score+=ai_settings.alien1_points*len(alien1)
			sb.prep_score()
	if collisions2:
		for alien2 in collisions2.values():
			stats.score+=ai_settings.alien2_points*len(alien2)
			sb.prep_score()
	if collisions3:
		for alien3 in collisions3.values():
			stats.score+=ai_settings.alien3_points*len(alien3)
			sb.prep_score()	
def update_bullets(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
	
	
def create_alien1(ai_settings,screen,aliens1):
	for _ in range(10):
		alien=Alien1(ai_settings,screen)
		aliens1.add(alien)
def create_alien2(ai_settings,screen,aliens2):
	for _ in range(5):
		alien=Alien2(ai_settings,screen)
		aliens2.add(alien)
def create_alien3(ai_settings,screen,aliens3):
	for _ in range(3):
		alien=Alien3(ai_settings,screen)
		aliens3.add(alien)
		

def check_fleet_edges(ai_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			alien.rect.y+=ai_settings.fleet_drop_speed+random.uniform(-10,10)
			alien.direction*=-1
def update_aliens(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	check_fleet_edges(ai_settings,aliens1)
	check_fleet_edges(ai_settings,aliens2)
	check_fleet_edges(ai_settings,aliens3)
	aliens1.update()
	aliens2.update()
	aliens3.update()
	if pygame.sprite.spritecollideany(ship,aliens1):	#一个精灵对象和一组精灵对象相撞
		ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
	for alien1 in aliens1:
		if alien1.rect.top>=ai_settings.screen_height:	
			ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
	for alien2 in aliens2:
		if alien2.rect.top>=ai_settings.screen_height:	
			ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
	for alien3 in aliens3:
		if alien3.rect.top>=ai_settings.screen_height:	
			ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)


def create_missile1(ai_settings,screen,aliens1,missiles1):
	for alien1 in aliens1:
		if random.randint(1,1000)==1:
			missiles1.add(Missile1_(ai_settings,screen,alien1))
def update_missile1(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	for missile1 in missiles1:
		missile1.update()
		if missile1.check_edges():
			missiles1.remove(missile1)
	if pygame.sprite.spritecollideany(ship,missiles1):
		ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
def create_missile2(ai_settings,screen,aliens2,missiles2):
	for alien2 in aliens2:
		if random.randint(1,2000)==1:
			missiles2.add(Missile2_(ai_settings,screen,alien2))
def update_missile2(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	for missile2 in missiles2:
		missile2.update()
		if missile2.rect.top>=ai_settings.screen_height:
			missiles2.remove(missile2)
	if pygame.sprite.spritecollideany(ship,missiles2):
		ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
def create_missile3(ai_settings,screen,aliens3,missiles3):
	for alien3 in aliens3:
		if random.randint(1,3000)==1:
			missiles3.add(Missile3_(ai_settings,screen,alien3))
def update_missile3(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets):
	for missile3 in missiles3:
		missile3.update()
		if missile3.rect.top>=ai_settings.screen_height:
			missiles3.remove(missile3)
	if pygame.sprite.spritecollideany(ship,missiles3):
		ship_hit(ai_settings,screen,stats,sb,ship,aliens1,aliens2,aliens3,missiles1,missiles2,missiles3,bullets)
