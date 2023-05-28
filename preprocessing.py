import re
import pandas as pd
def preprocessor(data):
    pattern = "\d{1,2}\/\d{2,4}\/\d{2,4},\s\d{1,2}:\d{1,2}\s\w{1,2}\s-\s"
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)
    user = []
    message = []

    for messages in df['user_message']:
        entry = re.split('([\w\W]+?):\s', messages)

        if entry[1:]:
            user.append(entry[1])
            message.append(entry[2])
        else:
            user.append("Group Notification")
            message.append(entry[0])

    df["user"] = user
    df["message"] = message
    df.drop(columns="user_message", inplace=True)
    df["year"] = df["date"].dt.year
    df["month_num"]=df["date"].dt.month
    df['only_date'] = df['date'].dt.date
    df["day_name"]=df['date'].dt.day_name()
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute

    return df