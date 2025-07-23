from database import get_connection
import sys

def get_city(postcode):
  db = get_connection()

  cursor = db.cursor()
  cursor.execute(f"SELECT Nom_de_la_commune "
                 f"FROM `communes-cp` "
                 f"WHERE Code_postal={postcode}")

  res = cursor.fetchone()

  print(res)
  return res

if __name__ == "__main__":
    print(f"=> {sys.argv[1]}")

    get_city(sys.argv[1])