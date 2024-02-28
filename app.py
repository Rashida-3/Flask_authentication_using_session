from flask import Flask ,request,session

from datetime import timedelta
app=Flask(__name__)
app.secret_key='hello '
app.permanent_session_lifetime=timedelta(seconds=25)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        session.permanent=True
        user=request.json['user']
        password=request.json['password']
        session['user']=user

        if user =='rashida' and password==12345:
            return 'login sucessfully done'
        else:
            return 'invalid credentials '
    else:
        if 'user' in session:
            return 'login'
        
@app.route('/user')
def user():
    if 'user' in session:
        user=session['user']
        return 'user successfully login Done! ' 
    else:
        return 'user session id expired'       

@app.route('/logout')
def logout():
    session.pop('user', None)
    return 'user logout successfully'


if __name__=='__main__':
    app.run(debug=True)


