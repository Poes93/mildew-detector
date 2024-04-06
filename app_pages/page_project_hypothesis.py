import streamlit as st


def page_project_hypothesis_body():

    st.header("Mildew Detection in Cherry Leaves Hypotheses and Validation")

    st.subheader(
        f"There are 4 main hypotheses for this project:")
    st.info(
        f"1) Cherry leaves infected with powdery mildew have white spots or areas on the leaf surface, or plant stems. \n\n"
        f"2) The powdery mildew infection gradually spreads, eventually covering the plant in a white powdery/fuzzy appearance all over. \n\n"
        f"3) This distinct appearance of an infected plant should be enough to train an ML model to detect and predict the presence of powdery mildew on new leaf image data. This can help the client reduce time and labour costs associated with manual detection. \n\n"
        f"4) The ML model will be able to distinguish between a healthy cherry leaf and one infected with powdery mildew, with an accuracy of at least 97%. \n\n"
    )

    st.success(
        f"**Project Hypotheses Validation**\n\n"

        f"- Visual evidence confirms that cherry leaves infected with powdery mildew exhibit a lighter coloration/white patchy appearance and more deformed edges compared to healthy leaves. \n\n"
        f"- An image montage effectively showcases the visual distinction between healthy and infected leaves within this project. \n\n"
        f"- The ML application successfully differentiates between healthy cherry leaves and those infected with powdery mildew. \n\n"
        f"- The Mildew Detector achieves at least a 97% accuracy level on new data, as validated through the training and validation stages of the model development process. \n\n"
        f"- A comprehensive evaluation of the ML pipeline's performance can be found on the 'ML Performance Metrics' page. \n\n"
        f"- For image montages comparing healthy and infected leaves, please navigate to the 'Cherry Leaf Visualiser' page in the menu sidebar. "
    )