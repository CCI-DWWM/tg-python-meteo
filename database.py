import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

# load .env file ton environment
load_dotenv()

def get_connection():
  try:
    # DB connection
    db = mysql.connector.connect(
      # use data from .env file
      user=os.getenv('DB_USER'),
      password=os.getenv('DB_PASSWORD'),
      host=os.getenv('DB_HOST'),
      database=os.getenv('DB_DATABASE')
    )
    # message if connection is ok
    print("Database connected successfully")
    return db
  # messages if connection is not ok
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(f"Error: {err}")
    return None
