from flask import Flask, render_template
import im_a_simple_robot as simp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

def train_simple(train_set, train_labels):
    weights, bias = simp.train("", "", .01, 1000)
    # write weights to file 
    # write bias to file

def classify_simple(weights, bias, dev_set):
    simp.classify(weights, bias, dev_set)
    # write the results to html page

