from flask import Flask,render_template,request,redirect,url_for,make_response,jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
# import cv2

from ImagetoText.build_vocab import Vocabulary
from run_sh import itt, ts

from datetime import timedelta

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp', 'jpeg', 'JPEG'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)

CORS(app, resources=r'/*')

app.send_file_max_age_default = timedelta(seconds=1)

@app.route('/', methods=['POST', 'GET'])
def index():
    # filename = None
    # if request.method == 'POST':
    #     f = request.files['file']

    #     if not (f and allowed_file(f.filename)):
    #         return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})
 
    #     # user_input = request.form.get("name")

    #     basepath = os.path.dirname(__file__)

    #     filename=secure_filename(f.filename)
    #     upload_path = os.path.join(basepath, 'static/images',filename)
    #     f.save(upload_path)

    #     if filename == None:
    #         return render_template('index.html', userinput=None)
    #     else:
    #         userinput = url_for('static', filename=f'images/{filename}')
    #         print(userinput)
    #         sentence = itt(f'E:\\4160\\static\\images\\{filename}')
    #         return render_template('index.html', userinput=userinput, sentence=sentence)
    return render_template('index.html')

@app.route('/i2t', methods=['POST'])
def imagetotext():
    if request.method == 'POST':
        f = request.files['file']

    basepath = os.path.dirname(__file__)

    filename=secure_filename(f.filename)
    upload_path = os.path.join(basepath, 'static/images', filename)
    f.save(upload_path)

    # userinput = url_for('static', filename=f'images/{filename}')
    userinput = f"http://10.30.6.52:5000/static/images/{filename}"

    sentence = itt(f'E:\\4160\\static\\images\\{filename}')
    return jsonify({"sentence":sentence.strip('<start>').strip('<end>'), "image":userinput})

@app.route('/ts', methods=['POST'])
def textsummarization():
    if request.method == 'POST':
        text = request.form['text']
    return ts(text)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug= True)