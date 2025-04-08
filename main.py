import time
import threading

# Función para aplicar Modus Ponens
def aplicar_modus_ponens(argumento):
    if "si" in argumento.lower() and "entonces" in argumento.lower():
        partes = argumento.lower().split("entonces")
        premisa = partes[0].replace("si", "").strip().capitalize()
        conclusion = partes[1].strip().capitalize()
        return f"Dado que '{premisa}' es verdadero, concluimos que '{conclusion}' (por Modus Ponens)"
    else:
        return "El argumento no tiene la estructura adecuada para aplicar Modus Ponens."

# Función para aplicar Modus Tollens
def aplicar_modus_tollens(argumento):
    if "si" in argumento.lower() and "entonces" in argumento.lower():
        partes = argumento.lower().split("entonces")
        premisa = partes[0].replace("si", "").strip().capitalize()
        conclusion = partes[1].strip().capitalize()
        return f"Dado que '{conclusion}' es falso, concluimos que '{premisa}' también es falso (por Modus Tollens)"
    else:
        return "El argumento no tiene la estructura adecuada para aplicar Modus Tollens."

# Función para detectar MP o MT a partir de dos argumentos
def detectar_regla_doble(p1, p2):
    if "si" in p1.lower() and "entonces" in p2.lower():
        conclusion = p2.lower().replace("entonces", "").strip()
        if "no" in conclusion:
            return f"Por lo tanto... {p1.split('si')[1].strip().capitalize()} (Modus Tollens)"
        else:
            return f"Por lo tanto... {conclusion.capitalize()} (Modus Ponens)"
    elif "si" in p2.lower() and "entonces" in p1.lower():
        conclusion = p1.lower().replace("entonces", "").strip()
        if "no" in conclusion:
            return f"Por lo tanto... {p2.split('si')[1].strip().capitalize()} (Modus Tollens)"
        else:
            return f"Por lo tanto... {conclusion.capitalize()} (Modus Ponens)"
    else:
        return None

# Funciones para evaluación de la proposición y tabla de verdad
def evaluacion_condicional(p, q):
    return not p or q  # Si P entonces Q (P → Q)

def evaluacion_disyuncion(p, q):
    return p or q  # P o Q (P ∨ Q)

def tabla_verdad_condicional():
    resultados = []
    for p in [True, False]:
        for q in [True, False]:
            resultado = evaluacion_condicional(p, q)
            resultados.append((p, q, resultado))
    return resultados

def tabla_verdad_disyuncion():
    resultados = []
    for p in [True, False]:
        for q in [True, False]:
            resultado = evaluacion_disyuncion(p, q)
            resultados.append((p, q, resultado))
    return resultados

def clasificar_resultado(tabla):
    resultados = [r[2] for r in tabla]
    if all(resultados):
        return "Tautología"
    elif not any(resultados):
        return "Contradicción"
    else:
        return "Contingencia" if True in resultados and False in resultados else "Falacia"

def mostrar_tabla_verdad(tabla, tipo):
    print(f"\nTabla de Verdad ({tipo}):")
    print("P    Q    Resultado")
    for fila in tabla:
        print(f"{fila[0]}  {fila[1]}  {fila[2]}")
    resultado_clasificado = clasificar_resultado(tabla)
    print(f"\nClasificación: {resultado_clasificado}")

# Función principal que maneja el flujo
def main():
    print("Ingresa el primer argumento:")
    primer_argumento = input("→ ")

    segundo_argumento = {'valor': None}

    def leer_segundo_input():
        segundo_argumento['valor'] = input("\nIngresa segundo argumento relacionado o espera 5 segundos:\n→ ")

    hilo_input = threading.Thread(target=leer_segundo_input)
    hilo_input.start()
    hilo_input.join(timeout=5)

    entrada = segundo_argumento['valor']

    if entrada is None or entrada.strip() == "":
        print("\n[Análisis automático de MP o MT basado en el primer argumento]")
        if "si" in primer_argumento.lower() and "entonces" in primer_argumento.lower():
            print("→ Resultado: Detectado Modus Ponens (por defecto)")
            print(aplicar_modus_ponens(primer_argumento))
        else:
            print("→ Resultado: Argumento no válido para MP o MT\n")

    elif entrada.lower() == 'mp':
        print("\n[Aplicando regla lógica: Modus Ponens]")
        print("→", aplicar_modus_ponens(primer_argumento))

    elif entrada.lower() == 'mt':
        print("\n[Aplicando regla lógica: Modus Tollens]")
        print("→", aplicar_modus_tollens(primer_argumento))

    elif ' o ' in entrada.lower():
        print("\n[Detectando disyunción y evaluando proposición compuesta]")
        print("→ Resultado: Por lo tanto, [proposición resultante] - Es una [tautología/contradicción/etc.]\n")

        # Evaluamos la disyunción y mostramos la tabla de verdad
        tabla = tabla_verdad_disyuncion()  # Evaluamos disyunción
        mostrar_tabla_verdad(tabla, "Disyunción (P ∨ Q)")

    else:
        resultado = detectar_regla_doble(primer_argumento, entrada)
        if resultado:
            print("\n[Análisis lógico a partir de dos argumentos]")
            print("→", resultado)
        else:
            print("\nEntrada no reconocida como regla lógica ni disyunción.")

if __name__ == '__main__':
    main()