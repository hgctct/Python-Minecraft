from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)
    #Z+
    if r==1:
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z = z+4
    #Z-
    elif r==2:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z = z-4
    #X-
    elif r==3:
        mc.setBlocks(x,y,z,x-4,y,z,1)
        x = x-4
    #X+
    elif r==4:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = x+4
    #Y+
    elif r==5:
        mc.setBlocks(x,y,z,x,y+4,z,1)
        y = y+4
    #Y-
    else:
        mc.setBlocks(x,y,z,x,y-4,z,1)
        y = y-4
    