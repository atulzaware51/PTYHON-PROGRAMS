import arcade
import math
import random

# --- Constants ---
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Shooter"

PLAYER_SCALE = 0.3
PLAYER_SPEED = 5
PLAYER_SHOOT_COOLDOWN = 0.2

BULLET_SPEED = 10
BULLET_SCALE = 0.8

ENEMY_SPAWN_RATE = 1.0  # Seconds between spawns
ENEMY_SPEED_MIN = 1
ENEMY_SPEED_MAX = 3
ENEMY_SCALE = 0.3

class Enemy:
    def __init__(self, target_x, target_y):
        # Choose a random starting side
        side = random.choice(("top", "right", "bottom", "left"))
        if side == "top":
            self.x = random.uniform(0, SCREEN_WIDTH)
            self.y = SCREEN_HEIGHT + 20
        elif side == "right":
            self.x = SCREEN_WIDTH + 20
            self.y = random.uniform(0, SCREEN_HEIGHT)
        elif side == "bottom":
            self.x = random.uniform(0, SCREEN_WIDTH)
            self.y = -20
        else:
            self.x = -20
            self.y = random.uniform(0, SCREEN_HEIGHT)

        # Calculate angle to point toward the player's current position
        dest_x = target_x - self.x
        dest_y = target_y - self.y
        self.angle = math.atan2(dest_y, dest_x)
        
        self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
        self.radius = 15  # Collision radius

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.RED)

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = BULLET_SPEED
        self.radius = 4 * BULLET_SCALE

    def update(self):
        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y += math.sin(math.radians(self.angle)) * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.YELLOW)

    def is_off_screen(self):
        return (self.x < -50 or self.x > SCREEN_WIDTH + 50 or 
                self.y < -50 or self.y > SCREEN_HEIGHT + 50)

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT // 2
        self.player_angle = 0
        self.player_radius = 15  # Effective collision radius
        
        self.bullets = []
        self.enemies = []
        self.keys_pressed = set()
        
        self.shoot_cooldown = 0
        self.enemy_spawn_timer = 0
        self.score = 0
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        
        if self.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 
                             arcade.color.WHITE, 54, anchor_x="center")
            arcade.draw_text(f"Final Score: {self.score}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60, 
                             arcade.color.WHITE, 24, anchor_x="center")
            return

        # Draw Player (Triangle)
        arcade.draw_triangle_filled(
            self.player_x + math.cos(math.radians(self.player_angle)) * self.player_radius * 2,
            self.player_y + math.sin(math.radians(self.player_angle)) * self.player_radius * 2,
            self.player_x + math.cos(math.radians(self.player_angle + 140)) * self.player_radius,
            self.player_y + math.sin(math.radians(self.player_angle + 140)) * self.player_radius,
            self.player_x + math.cos(math.radians(self.player_angle - 140)) * self.player_radius,
            self.player_y + math.sin(math.radians(self.player_angle - 140)) * self.player_radius,
            arcade.color.CYAN
        )

        for bullet in self.bullets:
            bullet.draw()
            
        for enemy in self.enemies:
            enemy.draw()

        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)

    def on_update(self, delta_time):
        if self.game_over:
            return

        # Player Movement
        if arcade.key.W in self.keys_pressed: self.player_y += PLAYER_SPEED
        if arcade.key.S in self.keys_pressed: self.player_y -= PLAYER_SPEED
        if arcade.key.A in self.keys_pressed: self.player_x -= PLAYER_SPEED
        if arcade.key.D in self.keys_pressed: self.player_x += PLAYER_SPEED

        # Keep player on screen
        self.player_x = max(self.player_radius, min(SCREEN_WIDTH - self.player_radius, self.player_x))
        self.player_y = max(self.player_radius, min(SCREEN_HEIGHT - self.player_radius, self.player_y))

        # Shooting
        self.shoot_cooldown -= delta_time
        if arcade.key.SPACE in self.keys_pressed:
            self.shoot()

        # Update Bullets
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

        # Spawn Enemies
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer >= ENEMY_SPAWN_RATE:
            self.enemies.append(Enemy(self.player_x, self.player_y))
            self.enemy_spawn_timer = 0

        # Update Enemies & Collisions
        for enemy in self.enemies[:]:
            enemy.update()
            
            # Collision: Enemy vs Player
            dist_to_player = math.sqrt((enemy.x - self.player_x)**2 + (enemy.y - self.player_y)**2)
            if dist_to_player < (enemy.radius + self.player_radius):
                self.game_over = True

            # Collision: Enemy vs Bullets
            for bullet in self.bullets[:]:
                dist_to_bullet = math.sqrt((enemy.x - bullet.x)**2 + (enemy.y - bullet.y)**2)
                if dist_to_bullet < (enemy.radius + bullet.radius):
                    if enemy in self.enemies: self.enemies.remove(enemy)
                    if bullet in self.bullets: self.bullets.remove(bullet)
                    self.score += 10
                    break

    def shoot(self):
        if self.shoot_cooldown <= 0:
            # Bullet spawns at the "nose" of the triangle
            bullet_x = self.player_x + math.cos(math.radians(self.player_angle)) * self.player_radius
            bullet_y = self.player_y + math.sin(math.radians(self.player_angle)) * self.player_radius
            self.bullets.append(Bullet(bullet_x, bullet_y, self.player_angle))
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def on_mouse_motion(self, x, y, dx, dy):
        diff_x = x - self.player_x
        diff_y = y - self.player_y
        self.player_angle = math.degrees(math.atan2(diff_y, diff_x))

def main():
    GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()