import requests
import numpy as np
import os

url = "https://australia-southeast1-wald-1526877012527.cloudfunctions.net/dea-live-grades"

def obj_encoder(obj):
    if isinstance(obj, np.dtype):
        return str(obj)
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.bool):
        return bool(obj)
    elif isinstance(obj, np.ndarray):
        if obj.size > 20:
            return -1
        return obj.tolist()
    elif isinstance(obj, tuple):
        return list(obj)[:20]
    else:
        return obj


def check_answer(uid, ans):
    data = {"uid": uid,
            "user": os.getenv('JUPYTERHUB_USER') if os.getenv('JUPYTERHUB_USER') else 'anonymous',
            "message": obj_encoder(ans)}

    r = requests.post(url, json=data)
    return r.text
    #return data
