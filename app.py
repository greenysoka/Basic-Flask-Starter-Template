from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') # The website page is located in the templates folder, you can change this to your needs

if __name__ == '__main__':
    # Change this if you host in a container and wanna use a different port to reach the internet
    app.run(debug=True, host="0.0.0.0", port=5000) # Disable debug for production use!
