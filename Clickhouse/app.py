import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time
#

try:
    conn_str = 'clickhouse://default:@localhost/default'
    engine = create_engine(conn_str)
    session = sessionmaker(bind=engine)()
except Exception as e:
    print("Error while connectint to Clickhoust " + str(e))


st.set_page_config(layout="wide")
st.title("Sales Transactions Real-Time ▁ ▂ ▃ ▄ ▅ ▆ █")

now = datetime.now()
dt_string = now.strftime("%d %B %Y %H:%M:%S")
st.write(f"Last update: {dt_string}")

if not "sleep_time" in st.session_state:
    st.session_state.sleep_time = 5

if not "auto_refresh" in st.session_state:
    st.session_state.auto_refresh = True

#
mapping = {
    "1 hour": {"period": "60", "granularity": "minute", "raw": 60},
    "30 minutes": {"period": "30", "granularity": "minute", "raw": 30},
    "10 minutes": {"period": "10", "granularity": "minute", "raw": 10},
    "5 minutes": {"period": "5", "granularity": "minute", "raw": 5}
}

with st.expander("Configure Dashboard", expanded=True):
    left, right = st.columns(2)

    with left:
        auto_refresh = st.checkbox('Auto Refresh?', st.session_state.auto_refresh)

        if auto_refresh:
            number = st.number_input('Refresh rate in seconds', value=st.session_state.sleep_time)
            st.session_state.sleep_time = number

    with right:
            time_ago = st.radio("Time period to cover", mapping.keys(), horizontal=True, key="time_ago")



st.header("Live Kafka Sales..." ) 

minute = mapping[time_ago]["period"]
print(str(minute))
query = f"""select 
created_date
,salesordernumber
, count(*) as "Num Transactions"
, count(distinct(salesordernumber)) as "Num orders"
, (toInt32(round(sum(salesamount),2))) as "sales"
from `default`.vw_sales
where created_date >=   dt -  INTERVAL {minute} MINUTE 
GROUP BY created_date,
salesordernumber
order by 1 ;"""

df = pd.read_sql(query, engine)
df.style.format('{:,}')

metric1, metric2, metric3 = st.columns(3)

metric1.metric(
    label="Number of Transactions",
    value=(df['Num Transactions'].sum()),
)

metric2.metric(
    label="Number of Orders",
    value=(df['Num orders'].sum()),
)

metric3.metric(
    label="Sales Amount",
    value=(df.sales.sum()), 
)

#
st.header(f"Transactions since last {minute} minutes..." ) 
#
st.line_chart(data = df, x= "created_date", y = "sales")
#
st.write(df[['salesordernumber','created_date','sales']])

#
if auto_refresh:
    time.sleep(number)
    st.experimental_rerun()








































