import streamlit as st


def page_summary_body():
    """Contents of Exec Summary"""
    st.write("### Executive Summary")
    st.info(
        f"* Powdery Mildew is a fungal infection that affects both herbaceous and woody plants, "
        f"leading to reduced fruit production in cherry trees.\n"
        f"* Currently, the detection of powdery mildew on cherry trees is done manually.\n"
        f"* This involves an employee spending approximately 30 minutes per tree, collecting leaf samples "
        f"and visually inspecting them to determine the health of the tree and presence of powdery mildew.\n"
        f"* As noted by the Connecticut Agricultural Experiment Station, "
        f"powdery mildew is identifiable by the white, powdery fungal growth on the host plant. \n"
        f"* This growth is characterized by the fungus's superficial hyphae spreading across the plant surface "
        f"and the formation of spore chains (conidia), giving the colonies a range from fluffy white to sparse gray."
    )