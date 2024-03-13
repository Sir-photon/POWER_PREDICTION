import streamlit as st
import pickle
import numpy as np 


def show_predict_page():
    st.title('Power Cosumption Prediction')

    st.write("""### We need some entry for your power cosumption prediction""")


    def load_model():
        with open('saved_steps.pkl', 'rb') as file:
            data = pickle.load(file)
        return data

    data=load_model()

    predictor_load=data['model']


    # Define all input values
    with st.form('Power consumption form'):
        st.write('Enter all power consumption data')
        Humidity=st.number_input('Enter Humidity value', value=None)
        Temperature=st.number_input('Enter Temperature value', value=None)
        Windspeed=st.number_input('Enter Windspeed value', value=None)
        GeneralDiffusion=st.number_input('Enter General Diffusion value', value=None)
        DiffuseFlows=st.number_input('Enter Diffuseflows value', value=None)

        # GEt the values into array:
        X=np.array([[Temperature, Humidity, Windspeed, GeneralDiffusion, DiffuseFlows]])
        X=X.astype(float)
        
        # Define button for the input data
        ok = st.form_submit_button('Calculate Power Consumption')
    if ok:
            # start prediction
        power_consumption=predictor_load.predict(X)
        return st.subheader(f'The estimated power consumption is {power_consumption[0]:.3f}Watts')
    
    threshold=1500 # Define energy threshold
    if power_consumption > threshold:
        st.write('Your energy consumption is high.')
    else:
        st.write('Normal active load.')

if __name__=="__main__":
    show_predict_page()

# Define button for the input data

# start prediction

