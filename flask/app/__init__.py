from flask import Flask

app1 = Flask(__name__)

from app.utils import NLPTasks

nlp_obj = NLPTasks()

from app import main
