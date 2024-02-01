import speedtest
from datetime import datetime, timezone
import time
import sqlite3





def get_timestamp():
    timestamp = int(datetime.now(timezone.utc).timestamp())
    return timestamp

def speed_test():
    con = sqlite3.connect("speed_log.db")
    cur = con.cursor()
    s = speedtest.Speedtest()
    ## s.get_best_server()

    s.get_closest_servers()
    print("Starting speed test")
    cur.execute("INSERT INTO speed (time, download, upload) VALUES (?,?,?)", (get_timestamp(), s.download(), s.upload()))
    con.commit()
    con.close()
    print("Finished")

while True:
    speed_test()
    time.sleep(600)
    

