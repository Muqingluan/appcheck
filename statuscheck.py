import os
import time

if __name__ == "__main__":

    while True:
        if os.system('ps -ef | grep main.py') != None:
            os.system("python main.py")

        time.sleep(2)
