import streamlit as st
# Import layout functions and templates for streamlit
from frontend import streamlit_utils
# Connection to the backend
from backend import pipeline


# Streamlit Documentation https://docs.streamlit.io/


# Cache and Singleton (Storing data / models / in cache) Only use for large files of computations
@st.experimental_memo  # @st.experimental_singleton
def hello():
    return pipeline.hello_streamlit()


def render():
    streamlit_utils.title()  # Title
    streamlit_utils.about_section()  # About section
    # Loading data
    hello_world = hello()  # Stored in cache (@st.experimental_memo)

    # ___________________ WITH TABS___________________
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])  # Remove this line and the 'with tab1/2' for a one tab page
    with tab1:
        st.write(hello_world)
    with tab2:
        st.write("This is a new tab...")

    streamlit_utils.thankyou()  # Custom HTML / CSS Example


def main():
    # Page configuration
    streamlit_utils.page_config()

    # # TODO: Uncomment when Auth0 component is ready or remove if you don't need authentication
    # is_user_authenticated = streamlit_utils.auth()
    # if is_user_authenticated:
    #     render()
    # else:
    #     st.stop()

    render()  # TODO: Remove and uncomment above when Auth0 component is ready


if __name__ == "__main__":
    main()
