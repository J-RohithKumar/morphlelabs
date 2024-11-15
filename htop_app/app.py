from flask import Flask
import subprocess
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = "Rohith Kumar Jupalle"
    
    ist_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    top_output = subprocess.getoutput("top -bn1 | head -20")
    response = f"""
    <html>
        <head><title>HTOP Endpoint</title></head>
        <body>
            
            <h3>Name: {username}</h3>
            <h2>user: codespace</h2>
            <h3>Server Time (IST): {ist_time}</h3>
            <h2>TOP Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
