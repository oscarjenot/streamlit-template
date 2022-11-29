import os

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
if not AUTH0_CLIENT_ID and not AUTH0_DOMAIN:
    from dotenv import load_dotenv
    load_dotenv()
    AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
    AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")


class appConstants:
    # _______________ Authentification  _______________
    AUTH0_DOMAIN = AUTH0_DOMAIN
    AUTH0_CLIENT_ID = AUTH0_CLIENT_ID
    # _______________ Page attributes _______________
    PAGE_TITLE = "Streamlit Template"
    PAGE_ICON = "🤗"
    LAYOUT = "wide"
    # _______________ Global styles _______________
    # CSS classes options for more customization
    # Show or hide the main menu button on the top right or the 'Made with Streamlit' footer
    GLOBAL_STYLES = """
                <style>
                #MainMenu {visibility: visible;}
                footer {display: none !important;}
                header {visibility: hidden;}
                .block-container{
                    padding-top: 0px;
                }
                .example_css{
                    color: red;
                }
                </style>
                """
    # _______________ Title attributes _______________
    LOGO_URL = "https://docs.streamlit.io/logo.svg"  # imput any image url
    TITLE = "# Template Title"
    SUBTITLE = "  **Streamlit Template subtitle (use markdown)**"
    # _______________ About section attributes _______________
    ABOUT_INFO = """
    ### About this app
    - Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    - Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    - Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    """



