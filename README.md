# Mildew Detection in Cherry Leaves - Image Recognition Project

## Dataset Content
* The dataset was obtained from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves), which served as the basis for a hypothetical user story demonstrating the application of predictive analytics in a real-world workplace project.
* Comprising over four thousand images from the client’s agricultural fields, the dataset showcases cherry leaves in healthy condition as well as those afflicted with powdery mildew. This fungal disease impacts a wide range of plants and is of particular concern for the cherry crop, a premium offering in the company’s product line. The potential delivery of substandard quality produce to the market is a significant concern for the company.

## Business Requirements
Farmy & Foods, a prominent player in the agricultural sector, approached us with a specific request: to design a Machine Learning-powered system capable of swiftly identifying powdery mildew in cherry trees. The system needed to analyze tree leaf images instantly, distinguishing between healthy and affected trees, thus indicating the necessity for fungicide treatment. This request arose from Farmy & Food's recognition of the inefficiency of their current manual detection process. With thousands of cherry trees distributed across numerous farms throughout the country, the manual inspection procedure was proving to be non-scalable due to its time-intensive nature.

### Business Requirement 1: Data Visualization

* The primary focus here was to provide the client with visually intuitive tools to differentiate between healthy and powdery mildew-affected cherry leaves.

- As a client, my priority is to effortlessly navigate an interactive dashboard, facilitating clear comprehension of the presented data.
- As a client, I require the display of "mean" and "standard deviation" images for both healthy and powdery mildew-infected cherry leaves, aiding in visual differentiation.
- As a client, I seek to visualize the disparity between an average healthy cherry leaf and one affected by powdery mildew, enhancing my ability to distinguish between the two.
- As a client, I aim to view an image montage featuring both healthy cherry leaves and those affected by powdery mildew, enabling easier visual differentiation.

### For further insights into the importance and functionality, refer to Hypothesis 1

Addressing these user stories involved the implementation of specific tasks, as detailed in the streamlit dashboard and Data Visualization notebook:

Development of a Streamlit-based dashboard with a user-friendly navigation sidebar (refer to Dashboard design for specifics).
Calculation and depiction of the distinction between average healthy and infected cherry leaves.
Visualization of "mean" and "standard deviation" images for both healthy and powdery mildew-infected leaves.
Creation of an image montage for comparative analysis of infected and healthy leaves.

### Business Requirement 2: Classification
This requirement centers on accurately identifying whether a given cherry leaf is infected with powdery mildew.

- As a client, I require an ML model capable of predicting leaf health with a minimum accuracy of 86%.

* To fulfill these user stories, the following tasks were undertaken, as showcased in the streamlit dashboard and Data Visualization notebook:

- Presentation of the rationale behind the deployed ML model, outlined here.
- Implementation of an uploader widget on the dashboard, enabling clients to upload cherry leaf images for instant evaluation.
- Specifications include uploading images in .jpeg format, supporting multiple uploads up to 200MB, and displaying uploaded images alongside their corresponding prediction statements. These statements indicate the presence of powdery mildew infection and associated probability.

## Hypothesis 
* 1 - It is anticipated that the visual distinctions between cherry leaves affected by powdery mildew and those that are not will be significant enough to effectively train an image-based machine learning model.
* 2 - According to a company’s internal analysis, manually inspecting a cherry tree for powdery mildew symptoms takes about 30 minutes. It is proposed that adopting image recognition technology could greatly reduce this time, thereby enhancing the company’s efficiency and making the detection process more scalable.
* 3 - Considering that the available dataset categorizes images into ‘infected’ and ‘uninfected’, it is advised that a binary classification approach would be most effective in differentiating between the two conditions in cherry leaves.

