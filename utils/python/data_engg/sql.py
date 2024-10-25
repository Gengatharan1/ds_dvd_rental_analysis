from sqlalchemy import (
    create_engine, text
    )
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
username = os.environ.get('sql_db_usr') 
password = os.environ.get('sql_db_pwd')
hostname = 'localhost'
port = os.environ.get('sql_db_endpoint') 
database = os.environ.get('sql_db_dbname')


# postgresql
db_url = f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{database}'


# Create engine
engine = create_engine(db_url)


def sql():
    print(db_url)
    
    return engine


def get_table_df(query=None, t_main=None, calc_cols=None, t_joins=None, t_cols=None, groups=None, orders=None):

    # Get database engine
    engine = sql()

    # Generate SQL query if none provided
    if query is None:
        query = f"select"

        if t_cols:
            cols = []           # Handle selected columns for the query
            for t in t_cols:
                for c in t[1]:
                    cols.append(f"{t[0]}.{c}")
            query += ' ' + ', '.join(cols)
        else:
            query += " *"    # Select all columns

        # calculated columns
        if calc_cols:
            query += ', '+calc_cols

        query += f" from {t_main}"

        # join tables
        if t_joins:
            for t in t_joins:
                query += f" left outer join {t[0]} on {t[1]}"
                # query += f" left outer join {t[0]} on {t_main}.{t[1]} = {t[0]}."
                # if len(t) > 2:
                #     query += t[2]
                # else:
                #     query += t[1]

        # groupby query            
        if groups:
            query += f' group by {', '.join(groups)}'
        
        # orderby query
        if orders:
            query += f' order by {', '.join(orders)}'

    print(query)

    # Integrating SQL queries with Pandas using sqlalchemy
    stmt = text(query)
    with engine.connect() as connection: res = connection.execute(stmt)
    df = pd.DataFrame(res.fetchall(), columns=res.keys())
    return df

if __name__ == '__main__':
    pass