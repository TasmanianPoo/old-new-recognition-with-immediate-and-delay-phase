import pygame
import random
import sys


pygame.init()


# constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 40
FPS = 30
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RED = (255,0,0)
#display
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Old/New recognition test")
font = pygame.font.Font(None, FONT_SIZE)


# List of study items (semantically unrelated, generated by chatgpt)
study_items = ["giraffe", "calculator", "umbrella", "piano", "volcano",
    "skateboard", "pineapple", "galaxy", "pencil", "sneaker",
    "clock", "kangaroo", "television", "pyramid", "pizza",
    "sunglasses", "helicopter", "river", "book", "mountain"]

new_items = [    "moon", "sandwich", "computer", "ocean", "guitar",
    "bicycle", "castle", "jacket", "elephant", "cloud",
    "cactus", "dolphin", "keyboard", "pillow", "telescope",
    "lantern", "puzzle", "marshmallow", "firefighter", "charger"]





def display_text(text, y_offset=0, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 + y_offset))

def display_timer(seconds):
    """Function to display the timer countdown in MM:SS format."""
    minutes = seconds // 60
    secs = seconds % 60
    timer_text = f"{minutes:02}:{secs:02}"
    screen.fill(WHITE)
    display_text("Countdown Timer:", -100)
    display_text(timer_text, 50, RED)
    pygame.display.flip()


def run_test_phase(test_items, study_items):
    index = 0
    correct_responses = 0
    response_message = ""

    while index < len(test_items):
        screen.fill(WHITE)
        display_text(test_items[index], -100)
        display_text("Press 'O' for Old, 'N' for New", 200)
        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o:  # Old
                        if test_items[index] in study_items:
                            correct_responses += 1
                            response_message = "."
                        else:
                            response_message = "."
                        waiting_for_input = False
                    elif event.key == pygame.K_n:  # New
                        if test_items[index] not in study_items:
                            correct_responses += 1
                            response_message = "."
                        else:
                            response_message = "."
                        waiting_for_input = False

        screen.fill(WHITE)
        display_text(response_message, -50, GREEN if "Correct!" in response_message else RED)
        pygame.display.flip()
        pygame.time.delay(1000)  # Show response for 1 second #change to 1000 later
        index += 1

    return correct_responses



#main game loop
def main():
    clock = pygame.time.Clock()

    #welcome screen
    screen.fill(WHITE)
    display_text("You are about to do an Old/New recognition test.", -160)
    display_text("20 words will be shown to you one-by-one.", -130)
    display_text("You will then be tasked with recognizing certain words", -100)
    display_text("press any key to proceed", 50)
    pygame.display.flip()

    waiting_to_start = True
    while waiting_to_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting_to_start = False

    screen.fill(WHITE)
    pygame.display.flip()
    pygame.time.delay(1000)


    #study phase

    for items in study_items: #take the range out later
        screen.fill(WHITE)
        display_text(items)
        pygame.display.flip()

        pygame.time.delay(1000)

        #pause
    pygame.time.delay(3000)



    screen.fill(WHITE)
    display_text("You will now do the recognition task.", -160)
    display_text("Press 'O' for words that are old", -130)
    display_text("Press 'N' for words that are new", -100)
    display_text("press any key to proceed", 50)
    pygame.display.flip()

    waiting_to_begin = True
    while waiting_to_begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting_to_begin = False

    screen.fill(WHITE)
    pygame.display.flip()
    pygame.time.delay(1000)

    first_half_new_items = new_items[:10]
    second_half_new_items = new_items[10:]
    first_half_study_items = study_items[:10]
    second_half_study_items = study_items [10:]
    initial_test_items = first_half_study_items + first_half_new_items
    random.shuffle(initial_test_items)
    correct_responses_first = run_test_phase(initial_test_items, study_items)


    #distraction phase
    screen.fill(WHITE)
    pygame.time.delay(1000)
    display_text("You have completed the first test phase", -160)
    display_text("You will now do a distraction phase", -130)
    display_text("For the next 5 minutes, please scroll through TikTok", -100)
    display_text("press any key to proceed", 50)
    pygame.display.flip()

    waiting_to_happen = True
    while waiting_to_happen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting_to_happen = False

    #timer

    countdown_time = 300
    start_ticks = pygame.time.get_ticks()
    while countdown_time > 0:
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        countdown_time = 300 -seconds_passed

        if countdown_time >= 0:
            display_timer(countdown_time)
            clock.tick(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    countdown_time = 0

    screen.fill(WHITE)
    display_text("Time's up! You will now move on to second test phase", -50, RED)
    pygame.display.flip()
    pygame.time.delay(3000)

    second_test_items = second_half_study_items + second_half_new_items
    random.shuffle(second_test_items)
    correct_responses_second = run_test_phase(second_test_items, study_items)

    screen.fill(WHITE)
    display_text(f"Second test finished. You got {correct_responses} out of {len(test_items)} correct.",-50)
    pygame.display.flip()
    pygame.time.delay(5000)


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()




