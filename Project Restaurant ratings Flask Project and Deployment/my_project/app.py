import numpy as np
from flask import Flask, request, jsonify, render_template        # flask is used for deployment
import pickle

# creating flask
app = Flask(__name__)
# loading the pickle file - contain model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')                      # html file - index


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [int(x) for x in request.form.values()] # fetch value which user enter in the index form
    final_features = [np.array(features)]              # creating array of those values
    prediction = model.predict(final_features)         #  prediction
                                                       # final_features is input (i.e independent variables)
    output = round(prediction[0], 1)

    return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)