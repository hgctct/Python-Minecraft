from mcpi.minecraft import Minecraft
mc = Minecraft.create()
name = input('your name')
message = input("message")
mc.postToChat("{"+name+"}+message+)