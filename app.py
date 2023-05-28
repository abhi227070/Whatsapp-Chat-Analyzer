#importing the dependencies
import streamlit as st
import preprocessing,helper
import matplotlib.pyplot as plt
import requests
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu

#setting page configuration
st.set_page_config(page_title="Whatsapp Chat Analyzer",page_icon=":wave:",layout="wide")

#creating fuction to access lottie files
def lottie_url(url):

    r=requests.get(url)

    if r.status_code != 200:
        return None
    return r.json()

lottie_code=lottie_url("https://assets10.lottiefiles.com/packages/lf20_iv4dsx3q.json")
lottie1_code=lottie_url("https://assets2.lottiefiles.com/private_files/lf30_wyrwqyr9.json")
lottie2_code=lottie_url("https://assets6.lottiefiles.com/packages/lf20_ryosrokc.json")

@st.cache(allow_output_mutation=True)

def ob():
    pass

#Making the option menu at sidebar
with st.sidebar:
    selected = option_menu('Whatsapp chat analysis',
                           ['Home', 'Whatsapp chat analyser', 'Contact Us'],
                           icons=['house', 'whatsapp', 'cast'], default_index=0)

# Making the home page    
if selected =="Home":
    #st.markdown("<h2 style='text-align: center;'>Whatsapp Chat Analyzer</h2>",unsafe_allow_html=True)
    st.title("Whatsapp Chat Analyzer")
    #st.markdown('''<div style="border: 2px solid rgb(255, 249, 249);
    #background-color: rgb(103, 211, 61);
    #border-radius: 8px;
    #margin: 10px;
    #padding: 20px;
    #font-family: 'Open Sans', sans-serif;
    #color: white;
    #width: 500px;
    #text-align: center;
    #font-size: 30px;">
    #    <h2>Whatsapp Chat Analyser</h2>
    #</div>''',unsafe_allow_html=True)

    # writing the content like description, key point in the home page
    st.write("---")
    st.header("Description: WhatsApp Chat Analyzer using Machine Learning and NLP")
    st.write(''' 

The WhatsApp Chat Analyzer is a project that leverages machine learning and natural language processing techniques to analyze chat data from WhatsApp conversations. By applying advanced algorithms, the project aims to extract meaningful insights from the chat data, enabling users to gain valuable information and understand various aspects of the conversation.''')

    with st.container():

        st.write("---")
        st.header("Key Features:")
        left_column,right_column=st.columns(2)
        with left_column:

            st.write('''
            Data Extraction: The project extracts the chat data from WhatsApp, capturing information such as message content, timestamps, sender information, and any other relevant metadata.Data Preprocessing: The extracted chat data undergoes preprocessing steps to clean and transform the text, including removing irrelevant information, handling special characters, and tokenizing the messages into individual words or phrases.

            NLP Analysis: The preprocessed chat data is then subjected to NLP techniques, such as sentiment analysis, topic modeling, named entity recognition, or text classification, depending on the specific goals of the project.

            Data Representation: The analyzed data is organized and represented in a structured format, typically using a dataframe, where each row represents a message and each column contains relevant information, such as sender, timestamp, sentiment score, topic label, or other derived features.

            Visualization: To enhance the interpretability of the results, the project utilizes graphical representations, including charts, graphs, and plots, to visually depict patterns, trends, and key insights derived from the chat data analysis.
            ''')

        with right_column:
            st_lottie(lottie_code, height=350, key="code")

    with st.container():
          st.write("---")
          st.header("Potential Use Cases:")
          left_column,right_column=st.columns(2)
          with left_column:
               st_lottie(lottie2_code,height=300,key="android")

        

          with right_column:
               st.write('''
               Sentiment Analysis: Analyzing the overall sentiment of the chat to identify positive, negative, or neutral tones throughout the conversation.
               
               Topic Modeling: Identifying the main topics discussed in the chat and visualizing their distribution.

               User Interaction Analysis: Examining the frequency and patterns of communication between different participants.

               Keyword Extraction: Identifying frequently used keywords or phrases in the chat.

               Trend Analysis: Analyzing chat activity over time to detect spikes, lulls, or other patterns.
               ''')
               
          st.write("By employing machine learning and NLP techniques, the WhatsApp Chat Analyzer project enables users to gain a deeper understanding of their chat data, facilitating data-driven decision-making, sentiment monitoring, trend analysis, and other valuable insights from WhatsApp conversations.")

          st.write("---")

          st.write(''' It is designed to provide analytical insights from WhatsApp chat data using machine learning and natural language processing techniques. The project is for informational and educational purposes only and should not be considered as professional advice.
                    It is designed to provide analytical insights from WhatsApp chat data using machine learning and natural language processing techniques. The project is for informational and educational purposes only and should not be considered as professional advice.
                    For any inquiries or feedback regarding the WhatsApp Chat Analyzer project, please contact us by clicking contact us button present in sidebar.
                    Disclaimer: The WhatsApp Chat Analyzer project is not affiliated with or endorsed by WhatsApp Inc. WhatsApp is a registered trademark of WhatsApp Inc.''')
          
          st.markdown('''<nav class="navbar">
        <ul style="margin: 3px;
        padding-left: 250px;">
            <li style="float: left;
            list-style: none;
            border-radius: 8px;
            margin: 20px;
            padding: 20px;
            font-family: 'Open Sans', sans-serif;
            color: rgb(255, 255, 255);
            width: 150px;
            text-align: center;
            font-size: 10px;">Privacy Policy</li>
            <li style="float: left;
            list-style: none;
            border-radius: 8px;
            margin: 20px;
            padding: 20px;
            font-family: 'Open Sans', sans-serif;
            color: rgb(255, 255, 255);
            width: 150px;
            text-align: center;
            font-size: 10px;">Terms and condition</li>
            <li style="float: left;
            list-style: none;
            border-radius: 8px;
            margin: 20px;
            padding: 20px;
            font-family: 'Open Sans', sans-serif;
            color: rgb(255, 255, 255);
            width: 150px;
            text-align: center;
            font-size: 10px;">Copyright</li>
        </ul>
    </nav>''',unsafe_allow_html=True)

