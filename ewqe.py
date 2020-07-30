# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:50:08 2020

@author: appedu
"""

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    mc.executeCommand("time add 500")
    time.sleep(0.05)