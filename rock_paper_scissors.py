import pygame
import random
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SALMON = (250, 120, 114)
GREY = (194, 197, 204)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
FPS = 30
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

rock_pic = pygame.image.load("data/rock.png")
scissors_pic = pygame.image.load("data/scissors.png")
paper_pic = pygame.image.load("data/paper.png")
win_pic = pygame.image.load("data/win.png")
fail_pic = pygame.image.load("data/fail.png")
tie_pic =  pygame.image.load("data/tie.png")
arm_one_pic = pygame.image.load("data/arm_one.png")
arm_two_pic = pygame.image.load("data/arm_two.png")

rock_pic = pygame.transform.scale(rock_pic, (160, 160))
paper_pic = pygame.transform.scale(paper_pic, (160, 160))
scissors_pic = pygame.transform.scale(scissors_pic, (160, 160))
arm_one_pic = pygame.transform.scale(arm_one_pic, (160, 160))
arm_two_pic = pygame.transform.scale(arm_two_pic, (160, 160))

def draw_structure():
    screen.fill(WHITE)
    screen.blit(rock_pic, (20, 140))
    screen.blit(paper_pic, (220, 240))
    screen.blit(scissors_pic, (420, 340))
    pygame.draw.rect(screen, WHITE, (0, 0, WINDOW_WIDTH, 50))
    header_text = pygame.font.Font(None, 50).render("Rock Paper Scissors", True, BLACK)
    screen.blit(header_text, (WINDOW_WIDTH // 2 - header_text.get_width() // 2, 15))
    instruction = pygame.font.Font(None, 40).render("Choose Your Fighter",True, RED)
    screen.blit(instruction, (WINDOW_WIDTH // 2 - instruction.get_width() // 2, 60))
    pygame.display.update()

draw_structure()

def fail_draw_structure(player_choice, game_status):
    screen.fill(BLACK)
    screen.blit(fail_pic, (220, 80))
    if player_choice == 'rock':
        screen.blit(rock_pic, (220, 240))
    elif player_choice == 'scissors':
        screen.blit(scissors_pic, (220, 240))
    else:
        screen.blit(paper_pic, (220, 240))
    status_text = pygame.font.Font(None, 40).render(game_status, True, WHITE)
    screen.blit(status_text, (WINDOW_WIDTH // 2 - status_text.get_width() // 2, 450))

def win_draw_structure(player_choice, game_status):
    screen.fill(WHITE)
    screen.blit(win_pic, (220, 80))
    if player_choice == 'rock':
        screen.blit(rock_pic, (220, 240))
    elif player_choice == 'scissors':
        screen.blit(scissors_pic, (220, 240))
    else:
        screen.blit(paper_pic, (220, 240))
    screen.blit(arm_one_pic, (60, 240))
    screen.blit(arm_two_pic, (380, 240))
    status_text = pygame.font.Font(None, 40).render(game_status, True, BLACK)
    screen.blit(status_text, (WINDOW_WIDTH // 2 - status_text.get_width() // 2, 450))
   
def tie_draw_structure(game_status):
    screen.fill(GREY)
    screen.blit(tie_pic, (220, 180))
    status_text = pygame.font.Font(None, 40).render(game_status, True, SALMON)
    screen.blit(status_text, (WINDOW_WIDTH // 2 - status_text.get_width() // 2, 450))
    
def handle_click(x, y):
    if x > 20 and x < 180 and y > 140 and y < 300:
        computer_move("rock")
        return
    elif x > 220 and x < 380 and y > 240 and y < 400:
        computer_move("paper")
        return
    elif x > 420 and x < 580 and y > 340 and y < 500:
        computer_move("scissors")
        return
    else:
        return

def computer_move(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    check_winner(player_choice, computer_choice)
    pygame.display.update()

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        game_status = "It's a tie!"
        tie_draw_structure(game_status)
    elif player_choice == "rock":
        if computer_choice == "paper":
            game_status = "You lose! Paper covers rock"
            fail_draw_structure(player_choice, game_status)
        else:
            game_status = "You win! Rock breaks scissors"
            win_draw_structure(player_choice, game_status)
    elif player_choice == "paper":
        if computer_choice == "scissors":
            game_status = "You lose! Scissors cut paper"
            fail_draw_structure(player_choice, game_status)
        else:
            game_status = "You win! Paper covers rock"
            win_draw_structure(player_choice, game_status)
    elif player_choice == "scissors":
        if computer_choice == "rock":
            game_status = "You lose! Rock breaks scissors"
            fail_draw_structure(player_choice, game_status)
        else:
            game_status = "You win! Scissors cut paper"
            win_draw_structure(player_choice, game_status)
    reset_button = pygame.Rect(200, 500, 200, 50)
    pygame.draw.rect(screen, SALMON, reset_button)
    reset_text = pygame.font.Font(None, 30).render("NEW GAME", True, WHITE)
    screen.blit(reset_text, (WINDOW_WIDTH // 2 - reset_text.get_width() // 2, 515))
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            handle_click(mouse_x, mouse_y)
            if mouse_x > 200 and mouse_x < 400 and mouse_y > 500 and mouse_y < 550:
                draw_structure()
    pygame.time.Clock().tick(FPS)