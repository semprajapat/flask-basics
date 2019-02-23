from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def admin_page():
    return "Hello Admin !"

@app.route("/guest/<guest>")
def guest_name(guest):
    return "Hello %s as a guest !"%guest


@app.route("/user/<name>")
def user(name):
    if name == 'admin':
        return redirect(url_for("admin_page"))
    else:
        return redirect(url_for("guest_name",guest = name))


if __name__ == "__main__":
    app.run(debug=True)