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
a=0

while a<10:
    a=a+1
    time.sleep(2)
    color = random.randrange(8)
    x,y,z = mc.player.getTilePos()
    mc.setBlocks(x, y, z, x, y, z, 38,color)
    
   



