import json
import os


def load_schema(filepath):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/schemes/' + filepath) as file:
        schema = json.load(file)
        return schema


def abs_path_from_project(relative_path: str):
    from testrail_project_test import pages
    from pathlib import Path
    return (
        Path(pages.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
