import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

st.set_page_config(layout="wide")

tab1, tab11, tab2, tab22, tab3, tab33, tab4, tab44, tab5, tab55, tab6, tab66, tab7 = st.tabs(
    ["Home", "      ", "About Me", "      ", "Portfolio", "      ", "Skills", "      ", "Experience & Education", "      ", "My CV",
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
                "I was selected to work as a Data Scientist in an exclusive team on a **_funded research project_** for the United Nations with the University of Aberdeen and I have achieved the following results as part of the analysis:")
            st.write(
                "* India achieved 25% improvement towards successful implementation of the United Nations Sustainable Development Goals (SDGs) because of the India Government’s flagship programmes.")
            st.write(
                "* The statistical analysis suggested that the indicator from SDG ‘Good Health and Well-being’ could prove to be a significant factor in the implementation of United Nations SDGs in India by 2030.")
            st.write(
                "Additionally, on the basis of my Masters final research-project results, I was hired as a Data Scientist to provide an insight on an internal project of University of Aberdeen and I have achieved the below result using NLP:")
            st.write(
                "* The qualitative analysis indicated that the awareness of the graduate attributes program should be raised with further improvements.")
            st.write(
                "Furthermore, I have close to 2 years of experience working as a DevOps Engineer within the Insurance industry in the UK and close to 5 years of experience working in the Operations and Software development in India.")
            st.write(
                "Overall I enjoy solving puzzles and to me, big data sets are one big puzzle I want to solve and the experiences gave me the ability to translate complex questions into understandable insights.")

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            img = Image.open('Mypicture.png')
            st.image(img, width=500)


with tab3:
    st.title("Portfolio")
    st.write("I have displayed below the visual representations I have created for different projects.")
    st.write("")
    st.subheader("Complex Interactions between 17 Sustainable Development Goals")
    st.write("The United Nations along with 193 Member States adopted the SDGs in September 2015 as a universal call to tackle some of the more pressing challenges facing the world today, by the year 2030. My research was to find the intra and inter-relations between all the Sustainable Development Goals for India.")
    st.write("The Network graph was plotted using the python's pyvis library where the indicators of the Sustainable Development Goals are the nodes whereas the connection between all the different indicators joining the nodes basis their correlation value are the edges. Each indicator is represented in the color of its goal which is similar to the United Nations color scheme used for the goals representation.")
    st.write("The graphs have been plotted using Pyvis, Streamlit and Networkx libraries. **_The graphs have zooming ability and the nodes display the details of the goal and its indicator on mouse hover; feel free to play with the graphs using physics displayed below the graphs._**")
    with st.container():
        st.write("")
        HtmlFile = open("SynergyGraph.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        components.html(source_code, height=1000)

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("Note: The below representation is the zoomed in view of the most betweeness central node from the above graph that acts as a bridge along the shortest path between two other nodes. On the basis of the Betweenness Centrality measure, the indicator from SDG ‘Good Health and Well-being’ could prove to be a significant factor in the implementation of the United Nations SDGs in India by 2030.")

    with st.container():
        st.write("")
        HtmlFile = open("Synergynode.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        components.html(source_code, height=1000)

    st.write("")
    st.write("")
    ##st.subheader("Survey Analysis on Graduate Attributes and Skills")
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        image_col, text_col = st.columns((1.5, 1.5))
        with image_col:
            img = Image.open("STcounts.png")
            st.image(img)
        with text_col:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write(
                "* The graphical representation shows that the Synergy (highly correlated) indicators count has increased by 25% across all the SDGs from the year 2015 to 2020 whereas there has been rise in the count of Trade-off (negatively correlated) indicators count for the year 2017-2018.")
            st.write("* The graph has been plotted using the Matplotlib library.")

    st.write("")
    st.write("")
    st.subheader("Survey Analysis on Graduate Attributes and Skills")
    st.write("The University of Aberdeen (UoA) 2040 strategy is a series of commitments that linked teaching and research graduating students to be ready to thrive in diverse workplaces of the future. UoA conducted a survey to understand the significance of the university's graduate attributes (the high level qualities and skills a student should gain, while at university) and I was hired as a Data Scientist to analyse the survey results and present the same to the university.")
    st.write("Natural Language Processing (NLP) model has been used to perform a qualitative analysis of the survey data, based on the responses from Staff, Students and External members. All the responses have been analysed to understand the impression of the respondents towards the Graduate Attributes.")
    with st.container():
        st.write("")
        st.write("")
        st.write("")
        image_col, text_col = st.columns((0.75, 1))
        with image_col:
            img = Image.open("Usefulness.png")
            st.image(img)
        with text_col:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("* The graph represents the usefulness of the graduate attributes acknowledged by all the respondents on the basis of the survey results.")
            st.write("* I have used the Plotly library to plot this sunburst chart.")

    with st.container():
        st.write("")
        st.write("")
        st.write("")
        image_col, text_col = st.columns((0.75, 1))
        with image_col:
            img = Image.open('WordCloud.png')
            st.image(img)
        with text_col:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("* The responses to the graduate attribute programme survey have been analysed based on all the comments.")
            st.write(
                "* The word cloud was generated to display the significant keywords from all the responses on the Graduate Attributes Programme.")

with tab4:
    st.title("Skills")
    skill_container = st.container()
    col1, col2 = st.columns([100, 90])
    img = Image.open('Skills.jpg')

    with skill_container:
        with col1:
            st.write("")
            st.write("* Data Analysis")
            st.write("* Data Visualization")
            st.write("* Machine Learning | Data Modelling | K-Means | K-Nearest Neighbour | Linear Regression | Logistic Regression | Decision Tree")
            st.write("* Statistics | T-test | Hypothesis testing | Time series modelling")
            st.write("* Audio, Video & Image Analysis")
            st.write("* DevOps | Microsoft Azure | AWS")
            st.write("* CI/CD | Puppet | Terraform | Atlassian Bamboo")
            st.write("* Python | R | Mathematica | Java")
            st.write("* NLTK | Spacy | Textacy")
            st.write("* Pandas | Numpy | Scikit-learn")
            st.write("* Networkx | Matplotlib | Plotly")
            st.write("* WordCloud | Pyvis | Streamlit | Seaborn")
            st.write("* GitHub | GIT | Bitbucket | Artifactory")
            st.write("* JIRA | Confluence | Splunk")
            st.write("* SQL")
        with col2:
            img = Image.open('Skills.jpg')
            st.image(img, width=500)
            st.caption("(Representational Image) Photo: iStock")

with tab5:
    st.header("_Academic Experience_")
    st.caption(
        "As part of the Master's degree, every student has to work on a final project; However, I was selected to be part of an exclusive team on a **_funded research project_** for the United Nations as my Master's final year project.")
    st.subheader("The Complex Interactions of the United Nations Sustainable Development Goals")
    st.caption("Jan 2022 - April 2022 | Aberdeen, UK")
    st.write(
        "* Investigated and contributed to the ongoing research activity of the TOSSIB project to find the complex interactions of the United Nations Sustainable Development Goals.")
    st.write(
        "* The Project was **_funded_** by the Royal Society to analyse the development of the United Nations 17 Sustainable Development Goals.")
    st.write(
        "* Performed quantitative data analysis on the indicators of the United Nations SDGs for country India and graphically represented the data using Python.")

    st.write("")
    st.header("_Professional Experience_")
    st.subheader("University of Aberdeen | Data Scientist")
    st.caption("April 2022 - May 2022 | Aberdeen, UK")
    st.write("* After presenting my Master's final research project & results, I was hired to provide insight into an internal project of the University of Aberdeen.")
    st.write("* UoA conducted a survey to understand the significance of the university's graduate attributes (the high level qualities and skills a student should gain as a result of the learning and experiences they engage with, while at university) and I was offered the role to analyse the survey results and present the same to the university.")
    st.write("* Performed sentiment analysis on qualitative data of the graduate attributes survey conducted by the University, to understand the usefulness and further improve the Graduate Attributes.")
    st.write(
        "* Implemented statistical analysis using NLP to measure the TF-IDF score to extract the keywords from the survey comments for representation in the word cloud.")

    st.subheader("Expleo Technology UK Ltd | Technical - DevOps Engineer")
    st.caption("July 2017 - April 2019 | London, UK")
    st.write("* Successfully deployed 20+ releases as part of the Agile team at Hiscox as a Consultant.")
    st.write(
        "* Built and maintained the CI/CD pipeline in PaaS architecture and ensured stability and security of 15 environments including Staging and Production to ensure that the distributed team across the globe can bring beneficial advancements to the client’s customers and insurance experts.")
    st.write("* Trained and mentored two juniors on DevOps tools and technologies.")
    st.write("* Troubleshooting applications and environment issues with root cause analysis.")

    st.subheader("Shree Sai Enterprises | Software Engineer")
    st.caption("April 2016 - Sep 2016 | Mumbai, India")
    st.write(
        "* Developed and unit-tested modules for updating medicine inventory for in-house inventory and sales system in a pharmaceutical firm as part of an Agile team.")
    st.write("* Developed interfaces in Java swing and wrote SQL queries to retrieve data.")
    st.write(
        "* Responsible for technical design, development and unit testing of modules for updating medicine inventory and purchase and sale receipts to local distributors.")

    st.subheader("Marsh & McLennan Companies | Senior Consultant")
    st.caption("Jan 2012 - Jan 2016 | Mumbai, India and London, UK")
    st.write(
        "* Successfully migrated the UK payroll system BenPal– automated payroll, employee benefits and pension benefits tool from the UK to India and worked for clients Royal London, Commerce Bank, Hitachi, The Perfume Shop, Vision Express and many more.")
    st.write(
        "* Provided ongoing support to the team in order to meet SLAs on Accuracy and productivity standards with internal/external stakeholders to ensure smooth and efficient deliveries.")
    st.write("* Mentored new hires and supported the team in cross-skilling and upskilling initiatives.")
    st.write("* Conducted regular refreshers to bridge the knowledge gap and regularly updated the process documentation.")
    st.write("* Rewarded STAR OF THE MONTH and EB Archer Award for excellent work performance.")

    st.write("")
    st.header("_Education_")
    st.subheader("University of Aberdeen | M.Sc. Data Science with Commendation")
    st.caption("Jan 2021 - July 2022 | Aberdeen, UK")
    st.subheader("University of Mumbai | B.Sc. Computer Science")
    st.caption("Aug 2008 - July 2011 | Mumbai, India")

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
