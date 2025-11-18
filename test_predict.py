import requests

URL = "http://localhost:8999/predict"   
FILE_PATH = "heart_test.csv"            

def test_predict():
    with open(FILE_PATH, "rb") as f:
        files = {"file": (FILE_PATH, f, "text/csv")}
        response = requests.post(URL, files=files)

    print(f"Статус: {response.status_code}")
    try:
        print("Ответ:", response.json()[:10])
    except Exception:
        print("Сырой ответ:", response.text)


if __name__ == "__main__":
    test_predict()
