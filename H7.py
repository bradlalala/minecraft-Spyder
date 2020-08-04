# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,95,2)
mc.setBlock(x,y+1,z,95,3)
mc.setBlock(x,y+2,z,95,4)
mc.setBlock(x,y+3,z,95,5)
mc.setBlock(x,y+4,z,95,6)
mc.setBlock(x,y+5,z,95,7)
mc.setBlock(x,y,z,95,2)
mc.setBlock(x,y+1,z,95,3)
mc.setBlock(x,y+2,z,95,4)
mc.setBlock(x,y+3,z,95,5)
mc.setBlock(x,y+4,z,95,6)
mc.setBlock(x,y+5,z,95,7)
mc.setBlock(x,y+1,z,95,3)
mc.setBlock(x,y+2,z,95,4)
mc.setBlock(x,y+3,z,95,5)
mc.setBlock(x,y+4,z,95,6)
mc.setBlock(x,y+5,z,95,7)
mc.setBlock(x,y+1,z,95,3)
mc.setBlock(x,y+2,z,95,4)
mc.setBlock(x,y+3,z,95,5)
mc.setBlock(x,y+4,z,95,6)
mc.setBlock(x,y+5,z,95,7)
mc.setBlock(x,y+1,z,95,3)
mc.setBlock(x,y+2,z,95,4)
mc.setBlock(x,y+3,z,95,5)
mc.setBlock(x,y+4,z,95,6)
mc.setBlock(x,y+5,z,95,7)