import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
# We import the sleep() function from the time module in the Python
# standard library, so we can pause the game for a moment when the ship is
# hit
from ship import Ship
from bullet import Bullet
from alien import Alien
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Set the game window in fullscreen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # Set the game window in size of self.settings.screen_width and self.settings.screen_height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics,
        # and create a scoreboard.

        # Create an instance to store game statistics.
        # We make the instance after creating the game window but before defining other game elements, such as the ship
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        # We'll create the group that holds the bullets in __init__():
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # Make the Play button.
        # This code creates an instance of Button with the label Play, but it doesn’t
        # draw the button to the screen
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            # When the game is inactive, we don’t need to update the positions of game elements
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            # Pygame will do its best to make the loop run exactly 60 times per second.
            # And Pygame's clock should help the game run consistently on most systems.
            self.clock.tick(60)

    def _check_events(self):
        """_check_events is a helper method that just used inside the current class。
           And it's indicated by a leading underscore, aka a _ symbol.
        """
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Move the ship to the right when key is pressed.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Stop the ship to the right when key is released.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # We use pygame.mouse.get_pos(),
                # which returns a tuple containing the mouse cursor’s x- and y-coordinates
                # when the mouse button is clicked
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # A keyboard shortcut to end the game when the player presses Q.
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            # Stop the ship moving to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Another helper method to refactor the loop of method run_game."""
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # The bullets.sprites() method returns a list of all sprites in the group
        # bullets
        # We place this loop before
        # the line that draws the ship, so the bullets don’t start out on top of the ship.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Draw the score information.
        self.sb.show_score()
        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rig of old bullet."""
        # Update bullet position.
        # The line self.bullets.update() calls bullets.update() for each bullet we place in the group bullets.
        self.bullets.update()
        # At the moment, the bullets disappear when they reach the top, but only
        # because Pygame can’t draw them above the top of the screen. The bullets
        # actually continue to exist; their y-coordinate values just grow increasingly
        # negative. This is a problem because they continue to consume memory and
        # processing power.
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # Print how many bullets on the screen
        # print(len(self.bullets))
        self._check_bullet_alien_collision()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        # This refactoring will make it easier to add new rows and create and entire fleet.
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            # Print when ship is hit
            print("Ship hit!!!")

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collision(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        # Return a dictionary, keys are bullets and values are lists that hit by bullets
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # If dictionary is not null, which means a bullet has hit one of aliens
        if collisions:
            # Iteration for each list in the dictionary, which means how many aliens have been hit by one bullet
            # and the aliens have been stored in a list
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens) # len(aliens) means the length of the lists
            self.sb.prep_score()
            self.sb.check_high_score()

        # To make a new fleet of aliens appear after a fleet has been destroyed,
        # we first check whether the aliens group is empty. If it is, we make a call
        # to _create_fleet(). We’ll perform this check at the end of _update_bullets(),
        # because that’s where individual aliens are destroyed.
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            # Change the speed of each game element when the last alien is destroyed
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            # We’ll make the cursor reappear once the game ends so the player can
            # click Play again to begin a new game
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # We use the rect method collidepoint() to check whether the point of
        # the mouse click overlaps the region defined by the Play button’s rect
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()