## Validation of Hypothesis
* 1 - The dataset will undergo analysis through testing, training, and validation methods to evaluate the accuracy of image recognition.
* 2 - The validation process will be visualized on the dashboard for easy review.
* 3 - The dashboard will feature functionality for uploading images to assess the presence of infection.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
* **Business Requirement 1**: Data Visualization 
    * We will display images that represent the “mean” and “standard deviation” for both infected and uninfected cherry leaves. This statistical analysis aims to visually articulate the differences between the two conditions.
    * We will display a side-by-side comparison to illustrate the distinction between an average infected leaf and an average uninfected leaf.
    * We will display a montage of images for either infected or uninfected leaves to provide a comprehensive visual overview.

* **Business Requirement 2**:  Classification
	* We aim to forecast whether a specific leaf is affected by powdery mildew or not. Our objective involves constructing a binary classifier and producing detailed reports.


## ML Business Case
* We aim to develop a machine learning model capable of predicting whether a leaf is infected with powdery mildew based on historical image data. This supervised model is designed as a 2-class, single-label classification model.

* Our goal is to provide Farmy Foods' team with a faster method for identifying powdery mildew infection in plants. The success criteria for the model include achieving an accuracy of 65% or higher on the test set.

* The model will output a flag indicating whether the leaf is infected with powdery mildew or not. Farm staff will continue their leaf inspection as usual, capturing leaf images via the app for on-the-fly predictions rather than batch processing.

* Currently, the process involves manual verification by employees spending approximately 30 minutes per cherry tree. They visually inspect leaf samples for signs of powdery mildew. By implementing image analysis, sample collection, and processing, this task can be expedited and potentially performed by staff with less expertise or even robotically at scale.

* The training data to fit the model come from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). This dataset contains about 4+ thousand images. 
	* Train data - target: infected or not; features: all images.


## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
* Quick project summary
	* General Information
		* Powdery mildew is a disease that affects both herbaceous and woody plants, often leading to reduced fruit yield in cherry trees.
        * Currently, the detection process involves manual verification by an employee who spends approximately 30 minutes per cherry tree. They collect leaf samples and visually inspect them for signs of powdery mildew.
        * According to the Connecticut Portal, powdery mildew is easily recognizable by the white, powdery growth of the fungus on infected parts of the plant. This growth results from the superficial spread of the fungus's thread-like strands (hyphae) across the plant surface, along with the production of chains of spores (conidia). Colonies of powdery mildew can vary in appearance, ranging from fluffy and white to sparse and gray.
	* Project Dataset
		* The available dataset contains 2104 out of +4 thousand images taken from images of infected leaves.
	* Link to additional information
	* Business requirements
		* The client is interested in conducting a study to visually distinguish between a healthy cherry leaf and one infected with powdery mildew..
		* The client is interested in developing a predictive model to determine whether a cherry leaf is healthy or infected with powdery mildew.

### Page 2: Infected Leaves Visualizer
* It will answer business requirement 1
	* Checkbox 1 - Difference between average and variability image
	* Checkbox 2 - Differences between average infected and average uninfected leaves.
	* Checkbox 3 - Image Montage

### Page 3: Powdery Mildew Detector
* Business Requirement 2 Information:
* The client aims to predict whether a cherry leaf is healthy or contains powdery mildew.
* Link to download a set of infected and uninfected leaves for live prediction.
* User Interface Specifications:
    * The user interface includes a file uploader widget enabling users to upload multiple leaf sample images.
    * Uploaded images are displayed alongside a prediction statement indicating whether the leaf is infected or not with powdery mildew, along with the associated probability.
    * Furthermore, a table is provided showing the image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation
* On this page, users can find the project hypotheses listed in the first section, followed by their validation in the section below. The page is purely text-based, so there are no user actions required for testing or validation.

### Page 5: ML Performance Metrics
* On this page, users can view dataset split metrics, performance metrics, model evaluation, training history, and loss and accuracy details.
    * Label Frequencies for Train, Validation and Test Sets
    * Model History - Accuracy and Losses
    * Model evaluation result

## Unfixed Bugs


# Mapping Business Requirements to Data Visualizations and ML Tasks

The alignment of business requirements with data visualizations and machine learning (ML) tasks involved a systematic approach, where each requirement was dissected into user stories and subsequently translated into corresponding ML tasks. It's noteworthy that thorough manual testing ensured the functionality of all tasks.

