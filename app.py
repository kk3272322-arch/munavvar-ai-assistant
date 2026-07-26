from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Munavvar AI Assistant</title>
<style>
body {
    font-family: Arial;
    background:#f5f5f5;
    padding:30px;
}
.box {
    max-width:600px;
    margin:auto;
    background:white;
    padding:25px;
    border-radius:15px;
}
h1 {
    color:#b02a5b;
}
input, button {
    width:100%;
    padding:12px;
    margin-top:10px;
}
button {
    background:#b02a5b;
    color:white;
    border:0;
}
</style>
</head>

<body>
<div class="box">
<h1>🌸 Munavvar AI Assistant</h1>

<p>Помощник для цветочного бизнеса</p>

<form>
<input placeholder="Напишите вопрос про букет">
<button>Отправить</button>
</form>

</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

app.run(host="0.0.0.0", port=10000)
