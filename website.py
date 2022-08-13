import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

st.set_page_config(layout="wide")

tab1, tab11, tab2, tab22, tab3, tab33, tab4, tab44, tab5, tab55, tab6, tab66, tab7 = st.tabs(
    ["Home", "      ", "About Me", "      ", "Portfolio", "      ", "Skills", "      ", "Experience", "      ", "My CV",
     "      ", "Contact"])

with tab1:
    title_container = st.container()
    col1, col2 = st.columns([90, 90])
    img = Image.open('Mypicture.png')
    with title_container:
        with col1:
            st.title("Akshata Ahire")
            st.subheader("Data Scientist")
            st.write(
                "Certified Scrum Master | Puppet Fundamentals trained | ISTQB Certified Tester | Oracle certified Java Professional")
        with col2:
            img = Image.open('Mypicture.png')
            st.image(img, width=500)

with tab2:
    title_container = st.container()
    col1, col2 = st.columns([90, 90])
    img = Image.open('Mypicture.png')

    with title_container:
        with col1:
            st.title("About Me")
            st.write(
                "Hi! I am Akshata, a Data Scientist. I hold a Master’s degree with Commendation in Data Science (University of Aberdeen, UK) and a Bachelor’s degree in Computer Science (University of Mumbai, India).")
            st.write(
                "I have worked as a Data Scientist on a research project for the United Nations with the University of Aberdeen and I have achieved the below results as part of the analysis:")
            st.write(
                "* India achieved 25% improvement towards successful implementation of the United Nations Sustainable Development Goals (SDGs) because of the India Government’s flagship programmes.")
            st.write(
                "* The statistical analysis suggested that the indicator from SDG ‘Good Health and Well-being’ could prove to be a significant factor in the implementation of United Nations SDGs in India by 2030.")
            st.write(
                "Additionally, whilst working as a Data Scientist for University of Aberdeen's graduate attributes program I achieved the following result using NLP:")
            st.write(
                "* The qualitative analysis indicated that the awareness of the graduate attributes program should be raised with further improvements.")
            st.write(
                "Overall I enjoy solving puzzles and to me, big data sets are one big puzzle I want to solve and the experiences gave me the ability to translate complex questions into understandable insights.")

        with col2:
            img = Image.open('Mypicture.png')
            st.image(img, width=650)
            
