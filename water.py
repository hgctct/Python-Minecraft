from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x-1,y,z-1,x+1,y,z+1,8)
    time.sleep(10)
     