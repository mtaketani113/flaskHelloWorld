from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    name = "who"
    #return name
    return render_template('hello.html', title='hello', name=name)

@app.route('/<name>')
def helloName(name):
    #return name
    return render_template('hello.html', title='hello', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)