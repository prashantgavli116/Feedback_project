from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'feedback.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT,
                  rating INTEGER NOT NULL,
                  comments TEXT,
                  date TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form.get('email', '')
    rating = int(request.form['rating'])
    comments = request.form.get('comments', '')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO feedback (name, email, rating, comments, date) VALUES (?, ?, ?, ?, ?)",
              (name, email, rating, comments, date))
    conn.commit()
    conn.close()
    
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/view-feedback')
def view_feedback():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM feedback ORDER BY date DESC")
    feedback_items = c.fetchall()
    conn.close()
    return render_template('view_feedback.html', feedback=feedback_items)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)