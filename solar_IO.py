# coding: utf-8

from solar_objects import Object
input_filename = 'file'
output_filename = 'statistics'

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    Параметры:

    **input_filename** — имя входного файла
    """

    #return objects                                                                                                                     
    pass

def parse_object_parameters(line, obj):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    [X_coord,Y_coord] [Velocity_X,Velocity_Y] Mass Radius Color

    Параметры:

    **line** — строка с описание объекта.
    **obj** — объект.
    """
    obj.coords = line.split()[1]
    obj.vel = line.split()[2]
    obj.mass = float(line.split()[3])
    obj.rad = float(line.split()[4])
    obj.color = line.split()[6]
    
    pass


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    pass

if __name__ == "__main__":
    print("This module is not for direct call!")
