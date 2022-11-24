from flask import jsonify

from backpythonkpi.db import records

def get_records_by_filter(filter_func):
    return jsonify(list(filter(
        filter_func,
        records.values(),
    )))