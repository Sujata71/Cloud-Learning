from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style='text-align: center; margin-top: 10%; font-family: sans-serif;'>
        <h1>🚀 Sujata's Python Flask Container is Live!</h1>
        <p>This infrastructure project is running entirely inside an isolated Docker container room.</p>
    </div>
    """

if __name__ == '__main__':
    # host='0.0.0.0' allows external connections from outside the container
    app.run(host='0.0.0.0', port=5000)