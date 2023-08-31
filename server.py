from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/messages', methods=['POST'])
def receive_message():
    # Get the JSON data from the request
    data = request.json
    message = data.get('message', '')
    print(f"Received message: {message}")

    return jsonify({"status": "Message received!"})

@app.route('/api/send', methods=['GET'])
def send_message():
    # Prepare a message to send to the client
    response_message = "Hello from the server!"

    # You can also send additional data as needed
    # response_data = {"key": "value"}

    # Return the message as JSON to the client
    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8885)
