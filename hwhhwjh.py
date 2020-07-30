# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:41:46 2020

@author: appedu
"""
c,y,z = mc.player.getTilePos()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x, hit.pos.y ,hit.pos.z
        mc.createExplosion(x,y,z)

