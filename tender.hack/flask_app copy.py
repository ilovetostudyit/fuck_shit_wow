from flask import Flask, request, render_template, redirect, url_for
from parse_excel import year_parse
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save("test.xlsx")
      new_parse = year_parse
      new_parse.just_parse(year_parse, "test.xlsx")
      return redirect('1.html')
   else:
       return "No file"
   
@app.route('/1.html', methods = ['GET', 'POST'])
def blocks_page():
    if request.method == 'POST':
      f = request.files['file']
      f.save("test.xlsx")
      new_parse = year_parse
      new_parse.just_parse(year_parse, "test.xlsx")
      return redirect('1.html')
    else:
        return render_template('1.html')

@app.route('/year.json')
def year_json():
    return render_template('year.json')

if __name__ == '__main__':
   app.run()