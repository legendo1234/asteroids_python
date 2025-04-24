import pygame
from constants import *
from circleshape import CircleShape
from shot import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt, shots):
        keys = pygame.key.get_pressed()
        
        # Print timer value for debugging
        print(f"Timer: {self.timer}, dt: {dt}")
        
        # Decrease timer by dt
        if self.timer > 0:
            self.timer -= dt
        
    # Rest of the method...
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            shot = self.shoot()
            shots.add(shot)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Set the timer to the cooldown value
        self.timer = PLAYER_SHOOT_COOLDOWN
        
        # Create a vector pointing in the direction the player is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        
        # Scale it by the shot speed to determine velocity
        velocity = forward * PLAYER_SHOOT_SPEED
        
        # Create a new shot at the player's position
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, velocity)
        
        # Return the shot so it can be added to the shots group
        return shot
