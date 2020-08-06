# ilon bow
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlocks(x+6,y+3,z+6,x-6,y-6,z-6,1)
mc.setBlocks(x,y,z,x,y-12,z,46)