from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('feedback.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home Page (Feedback Form)
@app.route('/')
def index():
    return render_template('index.html')

# Submit Feedback
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    rating = request.form['rating']
    comment = request.form['comment']

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO feedback (name, rating, comment) VALUES (?, ?, ?)',
        (name, rating, comment)
    )
    conn.commit()
    conn.close()

    return redirect('/')

# Admin Dashboard
@app.route('/admin')
def admin():
    conn = get_db_connection()
    feedbacks = conn.execute('SELECT * FROM feedback').fetchall()

    ratings = conn.execute(
        'SELECT rating, COUNT(*) as count FROM feedback GROUP BY rating'
    ).fetchall()

    conn.close()

    return render_template(
    'admin.html',
    feedbacks=feedbacks,
    ratings=ratings
)
if __name__ == '__main__':
    app.run(debug=True, port=5001)