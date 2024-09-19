# Because Scoreboard writes text to the screen, we begin by importing the
# pygame.font module
import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information."""
    # Next, we give __init__() the ai_game parameter so it can
    # access the settings, screen, and stats objects, which it will need to report the
    # values we’re tracking
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        # We assign the game instance to an attribute, because we’ll need it to
        # create some ships
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images
        # To turn the text to be displayed into an image, we call prep_score()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        # In prep_score(), we turn the numerical value stats.score into a string 1
        # and then pass this string to render(), which creates the image
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # We’ll position the score in the upper-right corner of the screen and
        # have it expand to the left as the score increases and the width of the number grows.
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        # The prep_ships() method creates an empty group, self.ships, to hold
        # the ship instances
        self.ships = Group()
        #  To fill this group, a loop runs once for every ship the
        # player has left
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            # Inside the loop, we create a new ship and set each ship’s
            # x-coordinate value so the ships appear next to each other with a 10-pixel
            # margin on the left side of the group of ships
            ship.rect.x = 10 + ship_number * ship.rect.width
            # We set the y-coordinate
            # value 10 pixels down from the top of the screen so the ships appear in the
            # upper-left corner of the screen
            ship.rect.y = 10
            # Then we add each new ship to the group ships
            self.ships.add(ship)


