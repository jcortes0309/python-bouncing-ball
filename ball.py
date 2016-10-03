import pygame
import random

class Ball(object):
    def __init__(self, x, y, ball_color_list):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 15) # Random number provides the speed of the ball when it's initialized
        self.dir_x = 1 # Set direction for x
        self.dir_y = 1 # Set direction for y
        self.radius = random.randint(5, 50) # Provide random size for the balls
        self.ball_color = ball_color_list[random.randint(0, len(ball_color_list) - 1)]

    def update(self, width, height):
        self.x += self.dir_x * self.speed
        self.y += self.dir_y * self.speed
        if self.x + self.radius > width:
            self.dir_x = -1
        if self.y + self.radius > height:
            self.dir_y = -1
        if self.x - self.radius < 0:
            self.dir_x = 1
        if self.y - self.radius < 0:
            self.dir_y = 1

    def render(self, screen):
        pygame.draw.circle(screen, (self.ball_color), (self.x, self.y), self.radius)


def main():
    # declare the size of the canvas
    width = 500
    height = 500
    # declare all colors to be used by the ball and canvas lists
    blue = (97, 159, 182)
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    aqua = (0, 255, 255)
    silver = (192, 192, 192)
    magenta = (255, 0, 255)
    navy = (0, 0, 128)
    # declare the colors to be used in the canvas
    bg_color_list = [
        blue,
        black,
        white
    ]
    random_bg_color = bg_color_list[random.randint(0, len(bg_color_list) - 1)]

    # declare the color to be used by the Ball object
    ball_color_list = [
        red,
        aqua,
        silver,
        magenta,
        navy
    ]


    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    ball_list = {
        Ball(50, 50, ball_color_list),
        Ball(200, 50, ball_color_list),
        Ball(50, 200, ball_color_list),
        Ball(50, 300, ball_color_list),
        Ball(300, 50, ball_color_list)
    }

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        for ball in ball_list:
            ball.update(width, height)

        # fill background color
        screen.fill(random_bg_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        for ball in ball_list:
            ball.render(screen)

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
