from test2 import *

# show_table()

# create_table()
# show_db()
# def delete():
#     table=input("which:")
#     delete_db(db_name=table)
# delete()
def insert_data():
    table=input("table:")
    id=input("student id :")
    name=input("name:")
    stts=input("status answer:")
    ans=input("answer:")
    insert_file(table_name=table,sid=id,nme=name,stts=stts,answer=ans)

# insert_data()
show_all_data("quiz1")