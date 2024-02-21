# pip install requests==2.31.0 (talvez tenha que ser pip3 dependendo da máquina)

print("\nImportação e uso de um módulo de terceiros:")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitacao HTTP para {url} retornou o status {response.status_code}.")
