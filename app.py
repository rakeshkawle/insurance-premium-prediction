from flask import Flask,jsonify ,request
import pandas as pd
import pickle
print('sucesse_1')

#Create Falsk app
app=Flask(__name__)
print('sucesse_2')


# Load the trained machine learning model
with open('model.pkl','rb') as f:
    model = pickle.load(f)
print('sucesse_3')


# Define an endpoint to receive input data and return predictions
@app.route('/prediction',methods=["POST"])



# used for writting functions

def details():
    data=request.get_json()
    age=data['age']
    sex=data['sex']
    bmi=data['bmi']
    children=data['children']
    smoker=data['smoker']
    region=data['region']
    print('sucesse_5')

    # defining function
    def cnvt_1(sex):
        if sex=='male':
            return 1
        else:
            return 0
    sex=cnvt_1(sex)

    def cnvt_2(smoker):
        if smoker=='yes':
            return 1
        else:
            return 0
    smoker=cnvt_2(smoker)

    def cnvt_3(region):
        if region=='southeast':
            
            return 1
        elif region=='southwest':
            
            return 2
        elif region == 'northwest':
            
            return 3
        else:
            
            return 4
    region=cnvt_3(region)
    print('sucesse_6')

    test_df=pd.DataFrame({'age':[age], 'sex':[sex], 'bmi':[bmi], 'children':[children], 'smoker':[smoker], 'region':[region]})
    prediction_expense=model.predict(test_df)
    print('sucesse_7')

    return jsonify({'Prediction_Premiun':prediction_expense.tolist()})


if __name__ == "__main__":
        app.run(debug=True)