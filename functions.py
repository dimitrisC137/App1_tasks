FILEPATH = "tasks.txt"


def read_txt(filepath=FILEPATH):
    """ Read from the txt file and return a list of the tasks"""
    with open(filepath, 'r') as file_read:
        tasks_read = file_read.readlines()
    return tasks_read


def write_txt(tasks_write, filepath=FILEPATH):
    """ Write or overwrite tasks on the txt file"""
    with open(filepath, 'w') as file_write:
        file_write.writelines(tasks_write)


if __name__ == "__main__":

    print("Hello")

