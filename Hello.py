from flask import Flask, redirect, url_for, request, render_template, session, escape
app = Flask(__name__)
app.secret_key = '12345678'

@app.route('/hello')
def hello_world():
   return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
   

#@app.route('/')
#def index():
#   return render_template('hello.html')

@app.route('/hello/<user>')
def hello_name1(user):
   return render_template('hello.html', name = user)

@app.route('/hello/<int:score>')
def hello_score(score):
   return render_template('score.html', marks = score)

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

#@app.route("/")
#def index():
#   return render_template("index.html")
   
@app.route('/old')
def student():
   return render_template('student.html')

@app.route('/results',methods = ['POST', 'GET'])
def results():
   if request.method == 'POST':
      result = request.form
      return render_template("results.html",result = result)

@app.route('/')
def index():
   if  'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login1'></b>" + "click here to log in</b></a>"

@app.route('/login1', methods = ['GET', 'POST'])
def login1():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return '''
	
   <form action = "" method = "post">
      <p><input type = text name = username /></p>
      <p><input type = submit value = Login /></p>
   </form>
	
   '''

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))


   
if __name__ == '__main__':
   #app.run(debug = True)
   app.run()
