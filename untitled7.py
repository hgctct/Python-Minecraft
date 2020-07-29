from mcpi.minecraft import Minecraftmc=Minecraft.create()
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    hits = mc.events.pollBlockHits()
    if len
    x,y,z=hit.pos.x, hit.pos.y, hit.pos.z,