import time
import os

def create_uuid():
    rand = os.urandom(16)
    rand = rand.hex()
    uuid = '-'.join([rand[0:8], rand[8:16], rand[16:32]])
    return uuid
    
if __name__ == '__main__':
    print(create_uuid())