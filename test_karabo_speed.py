import time
from app import get_frame_from_karabo, get_run_from_karabo

print('#####################')
print('Getting single Frames')
t1 = time.time()
for i in range(1, 10):
    get_frame_from_karabo(67, i)
    print('Time needed: {} s'.format(time.time()-t1))
    t1=time.time()

print('##################')
print('Getting whole runs')
t1 = time.time()
for i in range(67, 77):
    get_run_from_karabo(67)
    print('Time needed: {} s'.format(time.time()-t1))
    t1=time.time()

