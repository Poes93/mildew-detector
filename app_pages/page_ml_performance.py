import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate import load_test_evaluation


def page_ml_performance_metrics():
    """Contents of ML Metrics"""
    st.write("### ML Metrics")
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("## Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### F1 Test Score")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))

        # Generate and display model history plot
    st.write("## Model History")
    st.write("### Loss and Accuracy over Epochs")
    history_data = plt.imread(f"outputs/{version}/model_loss_acc.png")
    plt.figure(figsize=(8, 5))
    columns_to_plot = ['loss', 'val_loss', 'accuracy', 'val_accuracy']
    history_data[columns_to_plot].plot(ax=plt.gca(), style='.-')
    plt.xlabel('Epochs')
    plt.ylabel('Metrics')
    plt.title('Model Loss and Accuracy over Epochs')
    st.pyplot(plt)