# --- Mis datos de la carnicería ---
sueldo_cajero = 180000
cobro_gaby = 90000
ahorro_total = sueldo_cajero + cobro_gaby

meta_pesos = 1000000

# --- Cálculo ---
meses_para_meta = meta_pesos / ahorro_total

print(f"Juntando ${ahorro_total} por mes, llego al millon en {meses_para_meta:.1f} meses.")
