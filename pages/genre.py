from utils.components import form_input_x, prediction_page
import streamlit as st
from genre_model import genre_model as model
prediction_page(model['x_names'], '', '', model['y_name'])