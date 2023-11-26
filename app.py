from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace these with your RDS credentials
db_credentials = {
    'host': 'surya-db.cg9yyqmiwyp9.us-east-2.rds.amazonaws.com',
    'user': 'admin',
    'password': 'Binamare8*',
    'database': 'surya_database',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        save_to_database(first_name, last_name)
        return render_template('success.html', first_name=first_name, last_name=last_name)

def save_to_database(first_name, last_name):
    connection = mysql.connector.connect(**db_credentials)
    cursor = connection.cursor()

    # Assuming you have a 'person' table with 'first_name' and 'last_name' columns
    query = "INSERT INTO person (firstname, lastname) VALUES (%s, %s)"
    values = (first_name, last_name)

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
