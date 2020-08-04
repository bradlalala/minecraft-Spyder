# 放置方塊
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

mc.setSign(x,y,z,63,0,"我愛","Minecraft","","也愛Python")

 