from flask import Flask, render_template, request, redirect, url_for, session
import logging
import redis
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

logging.basicConfig(filename='/logs/app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w',
                    datefmt='%d-%b-%y %H:%M:%S')

users = {"user1": "password1", "user2": "password2"}

RATE_LIMIT = 5  # 5 requests
TIME_WINDOW = 60  # per 60 seconds

@app.route('/', methods=['GET', 'POST'])
def login():
    redis_client.incr('visit_count')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        ip = request.remote_addr # Get the IP address of the client
        if not rate_limited(ip):
            if username in users and users[username] == password:
                session['username'] = username
                logging.info(f"User {username} logged in successfully.")
                return redirect(url_for('dashboard'))
            else:
                logging.warning(f"Failed login attempt for user {username}.")
                return "Invalid credentials!", 401
        else:
            logging.warning(f"Rate limit exceeded for IP: {ip}")
            return render_template('error.html'), 429
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))


def rate_limited(ip):
    """Checks if the IP is rate-limited"""
    count = redis_client.get(ip)
    if count:
        count = int(count)
        if count >= RATE_LIMIT:
            return True
        else:
            redis_client.incr(ip)
    else:
        redis_client.set(ip, 1, ex=TIME_WINDOW)
    return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
