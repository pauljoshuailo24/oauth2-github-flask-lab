from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

oauth = OAuth(app)

github = oauth.register(
    name='github',
    client_id='Ov23lilQBeuERbLcu7Cq',
    client_secret='a7453ddf081bbbef5547f1a45891d4bc6d76caf0',

    access_token_url='https://github.com/login/oauth/access_token',

    authorize_url='https://github.com/login/oauth/authorize',

    api_base_url='https://api.github.com/',

    client_kwargs={
        'scope': 'user:email',
    },
)

# LOGIN ROUTE
@app.route('/login')
def login():
    return github.authorize_redirect(
        'http://localhost:5000/callback'
    )

# CALLBACK ROUTE
@app.route('/callback')
def callback():

    token = github.authorize_access_token()

    user = github.get('user').json()

    session['user'] = user

    return redirect('/profile')

# PROTECTED PROFILE ROUTE
@app.route('/profile')
def profile():

    if 'user' not in session:
        return "Unauthorized", 401

    return jsonify(session['user'])

# BONUS PROTECTED API
@app.route('/api/secure-data')
def secure_data():

    if 'user' not in session:
        return jsonify({
            "error": "Unauthorized"
        }), 401

    return jsonify({
        "message": "This is protected secure data!",
        "user": session['user']['login']
    })

# LOGOUT ROUTE
@app.route('/logout')
def logout():

    session.pop('user', None)

    return "Logged out successfully"

# RUN APP
if __name__ == '__main__':
    app.run(debug=True)