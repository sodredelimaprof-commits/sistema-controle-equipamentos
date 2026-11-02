# Sistema de Controle de Equipamentos
# Arquivo: equipamentos.py

equipamentos = [
    {"nome": "Betoneira", "status": "Disponível"},
    {"nome": "Andaime", "status": "Locado"},
    {"nome": "Lavadora de Alta Pressão", "status": "Manutenção"},{"nome": "Gerador", "status": "Disponível"}
]


def listar_equipamentos():
    print("\n--- EQUIPAMENTOS CADASTRADOS ---")

    for equipamento in equipamentos:
        print(f"Equipamento: {equipamento['nome']}")
        print(f"Status: {equipamento['status']}")
        print("--------------------------")

listar_equipamentos()