# coding: utf-8

from solar_physics import Object 
input_filename = 'input_file'
output_filename = 'statistics'

def read_space_objects_data_from_file(input_file_lines):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    Параметры:

    **input_file_lines** — Строки входного файла
    """
    
    objects = []
    for line in input_file_lines:
        if len(line.strip()) == 0 or line[0] == '#':
            continue  # пустые строки и строки-комментарии пропускаем
        object = Object()
        parse_object_parameters(line, object)
        objects.append(object)


    return objects

def parse_object_parameters(line, obj):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    X_coord Y_coord Velocity_X Velocity_Y Mass Radius Color

    Параметры:

    **line** — строка с описание объекта.
    **obj** — объект.
    """
    
    obj.coords[0] = float(line.split()[1])
    obj.coords[1] = float(line.split()[2])
    obj.vel[0] = float(line.split()[3])
    obj.vel[1] = float(line.split()[4])
    obj.mass = float(line.split()[5])
    obj.rad = float(line.split()[6])
    obj.color = line.split()[7]


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    pass


f = open("file.txt",'r')
file = f.readlines()
result = file[0].split()[1]
objects = read_space_objects_data_from_file(file)

for obj in objects:
    print(obj.mass)
