import requests
try:
    from flask import Flask,render_template,url_for,request,redirect, make_response
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github
except Exception as e:
    print("Some Modules are Missings {}".format(e))


app = Flask(__name__)
app.config["SECRET_KEY"]="Client secrets"

github_blueprint = make_github_blueprint(client_id='Client ID',
                                         client_secret='Client secrets')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

@app.route('/user')
def user():
    response = requests.get("https://api.github.com/users/Prateeksharma911/events")
    response = response.json()
    return response


@app.route('/login')
def github_login():

    if github.authorized:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            details=user()
            return '<h1>Login Sucessfull {} '.format(account_info_json['login'],details)
        
    else:
        print("Authorization failed")

    return redirect(url_for('github.login'))


if __name__ == "__main__":
    app.run(debug=True)