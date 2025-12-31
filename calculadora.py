# Programa interactivo de ahorro
print("--- CALCULADORA DE METAS ---")

# Usamos input() para que la computadora te pregunte a vos
sueldo = int(input("¿Cuánto vas a cobrar este mes como cajero?: "))
gaby = int(input("¿Cuánto le vas a cobrar a Gaby?: "))

ahorro_mensual = sueldo + gaby
meta = 1000000

meses = meta / ahorro_mensual

print(f"\nResumen: Estás ahorrando ${ahorro_mensual} por mes.")
print(f"Te faltan {meses:.1f} meses para ser millonario.")
