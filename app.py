import streamlit as st

st.header('Throw a coin')

number_of_trials = st.slider('Number of Attempts?', 1, 1000, 10)

start_button = st.button('Execute')

if start_button:
	st.write(f'Experiment with {number_of_trials}' ongoing trials.)

st.write('This app is not functional yet')



