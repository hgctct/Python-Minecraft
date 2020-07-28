from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
try:
    blockType = int(input("Block Id?"))
    mc.setBlock(x,y,z,blockType)
except:
    print("只能輸入數字!!!!!")
    mc.postToChat("只能輸入數字!!!!!")

