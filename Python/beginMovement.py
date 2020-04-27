import random



def beginMovement(location, matrix,size):
    """
    Checks for neighbours to see if close to boundary or diffused. 
    If not will return the new location to walk to.

    param location: Current location of cell
    param matrix:   The environment to use
    param size:     The size of environment (eg 100x100)

    return location:    New location 
    return foundcell:   If it has diffused
    return nearedge:    If too close to boundary
    return end:         Instruction to end this iteration
    """
    
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