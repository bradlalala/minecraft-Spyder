# 方塊獵人
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time


mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
time.sleep(5)
mc.spawnEntity(x,y,z, 50)