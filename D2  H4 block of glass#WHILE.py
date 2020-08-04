# 放置方塊
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

time.sleep(1)

x,y,z = mc.player.getTilePos()

while True:
    color = random.randrange(16)
    mc.setBlocks(x+52, y-1, z+52, x-52, y-1, z-59, 95, color)
    time.sleep(0.5)

   



