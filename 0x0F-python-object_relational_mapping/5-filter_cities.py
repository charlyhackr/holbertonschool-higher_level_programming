#!/usr/bin/python3
# Displays all cities of a given state
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    op = db.cursor()
    op.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([cit[2] for cit in c.fetchall() if cit[4] == sys.argv[4]]))
