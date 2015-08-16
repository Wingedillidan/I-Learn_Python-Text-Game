import sail

player = sail.Ship()
map = sail.Map("Chimvera", player)
engine = sail.Journey(map)
engine.begin()