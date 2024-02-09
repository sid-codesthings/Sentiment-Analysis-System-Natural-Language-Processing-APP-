# We are referring to the code for a mobile phone review over here.
import streamlit as st
from google_auth_oauthlib.flow import InstalledAppFlow #for verification
from googleapiclient.discovery import build
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="Sentiment Analysis System",page_icon="https://cdn-icons-png.flaticon.com/512/9850/9850903.png")
st.title("SENTIMENT ANALYSIS SYSTEM")
st.sidebar.image("https://www.freecodecamp.org/news/content/images/2022/01/cover.jpg")
choice=st.sidebar.selectbox("My Menu",("HOME","Analyze Sentiment","Visualize the Results","CSV FILE"))
if(choice=="HOME"):
    st.image("https://uploads-ssl.webflow.com/5ebc4dae09fa971fce3e85a5/6132238846b8a0e52e357485_Screen%20Recording%202021-09-03%20at%2010.29.36.gif")
    st.markdown("<center><h1>WELCOME</h1></center>",unsafe_allow_html=True) # within markdown we wrote HTML code.
elif(choice=="Analyze Sentiment"):
    url=st.text_input("Enter Google Sheet URL")
    r=st.text_input("Enter Range")
    c=st.text_input("Enter Column")
    btn = st.button("Analyze")
    # We dont want to give permission again and again,
    # we want to do it just once, so using session state.    
    if(btn):
        if 'cred' not in st.session_state:
            f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
            st.session_state['cred']=f.run_local_server(port=0)
        mymodel=SentimentIntensityAnalyzer()
        service = build('Sheets','v4',credentials=st.session_state['cred']).spreadsheets().values()
        d = service.get(spreadsheetId=url,range=r).execute()
        mycolumns = d['values'][0]
        mydata = d['values'][1:]
        df = pd.DataFrame(data=mydata,columns=mycolumns)
        l=[]
        for i in range(0,len(df)):
            k = df._get_value(i,c)
            pred=mymodel.polarity_scores(k)
            if(pred['compound']>0.5):
                l.append("Positive")
            elif(pred['compound']<-0.5):
                l.append("Negative")
            else:
                l.append("Neutral")
        df['Sentiment'] = l
        st.dataframe(df)
        df.to_csv("Reviews_by_users3.csv",index=False) 
        st.header("This data has been saved by the name of Reviews_by_users3.csv")
elif(choice=='Visualize the Results'):
    choice2=st.selectbox("Choose Visualization",("None","Pie","Histogram"))# pie chart best for percentage,
    # Histogram best for categorical data and scatterplot for continuous data.
    if(choice2=="Pie"):
        # We will use the percentage code for it .
        df=pd.read_csv("Reviews_by_users3.csv")
        posper=len(df[df['Sentiment']=='Positive'])/len(df) * 100
        negper=len(df[df['Sentiment']=='Negative'])/len(df) * 100
        neuper=len(df[df['Sentiment']=='Neutral'])/len(df) * 100
        fig=px.pie(values=[posper,negper,neuper],names=['Positive','Negative','Neutral'])
        st.plotly_chart(fig)
    elif(choice2=="Histogram"): # for categorical values
        t=st.text_input("Use any categorical Column")
        if t:
            df=pd.read_csv("Reviews_by_users3.csv")
            fig=px.histogram(x=df['Sentiment'],color=df[t])
            st.plotly_chart(fig)
            
elif(choice=="CSV FILE"):
    path=st.text_input("Enter File Path")
    c=st.text_input("Enter Column")
    btn = st.button("Analyze")
    # We dont want to give permission again and again,
    # we want to do it just once, so using session state.    
    if(btn):
        if 'cred' not in st.session_state:
            f=InstalledAppFlow.from_client_secrets_file('key.json',['https://www.googleapis.com/auth/spreadsheets'])
            st.session_state['cred']=f.run_local_server(port=0)
        mymodel=SentimentIntensityAnalyzer()
        df = pd.read_csv(path)
        l=[]
        for i in range(0,len(df)):
            k = df._get_value(i,c)
            pred=mymodel.polarity_scores(k)
            if(pred['compound']>0.5):
                l.append("Positive")
            elif(pred['compound']<-0.5):
                l.append("Negative")
            else:
                l.append("Neutral")
        df['Sentiment'] = l
        st.dataframe(df)
        df.to_csv("Reviews_by_users3.csv",index=False) 
        st.header("This data has been saved by the name of Reviews_by_users3.csv")
 
    
