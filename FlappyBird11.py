# Flappy Bird Python Code Project for Stanford
# Write your code here :-)
import pygame
import sys
import time
import random

pygame.init()

# Set up game window
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game variables
gravity = 0.5
bird_y = HEIGHT // 2
bird_velocity = 0

# Obstacle variables
obstacle_width = 30
min_obstacle_height = 100
max_obstacle_height = 400
obstacle_speed = 5
gap_height = 200  # Gap height for the bird to pass through

# Background color
background_color = (255, 255, 255)  # White

# Background variables
background_x = 0

# Scoring
score = 0
font = pygame.font.Font(None, 36)

def draw_obstacle(x, top_height, bottom_height):
    pygame.draw.rect(screen, (0, 0, 255), (x, 0, obstacle_width, top_height))
    pygame.draw.rect(screen, (0, 0, 255), (x, HEIGHT - bottom_height, obstacle_width, bottom_height))

def display_score():
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 120, 20))

def main():
    global bird_y, bird_velocity, obstacle_speed, score

    game_over = False
    restart_time = None

    # Initialize obstacle_x
    obstacle_x = WIDTH

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        # Restart the game
                        bird_y = HEIGHT // 2
                        bird_velocity = 0
                        game_over = False
                        restart_time = None
                        score = 0
                    else:
                        bird_velocity -= 10  # Bird jumps

        if not game_over:
            # Update bird position
            bird_velocity += gravity
            bird_y += bird_velocity

            # Generate random obstacle heights
            top_height = random.randint(min_obstacle_height, max_obstacle_height - gap_height)
            bottom_height = HEIGHT - top_height - gap_height

            # Update obstacle position
            obstacle_speed += 0.001  # Increase speed over time
            obstacle_x -= obstacle_speed
            if obstacle_x < -obstacle_width:
                obstacle_x = WIDTH
                score += 3  # Increment score when obstacle passes

            # Check collision
            if bird_y < 0 or bird_y > HEIGHT or (obstacle_x < 100 < obstacle_x + obstacle_width and
                                                 (bird_y < top_height or bird_y > HEIGHT - bottom_height)):
                print("Game Over! Press SPACE to restart.")
                game_over = True
                restart_time = time.time()

            # Draw background
            screen.fill(background_color)

            # Draw bird
            pygame.draw.circle(screen, (255, 0, 0), (100, int(bird_y)), 20)  # Red bird

            # Draw obstacles
            draw_obstacle(obstacle_x, top_height, bottom_height)

            # Display score
            display_score()

            if game_over:
                if restart_time is not None and time.time() - restart_time >= 3:
                    print("Press SPACE to restart.")

        pygame.display.flip()
        pygame.time.Clock().tick(30)  # Frame rate

if __name__ == "__main__":
    main()
