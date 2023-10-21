# import sqlite3
#
# with sqlite3.connect('Sugar_DB.db') as db:
#     cur = db.cursor()
#     query = '''SELECT sugar_values, mesuaring_date
#                 FROM sugar_mesuaring
#                 WHERE part_of_day = 'Morning'
#                 '''
#     cur.execute(query)
#     val = cur.fetchall()
#     for x, y in val:
#         print(x)
#         print(y)
#     print(val)
#
#     # for X in val:
#     #     print(X)
#     db.commit()
import sqlite3

with sqlite3.connect('Sugar_DB.db') as db:
    cur = db.cursor()
    query = f'''SELECT * 
        FROM sugar_mesuaring
        ORDER BY musuaring_id DESC 
        LIMIT 7 '''
    cur.execute(query)
    db_val_morning = cur.fetchall()
    print(db_val_morning)