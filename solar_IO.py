from solar_physics import Object

def read_obj(file_name):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    Параметры:
    **input_file_lines** — Строки входного файла
    """

    input_file_lines = (file_name, 'r')
    objects = []
    for line in input_file_lines:
        if len(line.strip()) == 0 or line[0] == '#':
            continue  # пустые строки и строки-комментарии пропускаем
        object = Object()
        parse_obj_par(line, object)
        objects.append(object)

    return objects


def parse_obj_par(line, obj):
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


def write_obj(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
