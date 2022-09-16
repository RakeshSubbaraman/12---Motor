
from flask import Flask, render_template, request
import control
app = Flask(__name__)

control.init()


@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.form.get('submit_rc') == 'up':
        print("WRKS")
        control.forward()
    elif request.form.get('submit_rc') == 'down':
        print("d")
        control.reverse()
    elif request.form.get('submit_rc') == 'up-left':
        print("ul")
        control.forward_left()
    elif request.form.get('submit_rc') == 'up-right':
        print("ur")
        control.forward_right()
    elif request.form.get('submit_rc') == 'down-left':
        print("dl")
        control.backward_left()
    elif request.form.get('submit_rc') == 'down-right':
        print("dr")
        control.backward_right
    elif request.form.get('submit_rc') == 'stop':
        control.neutral()
    elif request.method == 'GET':
        return render_template('main.html', form='form')
    return render_template("main.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
