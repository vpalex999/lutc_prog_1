import os, time, sys

mypid = os.getpid()
parentpid = os.getppid()

sys.stderr.write(f"Child {mypid} of {parentpid}\n got arg: sys.argv[1]")

for i in range(2):
    time.sleep(3)
    recv = input()

    time.sleep(3)
    send = f"Child {mypid} got: [{recv}]"
    print(send)

    #sys.stdout.flush()
