SECUENCIA_BASE_NITROGENADA = ["A"*4,"C"*4, "T"*4, "G"*4]

# Verificar si la suencia ADN es una matriz cuadrada valida
def esAdnValido(adn):
    if type(adn) is not list or len(adn) < 4:
        return False

    if contieneBaseNitrogenada(adn):
        longitudAnd = len(adn)
        for secuenciaAdn in adn:
            if (len(secuenciaAdn) != longitudAnd):
                return False
    else:
        return False
    return True

# Validar si la secuencia ADN contiene las 4 bases nitrogenadas A = Adenina, C = Citosina, T = Timina, G = Guanina
def contieneBaseNitrogenada(adn): 
    BASE_NITROGENADA = "ACTG"
    for secuenciaAdn in adn:  
        if not (set(secuenciaAdn).issubset(set(BASE_NITROGENADA))):
            return False
    return True

def convertirListToString(adn):
    lista = []
    for secuencia in adn:
        lista.append("".join(secuencia))
    return lista
    
def descomponerSecuenciaAdn(adn):
    secuenciaAdn = []
    for secuencia in adn:
         secuenciaAdn.append(list(secuencia))
    return secuenciaAdn

# Trasponer la secuencia ADN de lado horizontal a Vertical
def trasponerSecuenciaAdn(adn):
    return [list(i) for i in zip(*adn)]

def contarSecuencia(adn): 
    contador = 0
    for secuenciaAdn in adn:  
        for base in SECUENCIA_BASE_NITROGENADA:
            if base in secuenciaAdn:
                contador += 1
    return contador

def encontrarSecuenciaHorizontal(adn): 
    print (" == Secuencia Horizontal Original == ")
    imprimirSecuenciaAnd(adn)
    return contarSecuencia(adn)

def encontrarSecuenciaVertical(adn):
    print (" == Secuencia Vertical == ")
    adnVertical = convertirListToString(trasponerSecuenciaAdn(adn))
    imprimirSecuenciaAnd(adnVertical)
    return contarSecuencia(adnVertical)

def esMutante(adnMutante):
    if esAdnValido(adnMutante):
        contadorSecuenciaAdn  = encontrarSecuenciaHorizontal(adnMutante) + encontrarSecuenciaVertical(adnMutante)
        print (f"Encontro {contadorSecuenciaAdn} Suencias ADN")
        if (contadorSecuenciaAdn > 1):
            return True
        else:
            return False

def imprimirSecuenciaAnd(adn):
    for a in adn:
        print (a)