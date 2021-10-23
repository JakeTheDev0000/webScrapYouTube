import os
import time

cls = lambda: os.system('cls')

def wait(timeX):
    time.sleep(timeX)

def main():
    print("starting")
    wait(1)
    cls()


main()