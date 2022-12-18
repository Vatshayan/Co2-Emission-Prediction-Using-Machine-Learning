from flask import Flask,render_template,request
import pickle


app=Flask(__name__)
file=open('model.pkl','rb')

regr=pickle.load(file)
file.close()
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        myDict=request.form
        engine=float(myDict['Engine'])
        input_size = [engine]
        test_y_ = regr.predict([input_size])[0][0]
        #print(test_y_)
        return render_template('result.html',EMI=round(test_y_))
    return render_template('index.html')
    #return 'HEllo World'+str(test_y_)
if __name__=='__main__':
    app.run(debug=True)
