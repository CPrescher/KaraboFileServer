import time
from app import get_frame_from_karabo


t1 = time.time()
for i in range(1, 20):
    get_frame_from_karabo(67, i)
    print('Time needed: {} s'.format(time.time()-t1))
    t1=time.time()
