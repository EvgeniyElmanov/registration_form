from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def index():
    print('я тут')
    return render_template('index.html')


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect(url_for('greet')))
        response.set_cookie('username', name)
        response.set_cookie('email', email)
        return response
    return redirect(url_for('index'))


@app.route('/greet')
def greet():
    username = request.cookies.get('username')
    return render_template('greet.html', username=username)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('email', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)