# Making the whatsapp chat analyser part for data analysis
if (selected=="Whatsapp chat analyser"):
     
     st.title("Welcome to whatsapp chat analysis part")
     st.header("Follow the steps:")
     st.write('''
     1.Open Whatsapp on your mobile or pc and open the whatsapp chat of single user or whatsapp group.

     2.Click on 3 dot present in right-top.

     3.Select More -> Export Chat -> Without media.

     4.Download that file.

     5.Upload that file below.

     6.Select the user (In group chat where multiple users are present)
     
     7.Click on Show Analysis''')

     st.markdown('''<div style="border: 2px solid rgb(255, 249, 249);
     background-color: rgb(210, 63, 63);
     border-radius: 8px;
     margin: 5px;
     padding: 20px;
     font-family: 'Open Sans', sans-serif;
     color: white;
     width: 500px;">
        <h4>Note:</h4>
        <p>This may take few minutes to load and show output.</p></div>''',unsafe_allow_html=True)
     
     #creating the file uploader section
     st.header("Choose the File")
     uploaded_file = st.file_uploader("")
     if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        data=bytes_data.decode("utf-8")

        df=preprocessing.preprocessor(data)

        user_list=df["user"].unique().tolist()
        user_list.remove("Group Notification")
        user_list.sort()
        user_list.insert(0,"Overall")

        selected_user=st.selectbox("Select the user",user_list)
        
        #creating the button for result
        if st.button("Show Analysis"):
            with st.spinner("Loading ..."):
                # Showing top statistics
                st.title("Top Statistics")
                num_msg,num_word,num_med,num_links=helper.fetch_stat(selected_user,df)

                col1,col2,col3,col4=st.columns(4)

                with col1:
                    st.header("Total Messages")
                    st.title(num_msg)
                with col2:
                    st.header("Number of words")
                    st.title(num_word)
                with col3:
                    st.header("Media Shared")
                    st.title(num_med)
                with col4:
                    st.header("Link Shared")
                    st.title(num_links)

            #monthly timeline
            with st.spinner("Loading ..."):
                st.title("Monthly Timeline")
                timeline=helper.monthly_timeline(selected_user,df)
                fig,ax=plt.subplots()
                ax.plot(timeline['time'],timeline['message'],color='green')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            #daily timeline
            with st.spinner("Loading ..."):
                st.title("Daily Timeline")
                d_timeline=helper.daily_timeline(selected_user,df)
                fig,ax=plt.subplots()
                ax.plot(d_timeline['only_date'],d_timeline['message'],color="black")
                plt.xticks(rotation="vertical")
                st.pyplot(fig)

            #activity map
            with st.spinner("Loading ..."):
                st.title("Activity Map")
                col1,col2=st.columns(2)
                with col1:
                    st.header("Most busy day")
                    busy_day=helper.week_activity(selected_user,df)
                    fig,ax=plt.subplots()
                    ax.bar(busy_day.index,busy_day.values,color="brown")
                    st.pyplot(fig)
                with col2:
                    st.header("Most busy month")
                    busy_month=helper.monthly_activity(selected_user,df)
                    fig,ax=plt.subplots()
                    ax.bar(busy_month.index,busy_month.values,color="orange")
                    plt.xticks(rotation="vertical")
                    st.pyplot(fig)

            #Most busy user
            with st.spinner("Loading ..."):
                if selected_user=="Overall":

                    st.title("Most Busy user")

                    col1,col2=st.columns(2)
                    x,new_df=helper.most_busy(df)
                    fig,ax=plt.subplots()

                    with col1:
                        ax.bar(x.index,x.values,color="red")
                        plt.xticks(rotation="vertical")
                        st.pyplot(fig)
                    with col2:
                        st.dataframe(new_df)
            #Word cloud
            with st.spinner("Loading ..."):
                st.title("Word Cloud")
                df_wc=helper.creat_wordcloud(selected_user,df)
                fig,ax=plt.subplots()
                ax.imshow(df_wc)
                st.pyplot(fig)

            #most common words
            with st.spinner("Loading ..."):
                st.title("Most common Words")
                most_common_words=helper.most_common_words(selected_user, df)

                plt.figure(figsize=(12,8))
                fig, ax = plt.subplots()

                ax.barh(most_common_words[0], most_common_words[1])
                st.pyplot(fig)

            #emoji count
            with st.spinner("Loading ..."):
                st.title("Emojis Used:")
                emoji_df=helper.emoji_count(selected_user,df)
                if emoji_df.empty:
                    st.header("No emoji found")
                else:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.dataframe(emoji_df)
                        st.markdown('''<div style="border: 2px solid rgb(255, 249, 249);
     background-color: rgb(210, 63, 63);
     border-radius: 8px;
     margin: 5px;
     padding: 20px;
     font-family: 'Open Sans', sans-serif;
     color: white;
     width: 500px;">
        <p>Note:<p>
        <p>Some emojis may not shown in the pie chart ,this is because some are not supported with matplotlib.</p></div>''',unsafe_allow_html=True)
                    with col2:
                        fig, ax = plt.subplots()
                        ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f")
                        st.pyplot(fig)
     




   
#creating a function to import css style file
def local_css(filename):
	with open(filename) as f:
		st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style\style.css")

# Making the contact us page
if selected=="Contact Us":
    with st.container():
        #defining the contact form
        st.header("Get in contect with me")

        contact_form="""<form action="https://formsubmit.co/abhijeetmaharana77@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your e-mail" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
        </form>"""

        left_column,right_column=st.columns(2)

        with left_column:
            st.markdown(contact_form,unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie1_code,height=300,key="thanks")
            
        


    #Writing the term condition in footer part only for style purpose(dummy type)
    with st.container():
        st.write("---")
        st.write("##")

        col1,col2,col3 = st.columns(3)

        with col1:
            st.write("2023 © Whatsapp Chat Analysis | All Rights Reserved.")
        with col3:
            st.write("      Privacy Policy")
            st.write("      Terms and Conditions")
            st.write("      Copyright")
     








