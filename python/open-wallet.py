import subprocess
import os

def run(cmd):
    return subprocess.run(cmd, shell=True)
wd = "/data/wallet/"
# ws = os.listdir("./")
ws = os.listdir(wd)
print(ws)
for w in ws:
    sl = w.split(".")
    print(sl[0])
    if sl[1] == "wallet":
        cmd = "cleos --wallet-url http://127.0.0.1:23333 --url http://172.18.0.2:2333 wallet open -n " + sl[0]
        run(cmd)