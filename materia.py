# tasas de cambio predefinidas (estas son tasas ficticias, debes actualizarlas si es necesesario)
TASA_MXN_USD = 0.054
TASA_MXN_EUR = 0.048
TASA_MXN_GBP = 0.043
TASA_USD_MXN = 18.57
TASA_EUR_MXN = 20.31
TASA_GBP_MXN = 23.26

# funcion para convertir pesos a otras monedas
def convertir_mxn_a_otra(moneda, cantidad):
    if moneda == "USD":
        return cantidad * TASA_MXN_USD
    elif moneda == "EUR":
        return cantidad * TASA_MXN_EUR
    elif moneda == "GBP":
        return cantidad * TASA_MXN_GBP 
    else:
        return None
    
#funcion para convertir de otra moneda a pesos
def convertir_otra_a_mxn(moneda, cantidad):
    if moneda == "USD":
        return  cantidad * TASA_USD_MXN
    elif moneda == "EUR":
        return cantidad * TASA_EUR_MXN
    elif moneda == "GBP":
        return cantidad * TASA_GBP_MXN
    else:
        return None
    
# menu de opciones 
print("bienvenido al conversor de monedas")
print("Elige una opcion:")
print("1. convertir de pesos mexicanos (MXN) a otra moneda") 
print("2. convertir de otra moneda a pesos mexicanos (MXN)")

#validacion de entrada 
try:
    opcion = int(input("ingresa el numero de la opcion que deseas: "))
    
    if opcion == 1:
        print("monedas dis´ponibles para convertir desde pesos mexicanos (MXN):")
        print("1. convertir a dolares (USD)")
        print("2. convertir a euros (EUR)")
        print("3. convertir a libras esterlinas (GBP)")
        
        opcion_moneda = int(input("selecciona el numero de la moneda a la que deseas convertir: "))
        cantidad = float(input("ingresa la cantidad en pesos mexicanos (MXN): "))
        
        if opcion_moneda == 1:
            resultado = convertir_mxn_a_otra("USD", cantidad)
            print(f"{cantidad} MXN son {resultado} USD")
        elif opcion_moneda == 2:
            resultado = convertir_mxn_a_otra("EUR",  cantidad)
            print(f"{cantidad} MXN son {resultado} EUR")
        elif opcion_moneda == 3:
            resultado = convertir_mxn_a_otra("GBP", cantidad)
            print(f"{cantidad} MXN son {resultado} GBP")
        else:
            print("opcion invalida")
            
    elif opcion == 2:
        print("monedas disponibles para convertir a pesos mexicanos (MXN):")
        print("1. convertir desde dolares (USD) a MXN")
        print("2. convertir desde euros (EUR) a MXN")
        print("3. convertir desde libras esterlinas (GBP) a MXN")
        
        opcion_moneda = int(input("selecciona el numero de la moneda desde la que deseas convertir:"))
        cantidad = float(input("ingresa la cantidad de la moneda seleccionada: "))
        
        if opcion_moneda == 1:
            resultado = convertir_otra_a_mxn("USD", cantidad )
            print(f"{cantidad} USD son {resultado} MXN")
        elif opcion_moneda == 2:
            resultado = convertir_otra_a_mxn("EUR", cantidad)
            print(f"{cantidad} EUR son {resultado} MXN")
        elif opcion_moneda == 3:
            resultado = convertir_otra_a_mxn("GBP", cantidad)
            print(f"{cantidad} GBP son {resultado} MXN")
        else:
            print("opcion no valida.")
            
    else:
        print("opcion no valida. por favor selecciona una opcion entre 1 y 2.")
        
except ValueError:
    print("entrada no valida por favor ingresa un numero valido")