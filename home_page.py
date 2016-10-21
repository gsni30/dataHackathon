from flask import app,Flask
from flask import render_template, request,redirect,url_for, send_from_directory
import os

app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('home.html')

# @app.route('/upload', methods=['POST'])
# def upload():

	# file = request.files['file']
	# nol=request.form["nol"]
	# if file and allowed_file(file.filename):

		# filename = secure_filename(file.filename)

		# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	# return redirect(url_for('uploaded_file',
                                # filename=filename))

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
	# retfname=route.main_sum(filename,nol)
	# return redirect(url_for('download.html'),None)
    # # return send_from_directory(app.config['UPLOAD_FOLDER'],
                               # # filename)
	# # return "ab"
	
if __name__ == "__main__":
	app.run(debug=True)
