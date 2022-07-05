def JumpCounts(x,y,n,height):
    """
    :param x: jump height
    :param y: slides down
    :param n: no of walls
    :param height: height of each wall
    :return: no of jumps to escape
    """
    jumps=0

    for i in range(n):
        if (height[i] <= x): #height of wall is less than or equal to jump
            jumps +=1
            continue
        # h= height[i]
        while (height[i] > x): #while height of wall is greater than jump
            jumps +=1 #jump++
            height[i] = height[i]- (x-y) #updating height after each jump
        jumps +=1
    return  jumps

x=5
y=1
height= [10,9]
n= len(height) #calculating no. of walls
print(JumpCounts(x,y,n,height))
