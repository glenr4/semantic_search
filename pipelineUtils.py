pipelines = {}  # pylint: disable=global-statement


def get_pipelines():
    if not pipelines:
        raise LookupError("Pipelines are not initiated")
    return pipelines


def set_pipelines(pipelineName, pipeline):
    pipelines[pipelineName] = pipeline
