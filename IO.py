from obj import Object


def read_obj(file_name):
    input_file_lines = open(file_name, 'r')
    objects = []
    for line in input_file_lines:
        if len(line.strip()) == 0 or line[0] == '#':
            continue  # пустые строки и строки-комментарии пропускаем
        objects.append(parse_obj_par(line))
    return objects


def parse_obj_par(line):
    obj = Object()
    obj.coords[0] = float(line.split()[0])
    obj.coords[1] = float(line.split()[1])
    obj.vel[0] = float(line.split()[2])
    obj.vel[1] = float(line.split()[3])
    obj.mass = float(line.split()[4])
    obj.rad = float(line.split()[5])
    return obj


def write_obj(file_name, space_objects):
    #output_file_lines = open(file_name, 'w')
    '''for obj in space_objects:
        output_file_lines.write(str(obj.coords[0]) + ' ' + str(obj.coords[1]) + ' '
                                + str(obj.vel[0]) + ' ' + str(obj.vel[1]) + ' '
                                + str(obj.mass) + ' ' + str(obj.rad) + '\n')'''
    pass

if __name__ == "__main__":
    print("This module is not for direct call!")
