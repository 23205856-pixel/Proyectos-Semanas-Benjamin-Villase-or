# huffman.py
# Implementación completa de Huffman: construir, codificar, decodificar, estadísticas
import heapq
from collections import Counter
from typing import Dict, Optional, Tuple

class NodoHuffman:
    def __init__(self, caracter: Optional[str], frecuencia: int):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierdo: Optional['NodoHuffman'] = None
        self.derecho: Optional['NodoHuffman'] = None

    def __lt__(self, otro):
        # heapq necesita comparar nodos
        return self.frecuencia < otro.frecuencia

    def es_hoja(self) -> bool:
        return self.izquierdo is None and self.derecho is None

class Huffman:
    def __init__(self):
        self.raiz: Optional[NodoHuffman] = None
        self.codigos: Dict[str, str] = {}
        self.codigos_inversos: Dict[str, str] = {}

    def construir_arbol(self, texto: str):
        frecuencias = Counter(texto)
        if len(frecuencias) == 0:
            return
        if len(frecuencias) == 1:
            ch = next(iter(frecuencias))
            self.raiz = NodoHuffman(ch, frecuencias[ch])
            self.codigos = {ch: '0'}
            self.codigos_inversos = {'0': ch}
            return

        heap = []
        for ch, f in frecuencias.items():
            heapq.heappush(heap, NodoHuffman(ch, f))

        while len(heap) > 1:
            izq = heapq.heappop(heap)
            der = heapq.heappop(heap)
            padre = NodoHuffman(None, izq.frecuencia + der.frecuencia)
            padre.izquierdo = izq
            padre.derecho = der
            heapq.heappush(heap, padre)

        self.raiz = heap[0]
        self._generar_codigos(self.raiz, "")

    def _generar_codigos(self, nodo: NodoHuffman, codigo_actual: str):
        if nodo is None:
            return
        if nodo.es_hoja():
            self.codigos[nodo.caracter] = codigo_actual or '0'
            self.codigos_inversos[codigo_actual or '0'] = nodo.caracter
            return
        self._generar_codigos(nodo.izquierdo, codigo_actual + '0')
        self._generar_codigos(nodo.derecho, codigo_actual + '1')

    def codificar(self, texto: str) -> str:
        if not self.codigos:
            self.construir_arbol(texto)
        return ''.join(self.codigos[ch] for ch in texto)

    def decodificar(self, bitstring: str) -> str:
        if not self.raiz:
            return ""
        resultado = []
        nodo = self.raiz
        for bit in bitstring:
            nodo = nodo.izquierdo if bit == '0' else nodo.derecho
            if nodo.es_hoja():
                resultado.append(nodo.caracter)
                nodo = self.raiz
        return ''.join(resultado)

    def guardar_comprimido(self, texto: str, ruta_salida: str) -> Tuple[int,int]:
        """
        Guarda un archivo simple: primero la tabla de frecuencias (serializada como línea)
        luego la cadena de bits (como bytes empaquetados). Devuelve (bits_original, bits_huffman_total)
        Nota: formato simple y pedagógico, no optimizado ni con padding sofisticado.
        """
        self.construir_arbol(texto)
        bitstring = self.codificar(texto)
        # Guardar frecuencias en texto para reconstruir
        frecuencias = Counter(texto)
        with open(ruta_salida, 'wb') as f:
            # primera línea: pares char:freq separados por |
            header = '|'.join(f"{ord(ch)}:{freq}" for ch, freq in frecuencias.items())
            header_bytes = (header + '\n').encode('utf-8')
            f.write(header_bytes)
            # convertir bitstring a bytes (agregar padding al final)
            padding = (8 - len(bitstring) % 8) % 8
            f.write(bytes([padding]))  # 1 byte con padding
            # agrupar en bytes
            for i in range(0, len(bitstring), 8):
                byte = bitstring[i:i+8].ljust(8, '0')
                f.write(int(byte, 2).to_bytes(1, 'big'))
        return (len(texto)*8, len(bitstring) + 8)  # bits originales, bits huffman (aprox)

# Prueba rápida si se ejecuta
if __name__ == "__main__":
    texto = "ABRACADABRA"
    h = Huffman()
    h.construir_arbol(texto)
    encoded = h.codificar(texto)
    print("Códigos:", h.codigos)
    print("Texto:", texto)
    print("Codificado bits:", encoded)
    print("Decodificado:", h.decodificar(encoded))
