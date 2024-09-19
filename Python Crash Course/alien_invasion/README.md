## alien_invasion.py

The main file, alien_invasion.py, contains the AlienInvasion class. This class 
creates a number of important attributes used throughout the game: the 
settings are assigned to settings, the main display surface is assigned to 
screen, and a ship instance is created in this file as well. The main loop of 
the game, a while loop, is also stored in this module. The while loop calls 
_check_events(), ship.update(), and _update_screen(). It also ticks the clock on 
each pass through the loop.

The _check_events() method detects relevant events, such as keypresses 
and releases, and processes each of these types of events through the methods _check_keydown_events() and _check_keyup_events(). For now, these methods 
manage the ship’s movement.


The AlienInvasion class also contains _update
_screen(), which redraws the screen on each pass through the main loop.
The alien_invasion.py file is the only file you need to run when you want 
to play Alien Invasion. The other files, settings.py and ship.py, contain code 
that is imported into this file.

## settings.py

The settings.py file contains the Settings class. This class only has an __init__()
method, which initializes attributes controlling the game’s appearance and 
the ship’s speed.

## ship.py

The ship.py file contains the Ship class. The Ship class has an __init__() method, 
an update() method to manage the ship’s position, and a blitme() method to 
draw the ship to the screen. The image of the ship is stored in ship.bmp, which 
is in the images folder.