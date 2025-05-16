import pygame as pg
import random
import numpy as np

MAX_VELOCITY = 3
RADIUS_PERCEPTION = 40

class Boid:
    def __init__ (self,width, height, cohesion=1, separation=1, alignment=1):
        self.position = pg.math.Vector2(random.randint(0, width), random.randint(0, height))
        self.velocity = pg.math.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        self.color = pg.Color(red, green, blue)
        self.width = width
        self.height = height
        self.cohesion_slider = cohesion
        self.separation_slider = separation
        self.alignment_slider = alignment
    
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
    
    def turn_inwards(self, boids):
        v = pg.Vector2(0,0)
        r = 30
        x_min = r
        x_max = self.width - r
        y_min = r
        y_max = self.height -  r
        if self.position.x < x_min:
            v.x = 10
        elif self.position.x > x_max:
            v.x = -10
        if self.position.y < y_min:
            v.y = 10
        elif self.position.y > y_max:
            v.y = -10
        return v
    
    def adjust_cohesion(self, value):
        self.cohesion_slider = value
    
    def adjust_separation(self, value):
        self.separation_slider = value
    
    def adjust_alignment(self, value):
        self.alignment_slider = value

    def update(self, boids, predator):
        c = self.cohesion(boids) * self.cohesion_slider
        s = self.separation(boids) * self.separation_slider
        a = self.alignment(boids) * self.alignment_slider
        t = self.turn_inwards(boids) * random.uniform(0.1, 0.5) # turn inwards with a random factor
        

        # Avoid the predator
        p = pg.Vector2(0, 0)
        distance = self.position.distance_to(predator.position)

        scatter = 1 
        if distance < RADIUS_PERCEPTION:
            scatter = 0 # if the predator is close dont flock
             # if the predator is close, speed up
            if distance < 20:
                # If the predator is very close, move away from it
                p = (self.position - predator.position) * 0.5
            p = (self.position - predator.position) * 0.1
        
        if self.position.x < 12 or self.position.x > self.width - 12 or self.position.y < 12 or self.position.y > self.height - 12:
            scatter = 0

            
        self.velocity +=  (scatter*c) + s + a + p + t
        self.position += self.velocity

        # Limit the velocity to a maximum value
        if self.velocity.length() > MAX_VELOCITY and predator.position.distance_to(self.position) > RADIUS_PERCEPTION -15:
            self.velocity.scale_to_length(MAX_VELOCITY)

        
        # Wrap around the screen edges
        # if self.position.x < 0:
        #     self.position.x = self.width
        # elif self.position.x > self.width:
        #     self.position.x = 0
        # if self.position.y < 0:
        #     self.position.y = self.height
        # elif self.position.y > self.height:
        #     self.position.y = 0


    def draw(self, window):
        center = (self.position.x, self.position.y)
        if self.position.x >= 0 and self.position.y >= 0:
            center = (round(self.position.x), round(self.position.y))
        pg.draw.circle(window, self.color, center, 5)

        
                    
