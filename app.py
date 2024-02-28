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























# # from flask_sqlalchemy import SQLAlchemy

# app=Flask(__name__)
# # app.secret_key='login'

# # app.config['SECRET_KEY']='SUPER-SECRET-KEY'
# # app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'

# db=SQLAlchemy(app)
# api=Api(app)

# class User(db.Model):
#     id=db.Column(db.Integer, primary_key=True)
#     username=db.Column(db.String(100))
#     password=db.Column(db.String(100))




# @app.route('/register',methods=['POST'])
# def register():
#     data=request.get_json()
#     username=data['username']
#     password=data['password']

#     if not username or not password:
#         return {'msg': 'missing username or password'},400
    
#     if User.query.filter_by(username=username).first():
#         return {'msg': 'user already taken'},400
    
#     new_user=User(username=username,password=password)
#     db.session.add(new_user)
#     db.session.commit()
#     return {'msg': 'user created suceessfully'},200

# @app.route('/login',methods=['GET'])
# def login():
#     data=request.get_json()
#     username=data['username']
#     password=data['password']
#     user=User.query.filter_by(username=username).first()
#     if user and user.password==password:
#         session["user_id"]=user.id
#         print(session)

#     return {'msg':'okay'},200

# @app.route('/cookies',methods=['GET'])
# def setcookies():
#     res=make_response("set a cookies")
#     return res







# # def login():
# #     if request.method=='POST':
# #         username=request.json['username']
# #         password=request.json['password']

# #         # print(username)

# #         if username == 'rashida' and password == 1234 :
# #             return ('login')

# #         else: 
# #             return('invalid')


#         # if (username =="rashida" and password=="1234"):
#         #     session['email']=username
#         #     return "successful login"
        
#         # else:
#         #     'msg: invalid login'
#     # return ('success')
        
        

# if __name__ == '__main__':

#     app.run(debug=True)