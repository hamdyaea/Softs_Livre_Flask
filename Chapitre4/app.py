from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def random_number():
    random_num = random.randint(1, 100)
    return render_template('random.html', random_num=random_num) 
#avec le return, une seule ligne.

if __name__ == '__main__':
    app.run(debug=True)
