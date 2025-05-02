import pygame as pg
import random
import numpy as np

MAX_VELOCITY = 4
class Boid:
    def __init__ (self,width, height):
        self.position = pg.Vector2(random.randint(0, width), random.randint(0, height))
        self.velocity = pg.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.angle = random.uniform(0, 360)
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.color = pg.Color(red, green, blue)
        self.width = width
        self.height = height
    
    def cohesion(self, boids):
        v = pg.Vector2(0, 0)
        for boid in boids:
            if boid != self:
                v += boid.position - self.position
        if len(boids) > 1:
            v /= len(boids) - 1
        return (v - self.position) / 8
    
    def separation(self, boids):
        v = pg.Vector2(0, 0)
        for boid in boids:
            if boid != self:
                if self.position.distance_to(boid.position) < 100:
                    v -= self.position - boid.position
        return v
    
    def alignment(self, boids):
        v = pg.Vector2(0, 0)
        for boid in boids:
            if boid != self:
                v += boid.velocity
        if len(boids) > 1:
            v /= len(boids) - 1
        return v * 0.1
    
    def update(self, boids, window):
        self.angle += random.randint(-1, 1)
        c = self.cohesion(boids)
        s = self.separation(boids)
        a = self.alignment(boids)
        self.velocity += c + s + a
        self.position += self.velocity

        if self.velocity.length() > MAX_VELOCITY:
            self.velocity.scale_to_length(MAX_VELOCITY)

        # Wrap around horizontally
        if self.position.x < 0:
            self.position.x = self.width
        elif self.position.x > self.width:
            self.position.x = 0

        # Wrap around vertically
        if self.position.y < 0:
            self.position.y = self.height
        elif self.position.y > self.height:
            self.position.y = 0


        
    
    def draw(self, window):
        center = (self.position.x, self.position.y)
        if self.position.x >= 0 and self.position.y >= 0:
            center = (round(self.position.x), round(self.position.y))
        pg.draw.circle(window, self.color, center, 5)

        
                    
