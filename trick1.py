import sys, time

def carriage_return():
    sys.stdout.write('\r')
    sys.stdout.flush()

for i in range(100):
        print i,
        carriage_return()
        time.sleep(1)
