import _mysql
import sys


sql_ip = "104.130.70.88"
sql_user = "perp"
sql_pass = "gBu{P2>V"
sql_db = "perp"

try:
    con = _mysql.connect(sql_ip, sql_user, sql_pass, sql_db)
        
    con.query("SELECT * FROM ip_intel")
    result = con.use_result()
    
    
    print(result)
    
except _mysql.Error, e:
  
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    
    if con:
        con.close()
