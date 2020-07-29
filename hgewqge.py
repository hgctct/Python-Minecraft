from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for i  in range(100):
    x,y,z(x+1,y-1,z-1,x+i,y-i,z-i)