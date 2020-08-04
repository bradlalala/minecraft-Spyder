# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x-1,y,z+1,46)
mc.setBlock(x,y,z+1,46)
mc.setBlock(x+1,y,z+1,46)
mc.setBlock(x+2,y,z,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x-1,y,z-1,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x-1,y,z,46)