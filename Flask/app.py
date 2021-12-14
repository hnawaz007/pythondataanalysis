from flask import Flask, url_for, redirect, render_template,request
import pickle

#create an instance of flask
app = Flask(__name__)


#create a base route
@app.route('/')
def home():
    prediction = request.args.get('prediction')
    return render_template('home.html', prediction=prediction)

#predict route
@app.route('/predict', methods=["POST","GET"])
def predict():
    if request.method == 'POST':
        budget = request.form['budget']
        print(budget)
        # Let's load the package
        model = pickle.load(open('simple_linear_regression.pkl', 'rb'))
        prediction = model.predict([[budget]])
        prediction = int(prediction[0])
        return redirect(url_for('home',
                prediction='Predicted Sales Amount: {}Millions'.format(prediction)))

if __name__ == '__main__':
    app.run(debug=True)