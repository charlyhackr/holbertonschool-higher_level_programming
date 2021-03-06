#!/usr/bin/python3
# List all states from the data base
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    op = db.cursor()
    op.execute("SELECT * FROM `states`")
    [print(state) for state in op.fetchall()]
