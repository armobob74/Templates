from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Sp3g9hT2I'



@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
