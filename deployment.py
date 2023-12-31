import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('trained_model.sav','rb'))

#creating a fucntion for prediction
def diabetes_prediction(input_data):
    #scaler=StandardScaler()
     # changing the input data to numpy array
    input_data_as_a_numpy_array=np.asarray(input_data)    # reshape the array as we are prediting
    input_data_reshaped=input_data_as_a_numpy_array.reshape(1,-1)
    #stnd_data=scaler.transform(input_data_reshaped)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==0):
         return 'The person is not diabetic'
    else:
        return ' The person is diabetic'

#def main():
     # giving a title
st.title('Diabetes prediction web app')
     # getting the input data from the user
Pregnancies=st.text_input('Number of pregnancies')
Glucose=st.text_input('Glucose level')
BloodPressure=st.text_input('Blood pressure value')
SkinThickness=st.text_input('Skin thickness level')
Insulin=st.text_input('Insulin level')
BMI=st.text_input('BMi value')
DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
Age =st.text_input('Age of the person')
   # code for prediction
diagnosis=' '
    
#      # creating a button for prediction
if st.button('Diabetest test result'):
    diagnosis=diabetes_prediction([Pregnancies,Glucose,                                 BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
st.success(diagnosis)       
    
#if __name__=='__main__ ':
   #  main()  # run from anaconda or command prompt



