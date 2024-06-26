import streamlit as st


DEMO_URL = 'https://youtu.be/qIFdCHsppTo'

def st_demo():
    st.subheader('Demo', divider=True)
    with st.expander('Show/Hide', expanded=True):
        st.video(DEMO_URL)

def st_model():
    st.subheader('Model', divider=True)
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            At the core of this project is a Tensorflow image-classification
            neural network based on the EfficientNetB0 architecture, trained on
            a subset of the
            [BIRDS 525 SPECIES - IMAGE CLASSIFICATION dataset](https://www.kaggle.com/datasets/gpiosenka/100-bird-species)

            Rather than scale the training dataset up to balance the dataset,
            I only took 25 images per species. This allowed me to train several
            models until they stopped learning in a few days and on a single
            personal computer, whereas a few epochs of a single model would
            take just as long using the full training dataset while not greatly
            improving performane. The models' hyperparameters were chosen with
            Bayesian optimization via Hyperopt.
        """)

def st_deployment():
    st.subheader('Deployment', divider=True)
    with st.expander('Show/Hide', expanded=True):
        st.markdown("""
            Once I had a model I was content with, I deployed it as follows:
            1. I made an API for the model with FastAPI.
            2. I containerized the model, its API, and their minimal
               environment with Docker, and pushed the image to Dockerhub.
            3. I made this frontend with Streamlit, containerized it, and
               pushed it to Dockerhub.
            4. I ran both containers using Docker compose on an AWS EC2
               instance and configured it to accept and forward HTTP requests
               to the Streamlit app.
        """)

def st_exec_summary():
    st.markdown(
        """
        This project is an exercise in machine learning (ML) development
        with limited computing resources and ML operations (MLOps).
        Below are summaries of this project's components.\n
        [E-mail](mailto:juan.m.lazaro.ruiz@gmail.com) to schedule a live demo.
        """
    )

def st_all():
    st.header(':penguin: Bird Class :student:')
    st_exec_summary()
    st.subheader('Contents', divider=True)
    st.markdown(
        '#### 1. [Demo](#demo)\n'
        '#### 2. [Model](#model)\n'
        '#### 3. [Deployment ](#deployment)\n',
        unsafe_allow_html=True
    )
    st_demo()
    st_model()
    st_deployment()
