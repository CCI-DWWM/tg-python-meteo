from weatherAPI import get_weather

if __name__ == "__main__":
    data = get_weather("75001")
    print("Résultat météo :", data["temperature"])