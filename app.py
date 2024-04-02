import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary import summary_body
from app_pages.leaves_visualizer import leaves_visualizer_body
from app_pages.mildew_detector import powdery_mildew_detector_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.ml_performance import ml_performance_metrics

app = MultiPage(app_name="Cherry Powdery Mildew detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaves Visualiser", page_leaves_visualizer_body)
app.add_page("Powdery Mildew detector", page_powdery_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()  # Run the app