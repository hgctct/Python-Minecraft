# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:21:20 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
a = 0 
while a<20:
    mc.setBlocks(x-30,y,z,x+30,y-9,z)
    z=z-5
    a = a+1