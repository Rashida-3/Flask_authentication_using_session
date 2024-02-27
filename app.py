from flask import Flask ,request,session,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api

app=Flask(__name__)
# app.secret_key='login'

app.config['SECRET_KEY']='SUPER-SECRET-KEY'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'

db=SQLAlchemy(app)
api=Api(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))




@app.route('/register',methods=['POST'])
def register():
    data=request.get_json()
    username=data['username']
    password=data['password']

    if not username or not password:
        return {'msg': 'missing username or password'},400
    
    if User.query.filter_by(username=username).first():
        return {'msg': 'user already taken'},400
    
    new_user=User(username=username,password=password)
    db.session.add(new_user)
    db.session.commit()
    return {'msg': 'user created suceessfully'},200

@app.route('/login',methods=['GET'])
def login():
    data=request.get_json()
    username=data['username']
    password=data['password']
    user=User.query.filter_by(username=username).first()
    if user and user.password==password:
        session["user_id"]=user.id
        print(session)

    return {'msg':'okay'},200

@app.route('/cookies',methods=['GET'])
def setcookies():
    res=make_response("set a cookies")
    return res







# def login():
#     if request.method=='POST':
#         username=request.json['username']
#         password=request.json['password']

#         # print(username)

#         if username == 'rashida' and password == 1234 :
#             return ('login')

#         else: 
#             return('invalid')


        # if (username =="rashida" and password=="1234"):
        #     session['email']=username
        #     return "successful login"
        
        # else:
        #     'msg: invalid login'
    # return ('success')
        
        

if __name__ == '__main__':

    app.run(debug=True)