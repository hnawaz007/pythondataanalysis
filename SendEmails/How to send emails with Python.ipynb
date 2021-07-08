{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "adjusted-little",
   "metadata": {},
   "outputs": [],
   "source": [
    "from email.mime.text import MIMEText\n",
    "from email.mime.application import MIMEApplication\n",
    "from email.mime.multipart import MIMEMultipart\n",
    "from email.mime.base import MIMEBase\n",
    "from email.message import EmailMessage\n",
    "from email import encoders\n",
    "import smtplib\n",
    "import os\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "radio-struggle",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyodbc\n",
    "import pandas as pd\n",
    "from pretty_html_table import build_table\n",
    "import io"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "subsequent-butter",
   "metadata": {},
   "outputs": [],
   "source": [
    "content = open('config/gmail.json')\n",
    "config = json.load(content)\n",
    "email = config['local']\n",
    "password = config['pass']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "colored-powell",
   "metadata": {},
   "outputs": [],
   "source": [
    "sender = 'admin@localmail.com'\n",
    "receiver = 'hnawaz@localmail.com'\n",
    "subject = \"Top 5 Economies of the world\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "competitive-holder",
   "metadata": {},
   "outputs": [],
   "source": [
    "message = f\"\"\"From: From <{sender}>\n",
    "To: To <{receiver}>\n",
    "MIME-Version: 1.0\n",
    "Content-type: text/html\n",
    "Subject: {subject}\n",
    "\n",
    "This is an e-mail message to be sent in HTML format\n",
    "\n",
    "<b>This is HTML message.</b>\n",
    "<h1>This is headline.</h1>\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "recreational-visit",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{}"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "server = smtplib.SMTP('localhost')\n",
    "server.login(email, password)\n",
    "server.sendmail(sender, receiver, message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "incorporate-production",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_gdp_data():\n",
    "    \"\"\"\n",
    "    GDP data\n",
    "    :return:\n",
    "    \"\"\"\n",
    "    gdp_dict = {'Country': ['United States', 'China', 'Japan', 'Germany', 'India'],\n",
    "                'GDP': ['$21.44 trillion', '$14.14 trillion', '$5.15 trillion', '$3.86 trillion', '$2.94 trillion']}\n",
    "    data = pd.DataFrame(gdp_dict)\n",
    "    return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "intensive-watts",
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_mail(body):\n",
    "    \n",
    "    message = MIMEMultipart()\n",
    "    message['Subject'] = 'Top 5 Economies of the World!'\n",
    "    message['From'] = 'admin@localmail.com'\n",
    "    message['To'] = 'hnawaz@localmail.com'\n",
    "    \n",
    "    body_content = body\n",
    "    message.attach(MIMEText(body_content, \"html\"))\n",
    "    msg_body = message.as_string()\n",
    "    \n",
    "    server = smtplib.SMTP('localhost')\n",
    "    server.login(email, password)\n",
    "    server.sendmail(sender, receiver, msg_body)\n",
    "    #\n",
    "    server.quit()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "antique-crash",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = get_gdp_data()\n",
    "data\n",
    "output = build_table(data, \"blue_light\")\n",
    "send_mail(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "polyphonic-relay",
   "metadata": {},
   "outputs": [],
   "source": [
    "connection = pyodbc.connect(\"Driver={SQL Server Native Client 11.0};\"\n",
    "                      \"Server=serverName;\"\n",
    "                      \"Database=AdventureWorksDW2012;\"\n",
    "                      \"Trusted_Connection=yes;\"\n",
    ")\n",
    "\n",
    "df = pd.read_sql_query(\"select top 10 * FROM [AdventureWorks2012].[Sales].[vw_salesoverview] order by OrderDate\", connection)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "helpful-fruit",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "theoretical-serum",
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_dataframe(df):\n",
    "    multipart = MIMEMultipart()\n",
    "    multipart['Subject'] = 'Please find attach your weekly report'\n",
    "    multipart['From'] = 'admin@localmail.com'\n",
    "    multipart['To'] = 'hnawaz@localmail.com'\n",
    "    #\n",
    "    for filename in EXPORTERS:\n",
    "        attachment = MIMEApplication(EXPORTERS[filename](df))\n",
    "        attachment['content-Disposition'] = 'attachement; filename={}'.format(filename)\n",
    "        multipart.attach(attachment)\n",
    "    #\n",
    "    multipart.attach(MIMEText(temp, 'html'))\n",
    "    #\n",
    "    server = smtplib.SMTP('localhost')\n",
    "    server.login(email, password)\n",
    "    server.sendmail(sender, receiver, multipart.as_string())\n",
    "    #\n",
    "    server.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "demographic-ready",
   "metadata": {},
   "outputs": [],
   "source": [
    "EXPORTERS = {'Weekly Product Report.csv': export_csv}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "italic-accountability",
   "metadata": {},
   "outputs": [],
   "source": [
    "def export_csv(df):\n",
    "    with io.StringIO() as buffer:\n",
    "        df.to_csv(buffer, index=False)\n",
    "        return buffer.getvalue()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "healthy-detail",
   "metadata": {},
   "outputs": [],
   "source": [
    "send_dataframe(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "genetic-pattern",
   "metadata": {},
   "outputs": [],
   "source": [
    "bodytemp = r'PathToYourTemplate'\n",
    "with open(bodytemp, \"r\", encoding='utf-8') as f:\n",
    "    temp= f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "practical-gateway",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
