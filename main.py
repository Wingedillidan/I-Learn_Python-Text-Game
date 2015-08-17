import sail, ui

player = sail.Ship()
ui = ui.Controller(player)
engine = sail.Journey("Chimvera", player, ui)
engine.begin()