## Business Requirement 1: Data Visualization
The primary objective here was to provide the client with visual insights into distinguishing between cherry leaves affected by powdery mildew and healthy ones.

### User Stories:

Interactive Dashboard Navigation: Clients seek an intuitive interface to navigate effortlessly through the data.
Display of Mean and Standard Deviation Images: Visualization of statistical metrics aids in visually differentiating cherry leaves.
Comparison of Healthy and Infected Cherry Leaves: Clients require a clear depiction of the disparity between healthy and powdery mildew-infected cherry leaves.
Image Montage for Comparison: A visual montage facilitates the differentiation between healthy and infected cherry leaves.
For further insights into the importance and functionality of these features, refer to Hypothesis 1.

## Addressing these user stories involved the implementation of various tasks, which are showcased in a Streamlit dashboard and calculated within the Data Visualization notebook:

Development of a Streamlit-based dashboard featuring an intuitive sidebar for navigation.
Calculation and display of the difference between average infected and healthy leaves.
Visualization of mean and standard deviation images for both healthy and infected leaves.
Creation of image montages for comparison purposes.
Business Requirement 2: Classification
This requirement aimed at enabling the client to determine whether a given cherry leaf is affected by powdery mildew or not.


## Deployment
### Heroku

* The App live link is: https://mildew-detector-d-3e955bca296b.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.

### Languages
- [Python](https://www.python.org/)
- [Markdown](https://en.wikipedia.org/wiki/Markdown)


## Main Data Analysis and Machine Learning Libraries
- [Pandas](https://pandas.pydata.org/) - Used for data structuring and analysis.
- [Numpy](https://numpy.org/) - Provides mathematical functions to operate with and manipulate arrays.
- [Matplotlib](https://matplotlib.org/) - Used for data visualisation.
- [Seaborn](https://seaborn.pydata.org/#) - Used for statistical graphics, and the stuling of these using themes. 
- [Plotly](https://plotly.com/python/) - Used for plotting data and functions. 
- [Scikit-learn](https://scikit-learn.org/stable/index.html#) - Adopted tools for data processing and predictive analysis. used in this project speicicifically top train the ML Model for the binary classification output. 
- [Tensorflow](https://www.tensorflow.org/) - Used to process and clean the data to search for non-image files. 
- [Keras](https://keras.io/) - Used for the Classification model, and ML pipeline. The neural learning multi-layer network was built using Keras. 
- [Joblib](https://joblib.readthedocs.io/en/latest/) - Used for loading and saving files generated in the project. 
* [Pillow](https://pypi.org/project/Pillow/) - Python Imaging Library used for supporting opening, saving, and manipulating different images with its processing capabilities. 

### Version Control 

- Git - Used as a version control for this project. 
- [GitHub](https://github.com/) - The project repository stored here. 

### Development & Hosting

- [Jupyter Notebooks](https://jupyter.org/) - The main development source for running and executing the ML pipelines. 
- [Codeanywhere](https://codeanywhere.com/) - Used as the workspace and development environment for this project. 
- [Streamlit](https://streamlit.io/) - UI host for the dashboard.
- [Heroku](https://www.heroku.com/) - Used to deploy the project.


## Credits 

### Content 

* [Code Institute Malaria Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/): The project's code and design were adapted from the Malaria Detector walkthrough project, with minor changes for the Mildew Detector. The Malaria Detector project provided valuable guidance for machine learning, data analytics, and data visualization, particularly in real-world business-driven projects and neural network-based binary classification tasks.
* [Mildew Detection](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) was utilised as the base template for this project.
* [Streamlit Documentation](https://docs.streamlit.io/)
* Information for the text content for the 'Context' section on the Project Summary page came from [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew)


### Media

* The Images dataset for this project was sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).
* The UI for the app has been built using [Streamlit](https://streamlit.io/).

## Acknowledgements (optional)
* Thanks to my mentor Mo, Niel and Daisy for the support and help. 