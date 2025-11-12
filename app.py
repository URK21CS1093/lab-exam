from flask import Flask,render_template_string

app=Flask(__name__)

template="""
<h1>This is experiment 4</h1>
"""

@app.route('/')
def home():
    return render_template_string(template)

app.run(host="0.0.0.0",port=5000)