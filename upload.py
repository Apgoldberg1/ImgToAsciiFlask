from flask import *  
import CVExpiriments


app = Flask(__name__) 
app.secret_key = "wewraefsdaf"
@app.route('/')  
def upload():
    session['file'] = ''  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['GET', 'POST'])  
def success():
    dims = 100
    color='False'
    if request.method == 'POST':
        if request.form.get('color') != None:
            color='True'
        if 'file' in request.files: 
            f = request.files['file']  
            f.save("static/images/" + f.filename)
            session['file'] = f.filename
            dims = CVExpiriments.process("static/images/" + f.filename, color=color)
        else:
            if request.form.get('scale') != None:
                dims = CVExpiriments.process("static/images/" + session['file'], int(request.form.get('scale')), color=color)
                return render_template("success.html", name = session['file'], scale = int(request.form.get('scale')), dims = dims, color=color)  
            else:
                dims = CVExpiriments.process("static/images/" + session['file'], color=color)
        return render_template("success.html", name = session['file'], dims = dims, color=color)  
    elif request.method == 'GET':
        dims = CVExpiriments.process("static/images/" + session['file'], color=color)
        return render_template("success.html", name = session['file'], dims = dims, color=color)
    
if __name__ == '__main__':  
    app.run(port = 5000, debug = True)  