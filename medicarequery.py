import pandas as pd
from google.cloud import bigquery


QUERY = """
        SELECT provider_city, provider_state, drg_definition,
        average_total_payments, average_medicare_payments
        FROM `bigquery-public-data.cms:medicare.inpatient_charges_2015`
        WHERE provider_city = "Amarillo" AND provider_state= "TX"
        ORDER BY provider_city ASC
        LIMIT 1000
        """
        
CLIENT = bigquery.Client.froom_service_account_json(
            'MedicareProject2-122xxxxf413.json')
            
query_job = client.query(QUERY)
df = query_job.to_datafram()

print("Records returned: " df.shape)
print()
print("First 10 Records")
print(df.head(10))
