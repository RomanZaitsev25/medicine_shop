path = str(input('Enter path file with format: '))

with open("db_new.json", "wb+") as my_new_data:  # файл куда перезаписывать данные бд
    with open(path, "r") as data:  # файл откуда брать данные
        my_new_data.write(data.read().encode("utf8"))
