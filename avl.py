# avl.py
# Árbol AVL (basado en la guía): inserción, rotaciones, inorden con factor de balance
from typing import Optional, List, Tuple

class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo: Optional['NodoAVL'] = None
        self.derecho: Optional['NodoAVL'] = None
        self.altura = 1  # altura de nodo (hoja = 1)

class AVL:
    def __init__(self):
        self.raiz: Optional[NodoAVL] = None

    def altura_nodo(self, nodo: Optional[NodoAVL]) -> int:
        return nodo.altura if nodo else 0

    def actualizar_altura(self, nodo: NodoAVL):
        nodo.altura = 1 + max(self.altura_nodo(nodo.izquierdo), self.altura_nodo(nodo.derecho))

    def factor_balance(self, nodo: Optional[NodoAVL]) -> int:
        if not nodo:
            return 0
        return self.altura_nodo(nodo.izquierdo) - self.altura_nodo(nodo.derecho)

    def rotacion_derecha(self, y: NodoAVL) -> NodoAVL:
        x = y.izquierdo
        T2 = x.derecho
        # Rotación
        x.derecho = y
        y.izquierdo = T2
        # Actualizar alturas
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return x

    def rotacion_izquierda(self, x: NodoAVL) -> NodoAVL:
        y = x.derecho
        T2 = y.izquierdo
        # Rotación
        y.izquierdo = x
        x.derecho = T2
        # Actualizar alturas
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        return y

    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo: Optional[NodoAVL], valor) -> NodoAVL:
        if not nodo:
            return NodoAVL(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_rec(nodo.derecho, valor)
        else:
            return nodo  # sin duplicados

        # actualizar altura y balance
        self.actualizar_altura(nodo)
        fb = self.factor_balance(nodo)

        # LL
        if fb > 1 and valor < nodo.izquierdo.valor:
            return self.rotacion_derecha(nodo)
        # RR
        if fb < -1 and valor > nodo.derecho.valor:
            return self.rotacion_izquierda(nodo)
        # LR
        if fb > 1 and valor > nodo.izquierdo.valor:
            nodo.izquierdo = self.rotacion_izquierda(nodo.izquierdo)
            return self.rotacion_derecha(nodo)
        # RL
        if fb < -1 and valor < nodo.derecho.valor:
            nodo.derecho = self.rotacion_derecha(nodo.derecho)
            return self.rotacion_izquierda(nodo)

        return nodo

    def inorden(self) -> List[Tuple]:
        res = []
        self._inorden(self.raiz, res)
        return res  # lista de (valor, FB)
    def _inorden(self, nodo: Optional[NodoAVL], res: List[Tuple]):
        if nodo:
            self._inorden(nodo.izquierdo, res)
            res.append((nodo.valor, self.factor_balance(nodo)))
            self._inorden(nodo.derecho, res)

    # Método para mostrar estructura (útil en consola)
    def mostrar_estructura(self):
        def _mostrar(nodo: Optional[NodoAVL], nivel=0, pref="Raíz: "):
            if nodo:
                print(" "*(nivel*4) + pref + f"{nodo.valor} (FB={self.factor_balance(nodo)}, h={nodo.altura})")
                if nodo.izquierdo or nodo.derecho:
                    _mostrar(nodo.izquierdo, nivel+1, "Izq: ")
                    _mostrar(nodo.derecho, nivel+1, "Der: ")
        _mostrar(self.raiz)

# Prueba si se ejecuta directamente
if __name__ == "__main__":
    avl = AVL()
    for v in [10, 20, 30, 40, 50, 25]:
        avl.insertar(v)
        print(f"\nDespués de insertar {v}:")
        avl.mostrar_estructura()
    print("\nInorden con FB:", avl.inorden())
