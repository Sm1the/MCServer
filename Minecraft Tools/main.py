import mcpi.minecraft as minecraft

world = minecraft.Minecraft.create()




def teleport():
    x, y, z = world .player.getPos()
    world .player.setPos(x+100, y, z+100)

def buildBox():
    stone = 1
    x, y, z = world.player.getPos()
    world.setBlocks(x+1, y+1, z+1, x+5, y+30, z+1000, 1)  
    
def playersId():
    playerIds = list(world.getPlayerEntityIds())
    world.postToChat(playerIds)
           
while True:
    for event in world.events.pollChatPosts():
        if "!help" in event.message:
            world.postToChat('/Coins - open trade list')
            teleport()
        else:
            if "2" in event.message:
                world.postToChat('2')
                buildBox()
            else:
                if "3" in event.message:
                    playersId()

