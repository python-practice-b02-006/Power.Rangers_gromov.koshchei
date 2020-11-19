A = []


def take_info(file_name):
    global A
    input = open(file_name, 'r')
    A = input.readlines()
    for i in range(len(A)):
        A[i] = (A[i].split())
    input.close()
    return A


def save_info(file_name):
    global A
    input = open(file_name, 'w')
    input.close()
    for i in range(len(A)):
        input = open(file_name, 'a')
        print(*A[i], file=input)
        input.close()
    return A


if __name__ == "__main__":
    print("This module is not for direct call!")