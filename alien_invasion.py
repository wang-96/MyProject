import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # 初始化python,设置和屏幕对象
    pygame.init()
    # 实例化类对象
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    # 创建一群外星人
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 根据键盘的输入更新飞船的位置
            ship.update()
            # 根据键盘和鼠标的输入更新未消失子弹的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人群的位置
            gf.update_aliens(aliens, ai_settings, ship, stats, sb, screen, bullets)
        # 每次循环时都重绘屏幕
        # 使用更新后的位置来重绘屏幕
        gf.update_screen(ai_settings, screen, sb, ship, aliens, bullets, play_button, stats)


run_game()
