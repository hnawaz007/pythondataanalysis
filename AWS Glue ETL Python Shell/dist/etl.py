import psycopg2

#Obtaining the connection to RedShift
con=psycopg2.connect(dbname= 'dev', host='redshift.amazonaws.com', port= '5439', user= 'awsuser', password= '*****')


#Copy Command as Variable
copy_command="""copy  src_dimproductsubcategory (productsubcategorykey ,productsubcategoryalternatekey ,englishproductsubcategoryname ,spanishproductsubcategorysame,frenchproductsubcategorysame ,productcategorykey )
from 's3://your-s3-bucket-name/public/DimProductSubcategory/DimProductSubcategory.csv' 
iam_role 'arn:aws:iam::879408800400:role/'
DELIMITER ','
IGNOREHEADER 1;"""

#Opening a cursor and run copy query
cur = con.cursor()
cur.execute("truncate table src_dimproductsubcategory;")
cur.execute(copy_command)
con.commit()

#Close the cursor and the connection
cur.close()
con.close()

print ("Print finised executing copy command")
