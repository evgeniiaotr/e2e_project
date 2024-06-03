from flask import Flask​

​

app = Flask(name)​

​

​

@app.route("/admin")​

def hello_admin():​

    return "Hello Admin"​

​

​

if name == "main":​

    app.run(debug=True)
