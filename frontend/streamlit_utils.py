import streamlit as st
from .constants import AppConstants
import auth0_component
from auth0_component import login_button
import base64


# _______________ Authentication _______________
def auth():
    """
    Use auth0-component to authenticate users
    """
    with st.sidebar:
        user_info = login_button(AppConstants.AUTH0_CLIENT_ID, domain=AppConstants.AUTH0_DOMAIN)
        st.info(
            "Access currently only available to XXXXXXX, XXXXXXXX, XXXXXXX domains, or upon special whitelist request. To register, click 'Login' button, then 'Sign Up' in the pop-up window. You must verify your email address before logging in. To change accounts, clear your browser cache."
        )

    if user_info and auth0_component.isAuth(user_info, domain=AppConstants.AUTH0_DOMAIN):
        return True
    else:
        st.info("Please login or register to access the app features.")
        return False


# _______________ Frontend Sections functions _______________
def page_config():
    st.set_page_config(
        page_title=AppConstants.PAGE_TITLE,
        page_icon=AppConstants.PAGE_ICON,
        layout=AppConstants.LAYOUT,
        initial_sidebar_state="auto",
    )
    st.markdown(AppConstants.GLOBAL_STYLES, unsafe_allow_html=True)


def title():
    # Title container
    with st.container():
        line()
        c1, e, c2 = st.columns([1, 0.1, 8])
        with c1:
            space(10)
            st.image(AppConstants.LOGO_URL, use_column_width=True)
        with c2:
            st.markdown(AppConstants.TITLE)
            st.markdown(AppConstants.SUBTITLE)
        line()


def about_section():
    # About this app
    with st.expander("ℹ️ About this app", expanded=False):
        st.write(AppConstants.ABOUT_INFO)
    space(20)


def thankyou():
    space(100)
    # Custom html / css class example
    st.markdown(
        """<div class="example_css"> Thank you for using our service !  </div>""",
        unsafe_allow_html=True,
    )


# _______________ Frontend layout functions _______________
def space(size=50):
    """Call space(<size>) to add spacing of <size> px in the page."""
    st.markdown(f"""<div style="padding-top: {size}px;"/>""", unsafe_allow_html=True)


def line():
    """Call line() to add a horizontal line"""
    st.markdown("""---""")


# _______________ Frontend layout functions _______________

def display_pdf(uploaded_pdf__file):
    """
    On streamlit, input the uploaded pdf from a st.file_uploader widget.
    Returns an iframe to display the pdf file on streamlit with:
    st.markdown(pdf_display, unsafe_allow_html=True)
    """
    if uploaded_pdf__file.type == 'application/pdf':
        base64_pdf = base64.b64encode(uploaded_pdf__file.getvalue()).decode('utf-8')
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width=100% height="1000" ' \
                      F'type="application/pdf"></iframe> '
        return pdf_display
    else:
        raise ValueError(
            "Please input a 'application/pdf' type object from Streamlit streamlit.runtime.uploaded_file_manager.UploadedFile object.")
