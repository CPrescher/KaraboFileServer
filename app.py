import os
import io
import numpy as np

from karabo_data import RunDirectory
from flask import Flask

try:
    from config import base_dir, instrument_source, instrument_key
except ModuleNotFoundError:
    from _config import base_dir, instrument_key, instrument_key


app = Flask(__name__)

import time

@app.route('/run_<run_index>/frame_<frame_index>')
def get_frame(run_index, frame_index):
    t1 = time.time()
    data = get_frame_from_karabo(int(run_index), int(frame_index))
    bytestream = io.BytesIO()
    np.save(bytestream, data)
    print(time.time()-t1)
    return bytestream.getvalue()


@app.route('/run_<run_index>')
def get_run(run_index):
    data = get_run_from_karabo(int(run_index))
    bytestream = io.BytesIO()
    np.save(bytestream, data)
    return bytestream.getvalue()


def get_frame_from_karabo(run_index, frame_index):
    run = RunDirectory(os.path.join(base_dir, 'r{:04d}'.format(run_index)))
    tid, data = run.train_from_index(frame_index)
    return data[instrument_source][instrument_key]


def get_run_from_karabo(run_index):
    run = RunDirectory(os.path.join(base_dir, 'r{:04d}'.format(run_index)))
    print(len(run.train_ids))
    data = run.get_array(instrument_source, instrument_key)
    return data
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')
