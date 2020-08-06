# tree~~~~~~~~~~~~~~~~
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def plantTree(x,y,z):
   mc.setBlocks(x+6,y+3,z+6,x-6,y-6,z-6,18)
   mc.setBlocks(x,y,z,x,y-12,z,17)

x,y,z = mc.player.getTilePos()

for i in range(0,200,20):
    plantTree(x+i, y, z)