# 放置方塊
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z = mc.player.getTilePos()


a=0

while a < 20:
    mc.setBlocks(x-40,y-1,z,x+40,y-20,z, 19)
    z = z+5
    a = a+1

