import time
#for sleeping
import hashlib
from datetime import datetime as dt

hosts_file_sample = "hosts"
localhost = "127.0.0.1"
websites = ["www.youtube.com"]
starting_time = 8
ending_time = 14
# add the websites you want to block

BLOCK_SIZE = 65536
prev_hashDigest = "1d03cd07586d183c798c75a7667231fa8de98349328c55710734d6592472476d"
#for hashing

#run a infinite Loop
while True:
    #for jumping lines
    line_offset = []
    offset = 0
    with open('hosts','r+') as file:
        for line in file:
            line_offset.append(offset)
            offset += len(line)

    file_hash = hashlib.sha256()
    with open('hosts', 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    cur_hashDigest = file_hash.hexdigest()

    time.sleep(5)
    print(dt.now())
    if dt(dt.now().year,dt.now().month,dt.now().day,starting_time)<dt.now() and dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,ending_time):
        print("Blocker is active")
        with open('hosts','r+') as file:
            text = file.read()
            for website in websites:
                if website in text:
                    pass
                else:
                    file.write("\n"+localhost+"  "+website+"\n")
    else:
        print("Blocker is not active")
        print(prev_hashDigest,cur_hashDigest)
        if prev_hashDigest != cur_hashDigest:
            text = None
            with open('hosts','r+') as file:
                text = file.readlines()
            with open('hosts','r+') as file:
                try:
                    file.seek(line_offset[20])
                    file.write("\n")
                    file.truncate()
                except:
                    pass
    prev_hashDigest = cur_hashDigest

