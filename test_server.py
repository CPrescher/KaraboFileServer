import requests
import numpy as np
import io
import time
from pylab import *

server_address = 'ppv'
port = 5000


def get_frame(run, frame):
    r = requests.get('http://{}:{}/run_{}/frame_{}'.format(server_address, port, run, frame))
    return np.load(io.BytesIO(r.content))

def get_run(run):
    r = requests.get('http://{}:{}/run_{}'.format(server_address, port, run))
    return np.load(io.BytesIO(r.content))


print('#####################')
print('Getting single Frames')
t1 = time.time()
for i in range(20, 23):
    get_frame(17, i)
    print('Time needed: {} s'.format(time.time()-t1))
    t1=time.time()


print('##################')
print('Getting whole runs')
t1 = time.time()
for i in range(1, 10):
    get_run(67)
    print('Time needed: {} s'.format(time.time()-t1))
    t1=time.time()

