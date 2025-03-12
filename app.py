%%writefile app.py
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("Product Recommendation System")

# User Input
product_index = st.number_input("Enter Product Index", min_value=0, step=1)

# Predict Button
if st.button("Recommend Similar Products"):
    def recommend_similar_products(product_index, top_n=5):
        similarity_matrix = model  # Assuming model.pkl contains similarity_matrix
        similar_indices = np.argsort(similarity_matrix[product_index])[::-1][1:top_n+1]
        return similar_indices

    recommendations = recommend_similar_products(product_index)
    st.write(f"Top similar products: {recommendations}")

