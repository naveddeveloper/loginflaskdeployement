from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

app.secret_key = "super-secret-key-naved"

@app.route("/")
def index():
    if 'username' in session:
        return f"Welcome, {session['username']}!  <button><a href='/logout'>Logout</a></button>"
    return "<button><a href='/login'>Login</a></button>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['name']
        flash("You've been logged in!")
        return redirect(url_for("index"))
    else:
        return render_template("login.html")


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)