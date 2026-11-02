# Nova funcionalidade: consulta de equipamentos disponíveis

equipamentos = [
    {"nome": "Betoneira", "status": "Disponível"},
    {"nome": "Andaime", "status": "Locado"},
    {"nome": "Lavadora de Alta Pressão", "status": "Manutenção"}
]

print("--- EQUIPAMENTOS DISPONÍVEIS ---")

for equipamento in equipamentos:
    if equipamento["status"] == "Disponível":
        print(equipamento["nome"])