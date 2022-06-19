expanded_a = {
    
}

expanded_b = {

}

def expand_a(order, currentrotation):
    steps_taken = 0
    rotationchange = 0
    xchange = 0
    ychange = 0
    if (order, currentrotation) in expanded_a:
        return expanded_a[(order, currentrotation)]
    if order == 0:
        return 0, 0, 0, 0
    else:
        xchange += expand_a(order-1,(currentrotation + rotationchange) % 4)[0]
        ychange += expand_a(order-1,(currentrotation + rotationchange) % 4)[1]
        rotationchange += expand_a(order-1,(currentrotation + rotationchange) % 4)[2]#Update each var with last a
        steps_taken += expand_a(order-1,(currentrotation) % 4)[3]

        rotationchange += 1 #Turn right

        xchange += expand_b(order-1,(currentrotation + rotationchange) % 4)[0]
        ychange += expand_b(order-1,(currentrotation + rotationchange) % 4)[1]
        rotationchange += expand_b(order-1,(currentrotation + rotationchange) % 4)[2]#Update each var with last b
        steps_taken += expand_b(order-1,(currentrotation) % 4)[3]

        rotationchange = rotationchange % 4 #Cleanup to get in range 0-3
        #Go forward based on current info:
        if (rotationchange + currentrotation) % 4 == 1:
            xchange += 1
        elif (rotationchange + currentrotation) % 4 == 2:
            ychange -= 1
        elif (rotationchange + currentrotation) % 4 == 3:
            xchange -= 1
        else:
            ychange += 1

        steps_taken += 1

        rotationchange += 1 #Turn right
        #No need for extra cleanup of rotation, function already does that
    expanded_a[(order, currentrotation)] = xchange, ychange, rotationchange, steps_taken
    return xchange, ychange, rotationchange, steps_taken

def expand_b(order, currentrotation):
    steps_taken = 0
    rotationchange = 0
    xchange = 0
    ychange = 0
    if (order, currentrotation) in expanded_b:
        return expanded_b[(order, currentrotation)]
    if order == 0:
        return 0, 0, 0, 0
    else:
        rotationchange -= 1 #Turn left

        rotationchange = rotationchange % 4 #Cleanup to get in range 0-3
        #Go forward based on current info:
        if (rotationchange + currentrotation) % 4 == 1:
            xchange += 1
        elif (rotationchange + currentrotation) % 4 == 2:
            ychange -= 1
        elif (rotationchange + currentrotation) % 4 == 3:
            xchange -= 1
        else:
            ychange += 1

        steps_taken += 1

        xchange += expand_a(order-1,(currentrotation + rotationchange) % 4)[0]
        ychange += expand_a(order-1,(currentrotation + rotationchange) % 4)[1]
        rotationchange += expand_a(order-1,(currentrotation + rotationchange) % 4)[2]#Update each var with last a
        steps_taken += expand_a(order-1,(currentrotation) % 4)[3]

        rotationchange -= 1 #Turn left

        xchange += expand_b(order-1,(currentrotation + rotationchange) % 4)[0]
        ychange += expand_b(order-1,(currentrotation + rotationchange) % 4)[1]
        rotationchange += expand_b(order-1,(currentrotation + rotationchange) % 4)[2]#Update each var with last b
        steps_taken += expand_b(order-1,(currentrotation) % 4)[3]

    expanded_b[(order, currentrotation)] = xchange, ychange, rotationchange, steps_taken
    return xchange, ychange, rotationchange, steps_taken


def position_after_order_n(order):
    #move_counter = 0
    
    xcoord, ycoord, rotation, steps = expand_a(order,4)

    return xcoord, ycoord, rotation, steps

print(position_after_order_n(50))

overall_x = position_after_order_n(50)[0]
overall_y = position_after_order_n(50)[1]
overall_rot = position_after_order_n(50)[2]
overall_steps = position_after_order_n(50)[3]
    




def followPath(path):
    target = 10**12
    xpos = 0
    ypos = 0
    rotation = 0
    num_steps = 0
    while len(path) > 0:
        i = path[0]
        path = path[1:]

        if i == "F":
            #Move forward
            if rotation == 0:
                ypos += 1
            elif rotation == 1:
                xpos += 1
            elif rotation == 2:
                ypos -= 1
            else:
                xpos -= 1

            num_steps += 1
            if num_steps == target:
                print("done")
                print(xpos, ypos, rotation, num_steps)
                break

        elif i == "R":
            #Turn right
            if rotation == 3:
                rotation = 0
            else:
                rotation += 1
            
        elif i == "L":
            #Turn left
            if rotation == 0:
                rotation = 3
            else:
                rotation -= 1
            
        elif i == "a":
            if int(path[0]) == 0:
                path.pop(0)
            else:
                order = int(path[0])
                if expand_a(order, rotation)[3] + num_steps < target:
                    xpos += expand_a(order, rotation)[0]
                    ypos += expand_a(order, rotation)[1]
                    rotation += expand_a(order, rotation)[2]
                    num_steps += expand_a(order, rotation)[3]
                    path = path[1:]
                else:
                    print(path)
                    path.insert(1, str(int(path[0]) - 1))
                    path.insert(1, str(int(path[0]) - 1))
                    path.pop(0)
                    path.insert(0,"a")
                    path.insert(2,"R")
                    path.insert(3,"b")
                    path.insert(5,"F")
                    path.insert(6,"R")
                    print(path)
                

        elif i == "b":
            if int(path[0]) == 0:
                path.pop(0)
            else:
                order = int(path[0])
                if expand_b(order, rotation)[3] + num_steps < target:
                    xpos += expand_b(order, rotation)[0]
                    ypos += expand_b(order, rotation)[1]
                    rotation += expand_b(order, rotation)[2]
                    num_steps += expand_b(order, rotation)[3]
                    path = path[1:]
                else:
                    print(path)
                    path.insert(1, str(int(path[0]) - 1))
                    path.insert(1, str(int(path[0]) - 1))
                    path.pop(0)
                    path.insert(0,"L")
                    path.insert(1,"F")
                    path.insert(2,"a")
                    path.insert(4,"L")
                    path.insert(5,"b")
                    print(path)

        rotation = rotation % 4  

        

    return xpos, ypos, rotation, num_steps

listpath = ["F","a","50"]

print(listpath)
print(followPath(listpath))
