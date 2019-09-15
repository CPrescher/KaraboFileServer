from flask import Flask, request
import os
import io
import numpy as np
from karabo_data import RunDirectory

app = Flask(__name__)

base_dir = '/gpfs/exfel/exp/HED/201922/p002550/raw'
instrument_source = 'HED_IA1_EPIX10K-1/DET/RECEIVER:daqOutput'
instrument_key = 'data.image.pixels'

@app.route('/run_<run_index>/frame_<frame_index>')
def get_frame(run_index, frame_index):
    data = get_frame_from_karabo(int(run_index), int(frame_index))
    bytestream = io.BytesIO()
    np.save(bytestream, data)
    return bytestream.getvalue()


def get_frame_from_karabo(run_index, frame_index):
    run = RunDirectory(os.path.join(base_dir, 'r{:04d}'.format(run_index)))
    tid, data = run.train_from_index(frame_index)
    return data[instrument_source][instrument_key]

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7545)
