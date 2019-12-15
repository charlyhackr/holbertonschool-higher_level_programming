#!/usr/bin/python3
# anti mysql injection
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    op = db.cursor()
    op.execute("SELECT * FROM `states`")
    [print(s-tate) for state in op.fetchall() if state[1] == sys.argv[4]]
