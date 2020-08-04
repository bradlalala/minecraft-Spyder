# 放置方塊
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(1)



while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlocks(x, y, z, x, y, z, 38)
    time.sleep(0.2)

   



