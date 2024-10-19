import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model

# Load the model
def load_dvd_price_model():
    try:
        model = load_model('dvd_rental_model.h5')
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Function to handle user input collection
def get_user_inputs():
    st.subheader("DVD Rental Details:")
    
    rental_duration = st.selectbox("Rental Duration", ["Select Rental Duration"] + [3, 4, 5, 6, 7])
    rental_rate = st.slider("Rental Rate", min_value=0.0, max_value=10.0, step=0.1)
    length = st.slider("Length of the Movie (in minutes)", min_value=45, max_value=185)
    replacement_cost = st.selectbox("Replacement Cost", ["Select Replacement Cost"] + [round(9.99 + i, 2) for i in np.arange(0, 21.01, 1.0)])
    rating = st.selectbox("Movie Rating", ["Select Rating"] + ['PG-13', 'NC-17', 'PG', 'R', 'G'])
    category = st.selectbox("Movie Category", ['Select Category'] + ['Horror', 'Documentary', 'New', 'Classics', 'Games', 'Sci-Fi', 'Foreign', 'Family', 'Travel', 'Music', 'Sports', 'Comedy', 'Drama', 'Action', 'Children', 'Animation'])
    status = st.selectbox("Rental Status", ['Select Status'] + ['Active', 'Not Active'])
    rental_month = st.selectbox("Rental Month", ['Select Rental Month'] + list(range(1, 13)))
    rental_day = st.slider("Rental Day", min_value=1, max_value=31)
    return_month = st.selectbox("Return Month", ['Select Return Month'] + list(range(1, 13)))
    return_day = st.slider("Return Day", min_value=1, max_value=31)
    
    # Collect inputs
    inputs = [rental_duration, rental_rate, length, replacement_cost, rating, category, status, rental_month, rental_day, return_month, return_day]
    return inputs

# Function to process inputs and check for missing values
def process_inputs(inputs):
    # Mapping categorical values to numerical
    if inputs[4] != "Select Rating":
        rating_map = ['PG-13', 'NC-17', 'PG', 'R', 'G']
        inputs[4] = rating_map.index(inputs[4])
    else:
        st.warning("Please choose a valid rating.")
        return None
    
    if inputs[5] != "Select Category":
        category_map = ['Horror', 'Documentary', 'New', 'Classics', 'Games', 'Sci-Fi', 'Foreign', 'Family', 'Travel', 'Music', 'Sports', 'Comedy', 'Drama', 'Action', 'Children', 'Animation']
        inputs[5] = category_map.index(inputs[5])
    else:
        st.warning("Please choose a valid category.")
        return None
    
    if inputs[6] != "Select Status":
        status_map = ['Active', 'Not Active']
        inputs[6] = status_map.index(inputs[6])
    else:
        st.warning("Please select rental status.")
        return None

    # Ensure all selections are valid
    if "Select" in str(inputs):
        st.warning("Please fill all fields correctly.")
        return None
    
    return list(map(float, inputs))

# Function to make the prediction and display the result
def predict_price(model, inputs):
    if model is not None:
        try:
            prediction = model.predict(np.array([inputs]))
            st.success(f"Estimated DVD Rental Price: ${round(prediction[0], 2)}")
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
    else:
        st.error("Prediction model not available.")

# Main function to structure the Streamlit app
def main():
    st.title("DVD Rental Price Prediction")
    
    # Load model
    model = load_dvd_price_model()

    # Sidebar with instructions
    st.sidebar.header("Instructions")
    st.sidebar.write("DVD rental to predict its price. The model uses various attributes like rental duration, movie length, and more to estimate the price.")

    # Collect inputs
    inputs = get_user_inputs()
    
    # Process inputs
    processed_inputs = process_inputs(inputs)
    
    # Prediction button
    if st.button("Estimate Price"):
        if processed_inputs:
            predict_price(model, processed_inputs)

if __name__ == "__main__":
    main()
