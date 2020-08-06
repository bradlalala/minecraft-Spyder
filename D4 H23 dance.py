# 方塊躲貓貓

from mcpi.minecraft import Minecraft
from random import randrange

mc = Minecraft.create()

for i in range(10):
    x, y, z = mc.player.getTilePos()
    x = x + i
    
    for j in range(10):
        r = randrange(0, 16)
        z = z + 1
        
        mc.setBlock(x, y, z, 35, r)