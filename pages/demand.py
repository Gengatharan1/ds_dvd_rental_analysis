from utils.components import form_input_x, prediction_page
import streamlit as st
from demand_model import demand_model as model
prediction_page(model['x_names'], '', '', model['y_name'])