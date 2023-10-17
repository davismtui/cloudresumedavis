from flask import Flask, render_template
import updater
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    number = updater.update()
    return render_template('index.html', number=f'Page View Count: {number}')




if __name__ == '__main__':
    app.run()
