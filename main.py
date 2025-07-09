import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x,y)

    field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        # code that makes the x button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen,(0, 0, 0))
        updatable.update(dt)

        # check if the player collied with an asteroid
        for i in asteroids:
            if player.check_collision(i):
                print("Game over!")
                return

        # check if an asteroid collied with a bullet
        for i in asteroids:
            for s in shots:
                if s.check_collision(i):
                    i.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
