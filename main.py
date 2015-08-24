import sail, ui

player = sail.Ship()
ui = ui.Controller(player)
engine = sail.Journey("Chimvera", player, ui)
engine.begin()

# me = sail.Ship()
# test = ui.Controller(me)
# print test.display("HI!\nTHERE!\nWHERE\nARE\nYOU\nFROM?")