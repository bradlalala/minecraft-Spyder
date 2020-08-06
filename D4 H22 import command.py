from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()


x,y,z = mc.player.getTilePos()

while True:
    mc.executeCommand("kill @a")
    sleep(0.1)

        