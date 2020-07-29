from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    hits = mc.events.pollBlockhits()
    if len(hits)>0:
         blockID = mc.getBlock(x,y,z)
         print("gfgggff"+str(46)"ghgjg")
         mc.postToChat("gfgggff"+str(46)"ghgjg")

   
