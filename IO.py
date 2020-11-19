from obj import Object

def read_obj(file_name):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    Параметры:
    **input_file_lines** — Строки входного файла
    """

    input_file_lines = open(file_name, 'r')
    objects = []
    for line in input_file_lines:
        if len(line.strip()) == 0 or line[0] == '#':
            continue  # пустые строки и строки-комментарии пропускаем
        objects.append(parse_obj_par(line))

    return objects


def parse_obj_par(line):
    obj = Object()
    #print(line.split())
    obj.coords[0] = float(line.split()[0])
    obj.coords[1] = float(line.split()[1])
    obj.vel[0] = float(line.split()[2])
    obj.vel[1] = float(line.split()[3])
    obj.mass = float(line.split()[4])
    obj.rad = float(line.split()[5])
    #obj.color = line.split()[7]

    return obj


def write_obj(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
