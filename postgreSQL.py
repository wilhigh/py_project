def query_postgreSQL(query):
     import pandas as pd
     import psycopg2 as pg
     from datetime import datetime
      
    # DB Connection
     conn = pg.connect(host='174.100.29.236', port='5432', dbname='sonarqube', user='sonarqube', password='sonarqube')
     start_tm = datetime.now()

     # Get a DataFrame
     query_result = pd.read_sql(query, conn)
 
     # Close connection
     end_tm = datetime.now()

     print('START: ', str(start_tm))
     print('END: ', str(end_tm))
     print('ELAP: ', str(end_tm - start_tm))
     conn.close()
 
     return query_result

##-- SQL query
query = """
     SELECT kee
    FROM public.projects
    where kee not like '%:%'
    group by kee ;
 """

##-- Excute PostgreSQL SQL in Python
qr = query_postgreSQL(query)

print(qr);