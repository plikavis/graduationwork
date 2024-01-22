import json
import os


def load_schema(filepath):
    with open(abs_path_from_project('schemes') + "/" + filepath) as file:
        schema = json.load(file)
        return schema


def abs_path_from_project(relative_path: str):
    import testrail_project_test
    from pathlib import Path
    return (
        Path(testrail_project_test.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
