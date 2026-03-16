# NOTE:
# - Deze testklasse is volledig Ai gegeneerd en is bedoeld om de logica van de settings en player modules te testen zonder afhankelijk te zijn van Pygame's display functies, wat problemen kan veroorzaken in een headless testomgeving.
# - Deze testklasse is bedoeld om de logica van de settings en player modules te testen.
# - Pygame functies die afhankelijk zijn van een display kunnen problemen veroorzaken bij het uitvoeren van tests in een headless omgeving. Daarom is de SDL_AUDIODRIVER ingesteld op "dummy" om audiofouten te voorkomen, en pygame.init() wordt alleen aangeroepen in de Player tests waar nodig.
# - De tests richten zich op het genereren van codes, het resetten van de game state, en de initiële eigenschappen van de Player klasse.
# - Om deze tests uit te voeren, zorg ervoor dat de testomgeving correct is ingesteld en dat de benodigde modules beschikbaar zijn.

# Je runned deze file door "python -m unittest test_game.py" in de terminal te typen, zorg ervoor dat je in de juiste directory zit waar deze file zich bevindt.

import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import unittest
import pygame
import settings
from player import Player

class TestSettingsLogic(unittest.TestCase):
    
    def test_generate_code(self):
        """Test of de gegenereerde geheime code voldoet aan de eisen (4 cijfers, 0-9)."""
        code = settings.generate_code()
        
        self.assertEqual(len(code), 4, "De code moet exact 4 cijfers lang zijn.")
        for cijfer in code:
            self.assertGreaterEqual(cijfer, 0, "Cijfer mag niet kleiner dan 0 zijn.")
            self.assertLessEqual(cijfer, 9, "Cijfer mag niet groter dan 9 zijn.")

    def test_reset_game_state_new_code(self):
        """Test de reset functie met het verzoek voor een nieuwe code."""
        # Verander wat settings om te zien of ze gereset worden
        settings.in_room = True
        settings.current_mode = "room"
        settings.code_ingevoerd = [1, 2, 3]
        
        # Voer reset uit
        settings.reset_game_state(new_code=True)
        
        self.assertFalse(settings.in_room, "in_room moet False zijn na reset.")
        self.assertEqual(settings.current_mode, "begin", "current_mode moet 'begin' zijn.")
        self.assertEqual(settings.code_ingevoerd, [], "Ingevoerde code moet leeg zijn.")
        self.assertEqual(len(settings.code), 4, "Er moet een nieuwe 4-cijferige code zijn gegeneerd.")

    def test_reset_game_state_keep_code(self):
        """Test de reset functie waarbij de oude code behouden moet blijven."""
        vaste_code = [5, 5, 5, 5]
        settings.code = vaste_code
        
        settings.reset_game_state(new_code=False)
        
        self.assertEqual(settings.code, vaste_code, "De code moet behouden blijven als new_code False is.")

class TestPlayerLogic(unittest.TestCase):
    
    def setUp(self):
        # Pygame init is nodig voor Rect objecten als ze afhankelijk zijn van display modules, 
        # hoewel Rects meestal ook zonder init werken.
        pygame.init()

    def test_player_initialization(self):
        """Test of de speler start met de juiste coördinaten en hitbox."""
        player = Player(x=100.0, width=50, height=50, speed=150, y=200.0)
        
        self.assertEqual(player.x, 100.0)
        self.assertEqual(player.y, 200.0)
        self.assertEqual(player.speed, 150)
        
        # Test de hitbox generatie
        self.assertEqual(player.player_hitbox.x, 100)
        self.assertEqual(player.player_hitbox.y, 200)
        self.assertEqual(player.player_hitbox.width, 50)
        self.assertEqual(player.player_hitbox.height, 50)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()