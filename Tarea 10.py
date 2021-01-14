aux = 0
X = 0
class NodoArbol:
  def __init__( self , value , left = None , right = None ):
    self.data = value
    self.left = left
    self.right = right
    
  def recorrido( self , contador = 0):

    global aux
    global X

    #print( self.data , "El nivel es: ", contador )
    if self.left:
      self.left.recorrido( contador  + 1)
    if self.right:
      self.right.recorrido( contador + 1)

    if aux < contador:
      aux = contador
      X = self.data


arbol = NodoArbol( 8 , NodoArbol( 3 , NodoArbol( 1 ) , NodoArbol( 6 , NodoArbol( 4 ) , NodoArbol( 7 ))) , NodoArbol( 10 , None , NodoArbol( 14 , NodoArbol( 13 ))) )
arbol.recorrido()
print("\n")
print(X , "Y su nivel es: ", aux)
print("\n")

arbol_2 = NodoArbol( 10 , NodoArbol( 7 , NodoArbol( 3 ) , NodoArbol( 8 , NodoArbol( 5 ) , NodoArbol( 9 , None , NodoArbol( 12 )))),NodoArbol( 11 ) )
aux = 0
arbol_2.recorrido()
print("\n")
print(X , "Y su nivel es: ", aux)
print("\n")


arbol_3 = NodoArbol( 2 , NodoArbol( 7 , NodoArbol( 2 ) , NodoArbol( 6 , NodoArbol( 5 ), NodoArbol( 11 ))) , NodoArbol( 5 , None , NodoArbol( 9 , NodoArbol( 4 ))))
aux = 0
arbol_3.recorrido()
print("\n")
print(X , "Y su nivel es: ", aux)
print("\n")

arbol_4 = NodoArbol( 60 , NodoArbol( 41 , NodoArbol( 16 , NodoArbol( 25 )) , NodoArbol( 53 , NodoArbol( 46 , NodoArbol( 42 ) ) , NodoArbol( 55 )) ) , NodoArbol( 74 , NodoArbol( 65 , NodoArbol( 63 , NodoArbol( 62 ) , NodoArbol( 64 ) ), NodoArbol( 70 ))))
aux = 0
arbol_4.recorrido()
print("\n")
print(X , "Y su nivel es: ", aux)
print("\n")