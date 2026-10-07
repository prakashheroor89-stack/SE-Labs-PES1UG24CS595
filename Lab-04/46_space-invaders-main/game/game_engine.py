import pygame
import random
from .player import Player
from .enemy import EnemyGrid
from .bullet import Bullet

# Game Engine

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (220, 60, 60)
YELLOW = (240, 220, 80)

# Difficulty settings: enemy movement speed and enemy firing chance per frame.
DIFFICULTIES = {
    "Easy":   {"speed": 0.05, "fire_chance": 0.004},
    "Medium": {"speed": 1.0, "fire_chance": 0.05},   # original game values
    "Hard":   {"speed": 2.0, "fire_chance": 0.02},
}

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 64, bold=True)

        self.reset("Medium")

    def reset(self, difficulty):
        """Start a fresh game with the chosen difficulty."""
        settings = DIFFICULTIES[difficulty]
        self.difficulty = difficulty

        self.player = Player(self.width // 2 - 20, self.height - 50, 40, 20)
        self.enemy_grid = EnemyGrid(self.width, speed=settings["speed"])

        self.player_bullets = []
        self.enemy_bullets = []
        self._shoot_cooldown = 0
        self.enemy_fire_chance = settings["fire_chance"]

        self.score = 0
        self.game_over = False

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        # Game Over menu: choose difficulty or exit
        if self.game_over:
            if event.key == pygame.K_1:
                self.reset("Easy")
            elif event.key == pygame.K_2:
                self.reset("Medium")
            elif event.key == pygame.K_3:
                self.reset("Hard")
            elif event.key == pygame.K_4:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            return

        if event.key == pygame.K_SPACE:
            if self._shoot_cooldown <= 0:
                bullet_x = self.player.center_x() - 2
                self.player_bullets.append(Bullet(bullet_x, self.player.y, direction=-1))
                self._shoot_cooldown = 15

    def handle_input(self):
        if self.game_over:
            return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.move(-self.player.speed, self.width)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move(self.player.speed, self.width)

    def update(self):
        if self.game_over:
            return

        if self._shoot_cooldown > 0:
            self._shoot_cooldown -= 1

        self.enemy_grid.move()

        for enemy in self.enemy_grid.alive_enemies():
            if random.random() < self.enemy_fire_chance:
                bullet_x = enemy.x + enemy.width // 2
                self.enemy_bullets.append(Bullet(bullet_x, enemy.y + enemy.height, direction=1))

        for bullet in self.player_bullets:
            bullet.move()
        for bullet in self.enemy_bullets:
            bullet.move()

        self.player_bullets = [b for b in self.player_bullets if not b.off_screen(self.height)]
        self.enemy_bullets = [b for b in self.enemy_bullets if not b.off_screen(self.height)]

        # Collision: player bullets vs enemies.
        # Build a new list of surviving bullets instead of removing from
        # self.player_bullets while iterating over it (which skipped bullets).
        # Each bullet destroys at most one enemy, and each enemy can only be
        # destroyed (and scored) once.
        alive_enemies = self.enemy_grid.alive_enemies()
        remaining_bullets = []
        for bullet in self.player_bullets:
            bullet_rect = bullet.rect()
            hit = False
            for enemy in alive_enemies:
                if enemy.alive and bullet_rect.colliderect(enemy.rect()):
                    enemy.alive = False
                    self.score += 1
                    hit = True
                    break  # one bullet -> at most one enemy
            if not hit:
                remaining_bullets.append(bullet)
        self.player_bullets = remaining_bullets

        for bullet in self.enemy_bullets:
            if bullet.rect().colliderect(self.player.rect()):
                self.game_over = True
                break

        if self.enemy_grid.reached_bottom(self.player.y):
            self.game_over = True

    def render(self, screen):
        pygame.draw.rect(screen, GREEN, self.player.rect())

        for enemy in self.enemy_grid.alive_enemies():
            pygame.draw.rect(screen, WHITE, enemy.rect())

        for bullet in self.player_bullets:
            pygame.draw.rect(screen, WHITE, bullet.rect())
        for bullet in self.enemy_bullets:
            pygame.draw.rect(screen, RED, bullet.rect())

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if self.game_over:
            self._render_game_over(screen)

    def _render_game_over(self, screen):
        # Dim the frozen game behind the menu
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        def draw_centered(text, font, color, y):
            surf = font.render(text, True, color)
            rect = surf.get_rect(center=(self.width // 2, y))
            screen.blit(surf, rect)

        draw_centered("GAME OVER", self.title_font, RED, 200)
        draw_centered(f"Final Score: {self.score}", self.font, WHITE, 280)
        draw_centered("Play again - choose difficulty:", self.font, YELLOW, 360)
        draw_centered("1 - Easy", self.font, WHITE, 410)
        draw_centered("2 - Medium", self.font, WHITE, 450)
        draw_centered("3 - Hard", self.font, WHITE, 490)
        draw_centered("4 - Exit", self.font, WHITE, 530)