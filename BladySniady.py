from flask import Flask, render_template_string

app = Flask(__name__)

# Twój kod HTML przeniesiony do zmiennej (lub oddzielnego pliku)
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>RAJU - Gaming Hub</title>
    <style>
        body { background-color: #0f0f0f; color: white; text-align: center; font-family: Arial; }
        h1 { color: #00ffcc; }
        .social a {
            display: block; margin: 15px auto; padding: 10px; width: 200px;
            background: #1f1f1f; color: white; text-decoration: none;
            border-radius: 8px; transition: 0.3s;
        }
        .social a:hover { background: #00ffcc; color: black; }
    </style>
</head>
<body>
    <h1>🎮 RAJU</h1>
    <p>FPS Grinder | Competitive Mindset</p>
    <div class="social">
        <a href="https://youtube.com/twojlink" target="_blank">YouTube</a>
        <a href="https://twitch.tv/twojlink" target="_blank">Twitch</a>
        <a href="https://discord.gg/twojlink" target="_blank">Discord</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)