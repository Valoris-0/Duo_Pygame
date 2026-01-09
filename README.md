# PyGame Final Project

Dit project is een eenvoudige PyGame-applicatie in Python met een **Player**, een **Enemy**, en **achtergrondmuziek**. Bij botsing tussen de speler en de vijand stopt de muziek en sluit het spel. Aan jullie de taak om hier jullie eigen final game van te maken. Je mag natuurlijk ook alles verwijderen en van scratch beginnen, het is jullie project. Ik dacht alleen dat het fijn zou zijn als jullie een voorbeeld hadden met classes.

---

## Uitleg

- **Player** (player.py): Een rechthoek die je kunt besturen met de pijltjestoetsen.  
- **Enemy** (enemy.py): Een vijand die automatisch heen en weer beweegt.  
- **MusicManager** (music.py): Regelt het afspelen van de achtergrondmuziek.  
- **main.py**: Start het spel, maakt het scherm, laadt de vijand, speler en muziek, en checkt of er een botsing is.

Zodra er een botsing plaatsvindt tussen de speler en de vijand, of wanneer je het venster sluit, eindigt het spel. 

> **Opmerking:**
> Door de regel `os.environ["SDL_AUDIODRIVER"] = "dummy"` hoor je in de codespace omgeving geen geluid, maar werkt je code wel. Wil je geluid horen, moet je lokaal werken met een echte audio driver, codespaces kan helaas geen geluid afspelen.

---

## Hoe te starten (Codespaces)

1. **Open** je Codespace.
2. **Open** een terminalvenster in Codespaces.
3. **Voer** het spel uit met:
   ```bash
   python main.py
   ```
4. Er wordt een poort (bijv. 6080) geforward om de desktop in je browser te zien.
- Ga in VS Code/Dev Containers naar het Ports-paneel aan de onderkant van je browser.
- Klik op “Open in Browser” om het virtuele bureaublad te bekijken (het rondje bij forwarded address).
5. In dat virtuele bureaublad zie je het PyGame-venster.
