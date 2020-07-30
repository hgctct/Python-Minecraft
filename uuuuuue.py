from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
nuber = 1
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,52)
    number = number*2
    mc.postToChat("number of fish is "+str(nuber))
    