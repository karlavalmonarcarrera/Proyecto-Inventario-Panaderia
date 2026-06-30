# ==========================================
# 1. ESTABLECER INVENTARIO INICIAL (100 de todo)
# ==========================================
inventario = {
    "Huevos": 100, "Pan_sanduchero": 100, "Jamon": 100, "Queso_sanduchero": 100,
    "Yogurt": 100, "Granola": 100, "Piña": 100, "Frutilla": 100, "Arandanos": 100,
    "Frambuesa": 100, "Pulpa": 100, "Omelette": 100, "Canasta_de_pan": 100,
    "Mantequilla": 100, "Mermelada": 100, "Nata": 100, "Tocino": 100,
    "Longaniza": 100, "Cachito": 100, "Tostada_francesa": 100, "Panes_de_yuca": 100,
    "Huevo_con_tocino": 100, "Tortilla_de_tiesto": 100, "Guacamole": 100,
    "Fruta_con_yogurt": 100, "Bizcochos": 100, "Queso_de_hoja": 100, "Manjar": 100,
    "Huevo_ranchero": 100, "Sanduche_de_pollo": 100, "Papa": 100, "Verde_majado": 100,
    "Estofado": 100, "Huevo": 100, "Tortilla_de_verde": 100, "Tortilla_de_yuca": 100,
    "Jamon_ahumado": 100, "Huevos_pochados": 100, "Salsa_holandesa": 100,
    "Sal_prieta": 100, "Bolones": 100, "Huevos_fritos": 100, "Tostadas": 100,
    "Hashbrown": 100, "Pancakes": 100, "Salchicha": 100
}

recetas = {
    1: {"Huevos": 2, "Pan_sanduchero": 1, "Jamon": 10, "Queso_sanduchero": 10, "Yogurt": 30, "Granola": 20, "Piña": 25, "Frutilla": 25, "Arandanos": 25, "Frambuesa": 25, "Pulpa": 1},
    2: {"Omelette": 1, "Canasta_de_pan": 1, "Mantequilla": 30, "Mermelada": 30, "Nata": 50},
    3: {"Tocino": 45, "Longaniza": 50, "Huevos": 2, "Cachito": 1, "Mantequilla": 30, "Mermelada": 30},
    4: {"Tostada_francesa": 1},
    5: {"Panes_de_yuca": 2, "Yogurt": 150, "Huevo_con_tocino": 1},
    6: {"Tortilla_de_tiesto": 1, "Guacamole": 60, "Huevo_con_tocino": 1},
    7: {"Tortilla_de_tiesto": 1, "Fruta_con_yogurt": 100, "Huevo_con_tocino": 1},
    8: {"Bizcochos": 4, "Queso_de_hoja": 1, "Manjar": 30, "Huevo_ranchero": 1},
    9: {"Bizcochos": 4, "Queso_de_hoja": 1, "Manjar": 30},
    10: {"Sanduche_de_pollo": 1, "Papa": 100, "Guacamole": 60},
    11: {"Verde_majado": 100, "Estofado": 50, "Huevo": 1},
    12: {"Tortilla_de_verde": 1, "Tortilla_de_yuca": 1, "Jamon_ahumado": 45, "Huevos_pochados": 2, "Salsa_holandesa": 30, "Sal_prieta": 5},
    13: {"Bolones": 2, "Guacamole": 60, "Estofado": 50},
    14: {"Huevos_fritos": 2, "Tostadas": 2, "Mantequilla": 30, "Mermelada": 30, "Hashbrown": 1, "Pancakes": 2, "Salchicha": 1, "Tocino": 45}
}

nombres_desayunos = {
    1: "Desayuno Aroma", 2: "Aroma de la Casa", 3: "Ranchero", 4: "Francés",
    5: "Yuca Aroma", 6: "Típico", 7: "Típico Aroma", 8: "Cayambeño Full",
    9: "Cayambeño", 10: "Chicken Aroma", 11: "Verde Aroma", 12: "Miti Miti",
    13: "Aroma Bolón", 14: "Americano"
}

# ==========================================
# 2. PROCESO REPETITIVO POR 7 DÍAS
# ==========================================
for dia in range(1, 8):
    print("\n==========================================")
    print("             INICIO DEL DÍA", dia)
    print("==========================================")
    
    dia_activo = True
    
    while dia_activo:
        print("\n--- MENÚ PANADERÍA AROMA ---")
        for k, v in nombres_desayunos.items():
            print(k, ".", v)
        print("15. Abastecer / Modificar Inventario (Aumentar Stock)")
        print("16. Cierre de Registro Diario (Cambiar de día)")
        
        opcion = int(input("Seleccione una opción: "))
        
        if opcion >= 1 and opcion <= 14:
            print("¿Cuántos desayunos", nombres_desayunos[opcion], "desea registrar?")
            cantidad_pedida = int(input())
            if cantidad_pedida <= 0:
                print("Cantidad inválida.")
                continue
                
            receta = recetas[opcion]
            max_posible = cantidad_pedida
            
            # Buscamos cuántos se pueden hacer realmente
            for ingrediente, cantidad_necesaria in receta.items():
                disponible_item = inventario[ingrediente] // cantidad_necesaria
                if disponible_item < max_posible:
                    max_posible = disponible_item
            
            cantidad_final = 0
            
            if max_posible == cantidad_pedida:
                cantidad_final = cantidad_pedida
            elif max_posible > 0:
                print("ALERTA: Inventario insuficiente para", cantidad_pedida, ". Solo disponemos de", max_posible)
                print("¿Desea registrar los", max_posible, "desayunos disponibles? (si/no): ")
                aceptar = input()
                if aceptar == "si" or aceptar == "sí":
                    cantidad_final = max_posible
                else:
                    print("Pedido cancelado.")
            else:
                print("ALERTA: Inventario insuficiente. No disponemos de ingredientes ahorita.")
            
            # Restamos usando las variables limpias
            if cantidad_final > 0:
                for ingrediente, cantidad_necesaria in receta.items():
                    inventario[ingrediente] -= (cantidad_necesaria * cantidad_final)
                print("¡Se han registrado", cantidad_final, nombres_desayunos[opcion], "con éxito!")
                
        elif opcion == 15:
            print("\n--- MODIFICAR / AUMENTAR STOCK ---")
            ingrediente_a_buscar = input("Ingrese el nombre del ingrediente que llegó: ")
            
            if ingrediente_a_buscar in inventario:
                print("Inventario actual de", ingrediente_a_buscar, "es", inventario[ingrediente_a_buscar])
                cantidad_nueva = int(input("¿Cuánto desea sumarle?: "))
                if cantidad_nueva >= 0:
                    inventario[ingrediente_a_buscar] += cantidad_nueva
                    print("¡Inventario actualizado!")
                else:
                    print("No puede sumar cantidades negativas.")
            else:
                print("El ingrediente ingresado no existe.")
                
        elif opcion == 16:
            print("\nCerrando el registro del Día", dia)
            dia_activo = False
        else:
            print("Opción inválida. Intente de nuevo.")

# ==========================================
# 3. REPORTES FINALES DE LA SEMANA
# ==========================================
print("\n==========================================")
print("¡HA TERMINADO LA SEMANA DE 7 DÍAS!")
print("==========================================")
print("       INVENTARIO FINAL RESTANTE          ")
print("==========================================")

for ingrediente, stock_restante in inventario.items():
    print("-", ingrediente, ":", stock_restante)