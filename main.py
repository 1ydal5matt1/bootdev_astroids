import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
        
        updatable.update(dt)

        # check if the player collied with an asteroid
        for i in asteroids:
            if player.collides_with(i):
                print("Game over!")
                return

        # check if an asteroid collied with a bullet
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        pygame.Surface.fill(screen,(0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60fps
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
