# 放置方塊
"""
Created on Mon Aug  3 10:50:27 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

try:
    block = int(input("請輸入要放ㄉ方塊ID?"))
    mc.setBlock(x,y,z,block)
except:
    mc.postToChat("只能輸入數字!!!!!!!!!!!!!")
 