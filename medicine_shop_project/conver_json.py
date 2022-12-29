

with open("db_new.json", "wb+") as mydata:
    with open("db.json", "r") as staff:
        mydata.write(staff.read().encode("utf8"))
