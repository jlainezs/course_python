"""
Write a drawPyramid() function with a height parameter. The top of the pyramid has one
centered hashtag character, and the subsequent rows have two more hashtags than the previous row.
The number of rows matches the height integer. There are no Python assert statements to check
the correctness of your program. Instead, you can visually inspect the output yourself. For example,
calling drawPyramid(8) would output the following:

       #
      ###
     #####
    #######
   #########
  ###########
 #############
###############
"""

def draw_pyramid(height):
    for i in range(height):
        for j in range(height-i-1):
            print(" ", end="")

        for j in range(i*2+1):
            print("#", end="")
        print()

draw_pyramid(3)
draw_pyramid(5)
draw_pyramid(6)
