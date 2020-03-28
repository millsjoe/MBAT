import random



def beginMovement(location, matrix,size):

    foundCell = False
    nearEdge = False
    end = False
    if (location[1] + 1) > size - 1 or (location[1] - 1) < 1 or (location[0] + 1) > size - 1 or (location[0] - 1) < 1:
        nearEdge = True

    if not nearEdge:
        # mark surrounding neighbours 
        neighbourDown = matrix[location[0] + 1][location[1]]
        neighbourUp = matrix[location[0] - 1][location[1]]
        neighbourLeft = matrix[location[0]][location[1] - 1]
        neighbourRight = matrix[location[0]][location[1] + 1]

        # check if found the cell and add it 
        if neighbourDown == 1:
            foundCell = True
            matrix[location[0] + 1][location[1]] = 1
        if neighbourDown == 2:
            end = True

        if neighbourUp == 1:
            foundCell = True
            matrix[location[0] - 1][location[1]] = 1
        if neighbourUp == 2:
            end == True

        if neighbourLeft == 1:
            foundCell = True
            matrix[location[0]][location[1] - 1] = 1
        if neighbourLeft == 2:
            end == True
        
        if neighbourRight == 1:
            foundCell = True
            matrix[location[0]][location[1] + 1] = 1
        if neighbourRight == 2:
            end == True

    # move in a random direction 
    if foundCell == False and end == False:
        random_direction = random.randint(0,3)
        if random_direction == 0:
            location = [location[0] + 1, location[1]]
        elif random_direction == 1:    
            location = [location[0] - 1, location[1]]
        elif random_direction == 2:
            location = [location[0],location[1] - 1]
        elif random_direction == 3:
            location = [location[0], location[1] + 1]

    return (location, foundCell, nearEdge, end)