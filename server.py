from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    # return 'Hello, Sany!'
    return render_template('index.html')

@app.route('/<username>/<int:post_id>')
def good_morning(username=None,post_id=None):
    # return 'Hello, Sany!'
    return render_template('index.html',name=username,post_id=post_id)

@app.route('/<string:page_name>')
def html_page(page_name:None):
    # return 'Hello, Sany!'
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # with open('database.txt',mode='a') as db_file:
            #     db_file.write(str(data))
            # print(data)
            write_to_csv(data)
            return redirect('thank_you.html')
        except:
            return "Sorry! Could not save the data!"
    else:
        return "Something went wrong"

def write_to_csv(data):
    with open('database.csv',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


# @app.route('/index.html')
# def index():
#     # return 'Hello, Sany!'
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     # return 'Hello, Sany!'
#     return render_template('about.html')

# @app.route('/components.html')
# def components():
#     # return 'Hello, Sany!'
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     # return 'Hello, Sany!'
#     return render_template('contact.html')

# @app.route('/works.html')
# def works():
#     # return 'Hello, Sany!'
#     return render_template('works.html')

# @app.route('/blog')
# def blog():
#     return 'Hello, In the BLOG!'