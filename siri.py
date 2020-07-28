from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
blockType = int(input("OOOOOOOOOOOOOOOOOOWOOOOOOOOOOOOOOOOOOOOOOO"))

mc.setBlocks(x,y,z, blockType)