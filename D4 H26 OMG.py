# 用2d list建立方塊

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

list2d = [[12, 41, 14],
          [35, 73, 86]]

myID = mc.getPlayerEntityId("bradlalala")
x, y, z = mc.entity.getTilePos(myID)

startX = x

for list1d in list2d:
    for i in list1d:
        mc.setBlock(x, y, z, i)
        x = x + 1
    
    x = startX
    z = z + 1