import psycopg2, psycopg2.extensions, psycopg2.extras
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE) # se znebimo problemov s šumniki
import Data.auth_public as auth
import datetime
import os
import pandas as pd


from typing import List

# Preberemo port za bazo iz okoljskih spremenljivk
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

## V tej datoteki bomo implementirali razred Repo, ki bo vseboval metode za delo z bazo.

class Repo:
    def __init__(self):
        # Ko ustvarimo novo instanco definiramo objekt za povezavo in cursor
        self.conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password, port=DB_PORT)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


    def prodaja_po_produktnih_linijah(self) -> pd.DataFrame:
        """
        Vrne podatke o prodaji po produktnih linijah.
        """
        query = """
           	select 
                s.bk_invoice_id, 
                b.branch_name, 
                b.branch_city, 
                l.product_line, 
                s.invoice_date, 
                s.quantity, 
                s.gross_income 
            from fact_sales s 
                left join dim_branch b on b.id = s.branch_id
                left join dim_product_line l on l.id = s.product_line_id

        """
        df = pd.read_sql(query, self.conn)
        self.conn.close()
        return df

    

   
    


        


