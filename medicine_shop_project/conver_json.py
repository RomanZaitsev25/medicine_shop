

with open("db_new.json", "wb+") as mydata:  # файл куда перезаписывать данные бд
    with open("db.json", "r") as staff:  # файл откуда брать данные
        mydata.write(staff.read().encode("utf8"))
