from database import get_connection
import sys

def get_city(postcode):
  db = get_connection()

  cursor = db.cursor()
  query = "SELECT Nom_de_la_commune FROM `communes-cp` WHERE Code_postal = %s"
  cursor.execute(query, (postcode,))

  res = cursor.fetchone()[0]

  print(res)
  return res

if __name__ == "__main__":
    print(f"=> {sys.argv[1]}")

    get_city(sys.argv[1])