# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    Clock_game = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        
        updatable.update(dt)

        for asteroid_instance in asteroids:
            if player.collides_with(asteroid_instance):
                print("Game over!")
                return

        for shot in shots:
            for asteroid_instance in asteroids:
                if shot.collides_with(asteroid_instance):
                    asteroid_instance.split()
                    shot.kill()
                    break

        for drawable_instance in drawable:
            drawable_instance.draw(screen)



        pygame.display.flip()
        dt = Clock_game.tick(60) / 1000

if __name__ == "__main__":
    main()