import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    """Contents of Project Hypothesis"""
    st.write("### Project Hypothesis")
    st.info(
        f"1. It is posited that the disparity between images of Cherry leaves with and without powdery mildew "
        f"is sufficient to train a model using an image dataset.\n"
        f"2. An internal company review indicates that manual assessment of a Cherry tree for powdery mildew signs "
        f"takes 30 minutes. Implementing image recognition could significantly expedite this process, "
        f"enhancing the company's efficiency and scalability in mildew detection.\n"
        f"3. Given that the provided sample dataset categorizes images into infected and uninfected, "
        f"binary classification emerges as the optimal method for distinguishing between healthy and mildew-affected leaves."
    )