with tab3:
    st.title("Portfolio")
    st.write(
        "I have created the below representations for University's graduate attributes project and Masters project- Complex interactions between sustainable development goals.")
    st.subheader("Survey Analysis on Graduate Attributes and Skills")

    with st.container():
        image_col, text_col = st.columns((1.2, 2))
        with image_col:
            img = Image.open("Usefulness.png")
            st.image(img)
        with text_col:
            st.write(
                "The word cloud for every question was generated to display all the significant keywords from all the positive responses about the Graduate Attributes.")

    with st.container():
        image_col, text_col = st.columns((1.2, 2))
        with image_col:
            img = Image.open('WordCloud.png')
            st.image(img)
        with text_col:
            st.write(
                "The word cloud for every question was generated to display all the significant keywords from all the positive responses about the Graduate Attributes.")

    st.subheader("Complex Interactions between 17 Sustainable Development Goals")

    with st.container():
        HtmlFile = open("SynergyGraph.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        components.html(source_code, height=1000)


with tab4:
    skill_container = st.container()
    col1, col2 = st.columns([90, 90])
    img = Image.open('Skills.jpg')
    with skill_container:
        with col1:
            st.write("")
            st.write("* Python | R | Mathematica | Java")
            st.write("* Pandas | Numpy | Scikit-learn")
            st.write("* NLTK | Spacy | Textacy")
            st.write("* Networkx | Matplotlib | Plotly")
            st.write("* Seaborn | Pyvis | Streamlit")
            st.write("* Data Visualization")
            st.write("* Machine Learning")
            st.write("* Statistics")
            st.write("* Audio, Video & Image Analysis")
            st.write("* DevOps | Azure | AWS")
            st.write("* CI/CD | Github")
            st.write("* JIRA")
            st.write("* SQL")
        with col2:
            img = Image.open('Skills.jpg')
            st.image(img, width=500)
            st.caption("(Representational Image) Photo: iStock")

with tab5:
    st.header("_Academic Experience_")
    st.caption(
        "I received an opportunity to work on a funded project for United Nations as my Master's final year project")
    st.subheader("The Complex Interactions of the United Nations Sustainable Development Goals")
    st.caption("Jan 2022 - April 2022 | Aberdeen, UK")
    st.write(
        "* Investigated and contributed to the ongoing research activity of the TOSSIB project to find the complex interactions of the United Nations Sustainable Development Goals.")
    st.write(
        "* The Project was funded by the Royal Society to analyse the development of the United Nations 17 Sustainable Development Goals.")
    st.write(
        "* Performed quantitative data analysis on indicators of United Nations SDGs for country India using Python.")

    st.header("_Professional Experience_")
    st.subheader("University of Aberdeen | Data Scientist")
    st.caption("April 2022 - May 2022 | Aberdeen, UK")
    st.write("* Performed sentiment analysis on qualitative data to further improve the Graduate Attributes.")
    st.write(
        "* Implemented statistical analysis using TF-IDF score to extract the keywords from the feedback for representation in word cloud.")

    st.subheader("Expleo Technology UK Ltd | Technical - DevOps Engineer")
    st.caption("July 2017 - April 2019 | London, UK")
    st.write("* Successfully deployed 20+ releases as part of the Agile team at Hiscox as a Consultant.")
    st.write(
        "* Built and maintained the CI/CD pipeline in PaaS architecture and ensured stability and security of 15 environments including Staging and Production to ensure that the distributed team across the globe can bring beneficial advancements to the client’s customers and insurance experts.")
    st.write("* Trained and mentored two juniors on the DevOps tools and technologies.")
    st.write("* Troubleshooting applications and environment issues with root cause analysis")

    st.subheader("Shree Sai Enterprises | Software Engineer")
    st.caption("April 2016 - Sep 2016 | Mumbai, India")
    st.write(
        "* Developed and unit tested modules for updating medicine inventory for in-house inventory and sales system in a pharmaceutical firm as part of an Agile team.")
    st.write("* Developed interfaces in Java swing and wrote SQL queries to retrieve data.")
    st.write(
        "* Responsible for technical design, development and unit testing of modules for updating medicine inventory and purchase and sale receipts to local distributors.")

    st.subheader("Marsh & McLennan Companies | Senior Pensions Consultant")
    st.caption("Jan 2012 - Jan 2016 | Mumbai, India and London, UK")
    st.write(
        "* Successfully migrated UK payroll system BenPal– automated payroll, employee benefits and pension benefits tool from the UK to India and worked for clients Royal London, Commerce Bank, Hitachi, The Perfume Shop, Vision Express etc.")
    st.write(
        "* Provided ongoing support to the team in order to meet SLAs on Accuracy and productivity standards with internal/external stakeholders to ensure the smooth and efficient deliveries.")
    st.write("* Mentored new hires and supported the team in cross skilling and up skilling initiatives.")
    st.write("* Conducted regular refreshers to bridge the knowledge gap and regularly updated process documentations.")
    st.write("* Rewarded STAR OF THE MONTH and EB Archer Award for securing the Highest Accuracy score.")

with tab6:
    with open("Akshataresume.png","rb") as file:
        st.download_button(label="Download my CV", data=file, file_name="Akshataresume.png", mime="image/png")
    st.image("Akshataresume.png")

with tab7:
    contact_container = st.container()
    col1, col2 = st.columns([90, 90])
    img = Image.open("Email.png")

    with contact_container:
        with col1:
            st.write("")
            st.write("")
            st.header("_Say Hello!!_")
            st.write("")
            st.write("")
            st.markdown(
                '<a href="https://www.linkedin.com/in/akshata-a-020a3b11b/"><p style="font-family:sans serif; color:Blue; font-size: 20px;">LinkedIn</p></a>',
                unsafe_allow_html=True)
            st.write("")
            st.markdown(
                '<a href="mailto:akshata.aahire@gmail.com"><p style="font-family:sans serif; color:Blue; font-size: 20px;">Email me</p></a>',
                unsafe_allow_html=True)
            st.write("")
            st.markdown(
                '<a href="https://www.google.com/maps/@51.6238961,-0.4586808,8z"><p style="font-family:sans serif; color:Blue; font-size: 20px;">London, UK</p></a>',
                unsafe_allow_html=True)
        with col2:
            img = Image.open("Email.png")
            st.image(img, width=500)
            st.caption("(Representational Image) Photo: pngall")


#### Footer

def layout(*args):
    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 85px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=0.6
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(0.5)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in Python 3.10.6 with ❤️ by Akshata"
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()
