import os
from karabo_data import RunDirectory


base_dir = '/gpfs/exfel/exp/HED/201922/p002550/raw'

with open('instrument_sources.txt', 'w') as f:
    for i in range(1, 150):
        try:
            run = RunDirectory(os.path.join(base_dir, 'r{:04d}'.format(i)))
        except:
            continue
        f.write('run {}, trains={}, source={}\n'.format(i, len(run.train_ids), run.instrument_sources))
        print('run {}, trains={}, source={}\n'.format(i, len(run.train_ids), run.instrument_sources))

