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

    projects = []

    for item in os.listdir(BASE_PATH):

        path = os.path.join(
            BASE_PATH,
            item
        )

        # Only show folders, ignore .gitkeep and files
        if os.path.isdir(path):
            projects.append(item)

    return projects



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
def get_project_file(name):

    project_path = os.path.join(
        BASE_PATH,
        name
    )

    if not os.path.exists(project_path):
        return None


    for file in os.listdir(project_path):

        if file.lower().endswith(
            (".xlsx", ".xls")
        ):

            return os.path.join(
                project_path,
                file
            )


    return None


    return None
