from flask import Flask, request, jsonify
app = Flask(__name__)

# Приклад бази даних у вигляді словника
tasks = {
    1: {"task": "Buy groceries", "done": False},
    2: {"task": "Learn Python", "done": False}
}

# Create (Створити нову задачу)
@app.route('/tasks', methods=['POST'])
def add_task():
    new_id = max(tasks.keys()) + 1
    task_data = request.get_json()
    tasks[new_id] = {"task": task_data['task'], "done": task_data.get('done', False)}
    return jsonify({"id": new_id, "task": task_data['task']}), 201

# Read (Отримати всі задачі)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Update (Оновити задачу)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    task_data = request.get_json()
    tasks[task_id]["task"] = task_data['task']
    tasks[task_id]["done"] = task_data.get('done', tasks[task_id]["done"])
    return jsonify(tasks[task_id]), 200

# Delete (Видалити задачу)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404
    del tasks[task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
