import sys
from catalogo import catalogo, leer, resumen_orbita, zona

entrada = sys.argv

ruta = entrada[1]

def resumen (ruta):
    cat=resumen_orbita(catalogo(leer(ruta)))
    print("\n========== RESUMEN DE SATÉLITES ==========\n")

    for orbita, datos in cat.items():
        print(f"--- Órbita {orbita} ---")
        print(f"Cantidad de satélites: {datos['cantidad']}")
        print(f"Altitud mínima:        {datos['minimo']} km")
        print(f"Altitud máxima:        {datos['maximo']} km")
        print(f"Altitud promedio:      {datos['promedio']} km")
        print()

    return 0

if entrada[2]=="resumen":
    resumen(ruta)

elif entrada[2]=="zona":
    zona(entrada)

else:
    print("Consulta invalida")