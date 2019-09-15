import requests
import numpy as np
import io
import time
from pylab import *

server_address = 'max-exfl001'


def get_data(run, frame):
    r = requests.get('http://{}:7545/run_{}/frame_{}'.format(server_address, run, frame))
    return np.load(io.BytesIO(r.content))

t1 = time.time()
for i in range(1, 20):
    get_data(67, i)
    print('Time needed: {} s'.format(time.time()-t1))
    t1=time.time()
