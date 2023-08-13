from flask import Flask, request, jsonify
from flask_cors import CORS
from psycopg2 import pool

app = Flask(__name__)
CORS(app)

# Database connection pool
db_params = {
    'database': 'perntodo',
    'user': 'robertguzman',
    'password': 'Civic1234',
    'host': 'localhost',
    'port': '5432'
}
conn_pool = pool.SimpleConnectionPool(1, 10, **db_params)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/todos', methods=['POST'])
def create_todo():
    try:
        data = request.get_json()
        description = data['description']

        conn = conn_pool.getconn()
        cursor = conn.cursor()

        query = "INSERT INTO todo (description) VALUES (%s) RETURNING *"
        cursor.execute(query, (description,))
        new_todo = cursor.fetchone()

        conn.commit()
        conn_pool.putconn(conn)

        return jsonify(new_todo)
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/todos', methods=['GET'])
def get_all_todos():
    try:
        conn = conn_pool.getconn()
        cursor = conn.cursor()

        query = "SELECT * FROM todo"
        cursor.execute(query)
        all_todos = cursor.fetchall()

        conn_pool.putconn(conn)

        return jsonify(all_todos)
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    try:
        conn = conn_pool.getconn()
        cursor = conn.cursor()

        query = "SELECT * FROM todo WHERE todo_id = %s"
        cursor.execute(query, (id,))
        todo = cursor.fetchone()

        conn_pool.putconn(conn)

        return jsonify(todo)
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    try:
        data = request.get_json()
        description = data['description']

        conn = conn_pool.getconn()
        cursor = conn.cursor()

        query = "UPDATE todo SET description = %s WHERE todo_id = %s"
        cursor.execute(query, (description, id))

        conn.commit()
        conn_pool.putconn(conn)

        return jsonify({'message': 'Todo was updated!'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    try:
        conn = conn_pool.getconn()
        cursor = conn.cursor()

        query = "DELETE FROM todo WHERE todo_id = %s"
        cursor.execute(query, (id,))

        conn.commit()
        conn_pool.putconn(conn)

        return jsonify({'message': 'Todo was deleted!'})
    except Exception as e:
        print(e)
        return jsonify({'error': 'An error occurred'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
