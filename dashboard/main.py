import base64
import json
import logging
import os
import sys

import panel as pn
from openvisuspy import SetupLogger, Slice

try:
    from openvisuspy import ProbeTool
except ImportError:
    ProbeTool = None


if __name__.startswith("bokeh"):
    pn.extension(
        "ipywidgets",
        "floatpanel",
        log_level="DEBUG",
        notifications=True,
        sizing_mode="stretch_width",
    )

    log_filename = os.environ.get(
        "OPENVISUSPY_DASHBOARDS_LOG_FILENAME", "logs/dashboard.log"
    )
    logger = SetupLogger(log_filename=log_filename, logging_level=logging.DEBUG)

    if len(sys.argv) < 2:
        raise RuntimeError("Expected an IDX path after --args.")

    view = Slice()
    view.load(sys.argv[1])

    query_params = dict(pn.state.location.query_params)
    if "load" in query_params:
        body = json.loads(base64.b64decode(query_params["load"]).decode("utf-8"))
        if hasattr(view, "setSceneBody"):
            view.setSceneBody(body)
        else:
            view.setBody(body)
    elif "dataset" in query_params:
        scene_name = query_params["dataset"]
        view.scene.value = scene_name

    if False and ProbeTool is not None:
        app = ProbeTool(view).getMainLayout()
    else:
        app = view.getMainLayout()

    app.servable()
