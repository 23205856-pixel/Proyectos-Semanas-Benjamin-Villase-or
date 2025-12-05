# main.py
import os
import sys
from avl import AVL
from huffman import Huffman
from bst import BST

def cargar_texto(ruta):
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read()

def construir_indice_avl(texto):
    """
    Construye un AVL indexando palabras únicas; para simplicidad guardamos palabras limpias.
    (Podrías extender para guardar posiciones: línea/columna por lista).
    """
    import re
    palabras = re.findall(r"\w+", texto.lower(), flags=re.UNICODE)
    avl = AVL()
    for p in set(palabras):
        avl.insertar(p)
    return avl, len(palabras)

def busqueda_interactiva(avl):
    print("Modo búsqueda (escribe 'salir' para terminar).")
    while True:
        q = input("Palabra a buscar: ").strip().lower()
        if q in ('salir', 'exit', ''):
            break
        # la clase AVL no tiene buscar por diseño en este ejemplo, usamos recorrido y comprobación
        encontrado = any(item[0] == q for item in avl.inorden())
        print("Encontrado." if encontrado else "No encontrado.")

def main():
    print("Proyecto Semana 8 — Índice (AVL) + Huffman\n")
    ruta = "texto_prueba.txt"
    if not os.path.exists(ruta):
        print(f"No encontré {ruta} en el directorio. Asegúrate de crear el archivo con el texto de prueba.")
        sys.exit(1)
    texto = cargar_texto(ruta)
    print("Cargando texto... (longitud:", len(texto), "caracteres)")
    avl, total_palabras = construir_indice_avl(texto)
    print(f"Índice construido (AVL). Palabras totales encontradas: {total_palabras}.")
    print("Muestro algunas entradas (inorden, valor y factor de balance):")
    muestra = avl.inorden()[:30]
    for v, fb in muestra:
        print(f"  {v} (FB={fb})")
    # búsqueda interactiva opcional
    print("\n--- Búsqueda ---")
    busqueda_interactiva(avl)
    # Huffman: comprimir y mostrar estadística
    print("\n--- Compresión Huffman ---")
    h = Huffman()
    bits_orig, bits_huff = h.guardar_comprimido(texto, "texto_prueba.huff")
    ahorro = 100.0 * (bits_orig - bits_huff) / bits_orig
    print(f"Bits originales: {bits_orig}, Bits aproximados Huffman: {bits_huff}")
    print(f"Ahorro aproximado: {ahorro:.2f}%")
    print("Archivo 'texto_prueba.huff' creado (formato pedagógico).")

if __name__ == "__main__":
    main()
