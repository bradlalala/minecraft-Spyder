# 方塊獵人
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time


mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

for i in range(20):
    mc.setBlocks(x+i,y-1,z+i,x+i+2,y-1,z+i,169)
    time.sleep(1)    