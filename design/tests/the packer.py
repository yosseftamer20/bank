import sqlite3

conn = sqlite3.connect(r'C:\Users\yosse\PycharmProjects\pythonProject1\bank_system\bank_db.sqlite')
c = conn.cursor()
f = open('MOCK_DATA (7).csv', 'r')
# lines = f.readlines()
# # c.execute("delete from users;")
# for line in lines:
#     line = line.split(',')
#     sql = f"""
#     insert into main.users (id,name,dob,phone,email,password) values ({line[0]},{line[1]},'{line[2]}','{line[3]}','{line[4].strip()}')
#     """
#     print(sql)
#     c.execute(sql)
#     conn.commit()
# c.close()
# conn.close()

# Fill users
# f = open('random_data.csv', 'r')
lines = f.readlines()
for line in lines:
    line = line.split(',')
    sql = f"""
    insert into main.users (id, name, dob,email) values ({line[0]},'{line[1]}','{line[2]}','{line[3].strip()}')
    """
    print(sql)
    c.execute(sql)
    conn.commit()
c.close()
conn.close()