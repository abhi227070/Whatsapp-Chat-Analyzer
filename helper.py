import pandas as pd
from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import emoji
extract=URLExtract()

def fetch_stat(selected_user,df):
    #number of messages
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]
    num_msg=df.shape[0]

    #number of words
    words=[]
    for message in df["message"]:
        words.extend(message.split())
    num_word=len(words)

    #number of media files
    num_med=df[df["message"]=="<Media omitted>\n"].shape[0]

    #number of links
    links=[]
    for message in df["message"]:
        links.extend(extract.find_urls(message))

    return num_msg,num_word,num_med,len(links)

def most_busy(df):
    x=df["user"].value_counts().head()

    most=round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={"index":"name","user":"percentage"})

    return x,most

def creat_wordcloud(selected_user,df):
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]

    temp = df[df['user'] != "Group Notification"]
    temp = temp[temp['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']

    f = open("stop_hinglish.txt", "r")
    stop_words = f.read()
    words=[]
    def stop_word(message):
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
        return " ".join(words)
    wc=WordCloud(width=500,height=500,min_font_size=10,background_color="white")
    temp["message"]=temp["message"].apply(stop_word)

    df_wc=wc.generate(temp["message"].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user,df):
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]

    temp=df[df['user']!="Group Notification"]
    temp=temp[temp['message']!='<Media omitted>\n']

    f=open("stop_hinglish.txt","r")
    stop_words=f.read()

    words=[]

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    return_df=pd.DataFrame(Counter(words).most_common(20))

    return return_df

def emoji_count(selected_user,df):
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]
    em=[]

    for message in df["message"]:
        em.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])

    emoji_df=pd.DataFrame(Counter(em).most_common((len(Counter(em)))))

    return emoji_df

def monthly_timeline(selected_user,df):
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]
    timeline=df.groupby(['year','month_num','month']).count()["message"].reset_index()

    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+'-'+str(timeline['year'][i]))

    timeline['time']=time

    return timeline

def daily_timeline(selected_user,df):
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]

    d_timeline = df.groupby(['only_date']).count()["message"].reset_index()

    return d_timeline

def week_activity(selected_user,df):
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]

    return df['day_name'].value_counts()

def monthly_activity(selected_user,df):
    if selected_user!="Overall":
        df = df[df["user"] == selected_user]

    return df['month'].value_counts()


