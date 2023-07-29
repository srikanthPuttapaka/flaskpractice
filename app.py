from flask import Flask,request,render_template

obj= Flask(__name__)


@obj.route('/')
def welcome():
    return "Welcome to the Flask"

@obj.route('/cal',methods =["GET","POST"])
def math_operation():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation== "add":
        result=number1+number2
    elif operation=="multiply":
        result=number1*number2
    elif operation=="sub":
        result=number1-number
    else:
        result= number1/number2
    return result

print(__name__)
if __name__ == '__main__':
    obj.run(debug=True)