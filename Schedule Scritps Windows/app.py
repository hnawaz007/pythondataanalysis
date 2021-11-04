from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import json
#
import pyodbc
import pandas as pd
from pretty_html_table import build_table
#

#
def get_data():
    # connect to database and query
    connection = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};" "Server=servername;" 
         "Database=AdventureWorksDW2012;"
         "UID=username;"
         "PWD=password;"
         "Trusted_Connection=no;")
    # read data from db
    df = pd.read_sql_query("select * FROM [AdventureWorks2012].[Sales].[vw_salesoverview] order by OrderDate", connection)
	#df = pd.read_excel("filename.xlsx")
    #
    # Filter out the dataframe
    df = df[(df['saleterritory'] == 'Central') & (df['Sales'] >= 20000)]
    df = df[['product', 'saleterritory', 'Sales']]
    # reset and drop index
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    # rename columns
    df.rename(columns={'product': 'Product', 'saleterritory': 'Sales Territory'}, inplace=True)
    # Formate the Sales column
    df['Sales'] = df['Sales'].apply(lambda x: f"${x:20,.0f}")
    df.to_excel("C:/Users/user/PycharmProjects/ScheduleScript/testfile.xlsx")
    # convert the dataframe to html table
    output = build_table(df, "blue_light", text_align="left")
    return output


def send_mail(body, sender, receiver, subject):
    # set up message details
    message = MIMEMultipart()
    message['Subject'] = sender
    message['From'] = receiver
    message['To'] = 'email@localmail.com'
    #Set body
    body_content = body
    message.attach(MIMEText(body_content, "html"))
    msg_body = message.as_string()
    # create server with credentials
    server = smtplib.SMTP('localhost')
    server.login(email, password)
    server.sendmail(sender, receiver, msg_body)
    #
    server.quit()

#
# get credentials from a config file
content = open("C:/Users/user/PycharmProjects/ScheduleScript/config/gmail.json")
config = json.load(content)
email = config['local']
password = config['pass']
#
sender = 'admin@localmail.com'
receiver = 'email@localmail.com'
subject = "Please find attached Central territory report"
# Call the function to get table
output = get_data()
# Call send mail with formatted table
send_mail(output, sender, receiver, subject)