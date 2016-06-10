# STEP 1 - Import
# First, we need to import some code that other people have written to let us connect to Minecraft

#import the minecraft modules
import mcpi.minecraft as minecraft
import mcpi.block as block
#import random so you can create lights in random locations
import random
#import time so we can put delays into our program
import time
  
  
  
  
  
  
# STEP 2 - Connect
# Next, we will connect to Minecraft, by setting up a connection with minecraft.Minecraft.create() and naming it "mc":

mc = minecraft.Minecraft.create()

  
  
  
  
# STEP 3 - Test Post
# To test the connection, try posting something to chat, using mc.postToChat("message")





# STEP 4 - Position
# Use mc.player.getTilePos() to find the player's positiona and save it as a variable called "pos"

pos = mc.player.getTilePos()
  
  
  
  
  
  

# STEP 5 - Build The Board
# We want the game to appear just in front of the player's location.
# You can make the game board out of whatever block material you want, google for a full list of names.

mc.setBlocks(pos.x - 1, pos.y, pos.z + 3,
             pos.x + 1, pos.y + 2, pos.z + 3,
             block.STONE.id)








# STEP 6 - Countdown
# The player needs a warning that the game is about to start
# Use the mc.PostToChat("message") from earlier, along with time.sleep(seconds) 

mc.postToChat("Get ready ...")
time.sleep(2)
mc.postToChat("Go")







# STEP 7 - Set Up Variables
# We need to keep track of a few bits of information, so we will create variables for each of them.
# We need to know how many blocks are currently lit (blocksLit) and what score the player has got (points)

blocksLit = 0
points = 0



#loop until game over (when all the lights are lit)
while blocksLit < 9:

    #sleep for a small amount of time
    time.sleep(0.2)

    #turn off any lights which have been hit
    for hitBlock in mc.events.pollBlockHits():
        #was the block hit glowstone
        if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
            #if it was, turn it back to STONE
            mc.setBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z, block.STONE.id)
            #reduce the number of lights lit
            blocksLit = blocksLit - 1
            #increase the points
            points = points + 1 

    #increase the number of lights lit
    blocksLit = blocksLit + 1
    #create the next light
    lightCreated = False
    while not lightCreated:
        xPos = pos.x + random.randint(-1,1)
        yPos = pos.y + random.randint(0,2)
        zPos = pos.z + 3

        #if the block is already glowstone, return to the top and try again
        # otherwise set it to the 
        if mc.getBlock(xPos, yPos, zPos) == block.STONE.id:
            #set the block to glowstone
            mc.setBlock(xPos, yPos, zPos, block.GLOWSTONE_BLOCK.id)
            lightCreated = True
            #debug
            #print "light created x{} y{} z{}".format(xPos, yPos, zPos)

#display the points scored to the player
mc.postToChat("Game Over - points = " + str(points))


# WHAT NEXT?
# Think about what cool extra features you might want to add to your game. 
# Here are a few ideas:

# The difficulty of the game is set by the waiting before changing another block, currently time.sleep(0.2)
# Inceasing this time will make it easier, decreasing will make it harder.
# Experiment and see what works best for you.

# What if the player gets things wrong and hits the wrong block?
# Can you change the program so that it changes the block to something else?
# This forces the player to think more about what block they are hitting and increases the skill required.

# It is common for video games to start easy and get harder.
# Can you make the game start easier and the more points you score, the harder it gets?

# If you've used Python Functions before, try to rearrange and separate your code so that it all lies in neat functions.
