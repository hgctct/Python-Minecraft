
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
message = input("你想要在告示牌上顯示什麼??")
mc.setSign(x,y,z, 63,2,[message])

