import pygame as pg
import random
import numpy as np

MAX_VELOCITY = 3
RADIUS_PERCEPTION = 40

class Boid:
    def __init__ (self,width, height):
        self.position = pg.math.Vector2(random.randint(0, width), random.randint(0, height))
        self.velocity = pg.math.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.color = pg.Color(red, green, blue)
        self.width = width
        self.height = height
    
    def cohesion(self, boids):
        v = pg.Vector2(0, 0)
        count = 0 #keeping track of how many boids are in the perception radius 
        for boid in boids:
            if boid != self and self.position.distance_to(boid.position) < RADIUS_PERCEPTION:
                v += boid.position
                count += 1
        if count > 0:
            v /= count
            v -= self.position
        return v*0.01 # move 1% towards the center of the boids in the perception radius
                      # this avoids the boids from moving too fast towards the center of the flock

    def separation(self, boids):
        v = pg.Vector2(0, 0)
        for boid in boids:
            d = self.position.distance_to(boid.position)
            if boid != self and d < RADIUS_PERCEPTION//3:
                    v -= (boid.position - self.position)/d # move away from the boid
                                                           # move away faster if the boid is closer
        return v 
    
    def alignment(self, boids):
        v = pg.Vector2(0, 0)
        count = 0 #``
        for boid in boids:
            if boid != self and self.position.distance_to(boid.position) < RADIUS_PERCEPTION:
                v += boid.velocity
                count += 1
        if count > 0:
            v /= count #average the velocity of the boids in the perception radius
        return v
        
    
    def update(self, boids):
        c = self.cohesion(boids)
        s = self.separation(boids)
        a = self.alignment(boids)
        self.velocity +=  c + s + a 
        self.position += self.velocity

        if self.velocity.length() > MAX_VELOCITY:
            self.velocity.scale_to_length(MAX_VELOCITY)
        
        # Wrap around the screen edges
        if self.position.x < 0:
            self.position.x = self.width
        elif self.position.x > self.width:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = self.height
        elif self.position.y > self.height:
            self.position.y = 0


    def draw(self, window):
        center = (self.position.x, self.position.y)
        if self.position.x >= 0 and self.position.y >= 0:
            center = (round(self.position.x), round(self.position.y))
        pg.draw.circle(window, self.color, center, 5)

        
                    
