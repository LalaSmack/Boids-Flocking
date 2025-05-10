import pygame as pg
import random

RADIUS_PERCEPTION = 100
MAX_VELOCITY = 3

class Predator:
    def __init__(self, width, height):
        self.position = pg.Vector2(random.randint(20, width-20), random.randint(20, height-20))
        self.velocity = pg.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize()*2
        self.size = 10
        self.color = (255, 0, 0)  # Red color for the predator
        self.width = width
        self.height = height

    def hunt(self, boids):
        closest_boid = None
        closest_distance = float('inf')
        position = pg.Vector2(0, 0)
        count = 0
        for boid in boids:
            distance = self.position.distance_to(boid.position)
            if distance < RADIUS_PERCEPTION:
                position += (boid.position - self.position)
                count += 1
                if distance < closest_distance:
                    closest_distance = distance
                    closest_boid = boid
                

        if count > 0:
            if closest_boid is not None and closest_distance < 30:
                # If the predator is close to a boid, it will chase it
                position = (closest_boid.position - self.position)
            else:
                # If the predator is not close to any boid, it will move towards the average position of the boids
                position /=  count

        return position*0.1 # move 10% towards the boid
    
    def turn_inwards(self):
        v = pg.Vector2(0,0)
        r = 15
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
    def update(self, boids):
        h = self.hunt(boids)
        t = self.turn_inwards() * random.uniform(0.1, 0.5)
        if t.length() > 0:
            self.velocity += t
        else :
            self.velocity += h 
        self.position += self.velocity

        if self.velocity.length() > MAX_VELOCITY:
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
        pg.draw.rect(window, self.color,(center[0]-self.size//2, center[1]-self.size//2, self.size, self.size),1)

