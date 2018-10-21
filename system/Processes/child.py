import os, sys

print("Hello from child ", os.getegid(), sys.argv[1])