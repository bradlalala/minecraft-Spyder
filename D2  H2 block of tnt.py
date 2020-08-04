# 放置方塊
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

time.sleep(1)

x,y,z = mc.player.getTilePos()
mc.setBlocks(x+52, y-1, z+52, x-52, y-1, z-59, 46)