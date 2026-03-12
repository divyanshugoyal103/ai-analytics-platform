import os
import json

REGISTRY_FILE = "datasets/registry.json"

def register_dataset(dataset_id, metadata):

    if not os.path.exists(REGISTRY_FILE):
        with open(REGISTRY_FILE,"w") as f:
            json.dump({},f)

    with open(REGISTRY_FILE,"r") as f:
        data = json.load(f)

    data[dataset_id] = metadata

    with open(REGISTRY_FILE,"w") as f:
        json.dump(data,f)


def get_dataset(dataset_id):

    with open(REGISTRY_FILE,"r") as f:
        data = json.load(f)

    return data.get(dataset_id)