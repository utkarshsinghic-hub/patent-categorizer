import os
import json


BASE_PATH = "data/projects"


def create_project(name):

    path = os.path.join(
        BASE_PATH,
        name
    )

    os.makedirs(
        path,
        exist_ok=True
    )

    return path



def get_projects():

    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

    return os.listdir(BASE_PATH)



def delete_project(name):

    import shutil

    path=os.path.join(
        BASE_PATH,
        name
    )

    if os.path.exists(path):
        shutil.rmtree(path)



def rename_project(old,new):

    os.rename(
        os.path.join(BASE_PATH,old),
        os.path.join(BASE_PATH,new)
    )
