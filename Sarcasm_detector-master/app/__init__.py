
import os
import flask, flask.views
from flask import Markup
from flask import jsonify
from app import evaluate

app = flask.Flask(__name__)

class Main(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
    
 
class About(flask.views.MethodView):
    def get(self):
        return flask.render_template('about.html')
    
class Contact(flask.views.MethodView):
    def get(self):
        return flask.render_template('contact.html')   

app.add_url_rule('/',view_func=Main.as_view('main'), methods=["GET"])
app.add_url_rule('/about/',view_func=About.as_view('about'), methods=["GET"])
app.add_url_rule('/contact/',view_func=Contact.as_view('contact'), methods=["GET"])


@app.route('/sarcasmComputation')
def sarcasmComputation():
    sentence = flask.request.args.get('sentence')
    print "Start " + sentence
    percentage = evaluate.tweetscore(str(sentence))
    print "Got " + str(percentage)
    return jsonify(result=percentage)
    

