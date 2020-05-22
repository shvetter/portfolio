from flask import Flask, render_template, request, redirect
import os
import csv
app = Flask(__name__)

@app.route('/')
def indexhtml():
    # indicate the name path of .html file
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_html(page_name):
    # indicate the name path of .html file
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':    # as we indicated in html file method POST
    	try:
        	data = request.form.to_dict()   # to place all data in dict named data
        # write data to database.txt
        # with open('database.txt', 'a') as db:
        # 	for value in data.values():
        # 		db.write(value + ', ')
        # 	db.write('\n')

        #or we can define function and use it
        	write_to_csv(data)
        	# redirect is uded to jump to another html
        	return redirect('/msg_sent.html')
    	except:
        	return 'Not saved to DB('
    else:
        return 'smth went wrong. Try again!'

# deifne func to write to txt file
def write_to_db(data):
	email = data['email']
	subject = data['subject']
	message = data['message']
	with open('database.txt', mode='a') as db:			# note that mode 'a' means append
		db.write(f'\n{email},{subject},{message}')

# define func to write to csv file
def write_to_csv(data):
	with open('database.csv', 'a', newline='') as db2:
		db_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		# delimiter above is how the data will be separated. As we using CSV, comma is here
		db_writer.writerow(data.values())