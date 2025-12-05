# bst.py
# Árbol binario de búsqueda simple (sin duplicados)
from typing import Optional, List, Tuple

class BSTNode:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo: Optional['BSTNode'] = None
        self.derecho: Optional['BSTNode'] = None

class BST:
    def __init__(self):
        self.raiz: Optional[BSTNode] = None

    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo: Optional[BSTNode], valor) -> BSTNode:
        if nodo is None:
            return BSTNode(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_rec(nodo.derecho, valor)
        # si es igual: no insertamos duplicados
        return nodo

    def buscar(self, valor) -> bool:
        return self._buscar_rec(self.raiz, valor)

    def _buscar_rec(self, nodo: Optional[BSTNode], valor) -> bool:
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izquierdo, valor)
        else:
            return self._buscar_rec(nodo.derecho, valor)

    def minimo(self, nodo: Optional[BSTNode]) -> Optional[BSTNode]:
        if nodo is None:
            return None
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo

    def eliminar(self, valor):
        self.raiz = self._eliminar_rec(self.raiz, valor)

    def _eliminar_rec(self, nodo: Optional[BSTNode], valor) -> Optional[BSTNode]:
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_rec(nodo.derecho, valor)
        else:
            # caso 1: hoja
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            # caso 2: un hijo
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            # caso 3: dos hijos -> usar sucesor inorden (mínimo del subárbol derecho)
            sucesor = self.minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.valor)
        return nodo

    def inorden(self) -> List:
        res = []
        self._inorden_rec(self.raiz, res)
        return res

    def _inorden_rec(self, nodo: Optional[BSTNode], res: List):
        if nodo:
            self._inorden_rec(nodo.izquierdo, res)
            res.append(nodo.valor)
            self._inorden_rec(nodo.derecho, res)

# Pruebas básicas cuando se ejecuta como script
if __name__ == "__main__":
    bst = BST()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insertar(v)
    print("Inorden:", bst.inorden())
    bst.eliminar(70)
    print("Inorden después de eliminar 70:", bst.inorden())
