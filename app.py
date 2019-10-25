from flask import flask, render_template, request

app = flask (__name__)


@app.route('/')
def index():
    return render_template('index.html')

    @app.route('/submit', methods=('post'))
    def submit():
        if request.method == 'post'
        

   

   if __name__ == '__main__':
       app.debug = true 
       app.run()