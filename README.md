This is a framework for making bots compete against each other in a number of games.

Usage
=====

    python app.py

Then go to http://localhost:8080/ with your webbrowser and run games.

Games
=====

The first game is a classic prisonner's dilema.  New games may be added later.
Games are placed in "Games/" directory.

Bots
====

To create a bot, make a subdirectory in Games/{game_name}/bots/ and follow the instructions in Games/{game_name}/doc/protocol.
See in Games/Prisonnier/bots/ for examples.
