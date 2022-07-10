import json
import psycopg2
import os

def lambda_handler(event, context):
    # TODO implement
    
    #Obtaining the connection to RedShift
    host = os.environ['host']
    user = os.environ['user']
    password = os.environ['password']
    port = os.environ['port']
    role = os.environ['role']
    bucket = os.environ['bucket']
    con=psycopg2.connect(dbname= 'dev', host=host, port=port, user=user, password=password)
    
    
    #Copy Command as Variable
    copy_command=f"""copy  src_dimsalesterritory (salesterritorykey, salesterritoryalternatekey, salesterritoryregion, salesterritorycountry, salesterritorygroup)
    from 's3://{bucket}/public/DimSalesTerritory/RevisedDimSalesTerritory.csv' 
    iam_role '{role}'
    DELIMITER ','
    IGNOREHEADER 1;"""
    
    #Opening a cursor and run copy query
    cur = con.cursor()
    cur.execute("truncate table src_dimsalesterritory;")
    cur.execute(copy_command)
    con.commit()
    
    #Close the cursor and the connection
    cur.close()
    con.close()
    
    print ("Print finised executing copy command")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
