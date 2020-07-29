# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:25:08 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random, time
mc=Minecraft.create()
pos=mc.player.getTilePos()
while True:
    x = pos.x + random.uniform(-20,20)
    y = pos +30
    z = pos.x + random.uniform(-20,20)
    mc.spawn
