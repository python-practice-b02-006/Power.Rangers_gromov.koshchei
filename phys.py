G = 6.67430*10**(-11)


def calculate_force(space_objects):
    '''Calculate force that move all objects in space objects.  
                              
    Parameters:
        
    **space_objects** - list of space objects.
    '''
    local = space_objects
    for i, body in enumerate(local):
        body.force[0] = 0
        body.force[1] = 0
        for j, body1 in enumerate(local):
            if j != i:
                r = ((body1.coords[0] - body.coords[0]) ** 2 + (body1.coords[1] - body.coords[1]) ** 2) ** 0.5
                body.force[0] += (body1.coords[0] - body.coords[0]) * G * body.mass * body1.mass / (r ** 3)
                body.force[1] += (body1.coords[1] - body.coords[1]) * G * body.mass * body1.mass / (r ** 3)

    return local


if __name__ == "__main__":
    print("This module is not for direct call!")
