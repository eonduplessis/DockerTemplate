"""
Base service to expose model functions
"""

import flask
import model

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'],
            summary='Interact with hosted advanced analytics model',
            description="",
            response_description="")
async def home():
    """
    Routing to custom model script functions
    """
    test = model.evaluate()
    return test