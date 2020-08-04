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

width =50
heigt =90 
length =25
block =169
air =0

mc.setBlocks(x, y, z, x+width, y+heigt, z+length, block)
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+heigt-1, z+length-1, air)

   



