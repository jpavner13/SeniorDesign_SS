from flask import Flask, render_template_string

app = Flask(__name__)

# Define the HTML template as a string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SS DRONES GUI</title>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .button {
            padding: 15px 30px;
            font-size: 16px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .blackout {
            background-color: red;
            color: white;
        }
        .brownout {
            background-color: yellow;
            color: black;
        }
    </style>
</head>
<body>
    <h1>SS DRONES GUI</h1>
    <button onclick="location.href='/blackout'" class="button blackout">BLACKOUT</button>
    <button onclick="location.href='/brownout'" class="button brownout">BROWNOUT</button>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/blackout')
def blackout():
    # TODO: Will need specific code to disconnect Battery from Larger Assembly
    print("Blackout Button Triggered")
    return index()  # Redirect to the main page after the action

@app.route('/brownout')
def brownout():
    # TODO: Will need specific code to clear pending and current commands. Drone will be hovering
    print("Brownout Button Triggered")
    return index()  # Redirect to the main page after the action

if __name__ == '__main__':
    app.run(debug=True)
