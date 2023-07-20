from colorama import Fore, init
init()

#colores

rojo = Fore.LIGHTRED_EX
azul = Fore.LIGHTBLUE_EX
gris = Fore.LIGHTBLACK_EX
blanco = Fore.LIGHTWHITE_EX
amarillo = Fore.LIGHTYELLOW_EX
violeta = Fore.LIGHTMAGENTA_EX
verde = Fore.LIGHTGREEN_EX
celeste = Fore.LIGHTCYAN_EX


def portada():
    print(f"""
{violeta}
                                                _..._                                                                                       
                                             .-'_..._''.                                      .---.    _______                _______       
 __  __   ___                _..._   .--.  .' .'      '.\.--._________   _...._               |   |.--.\  ___ `'.             \  ___ `'.    
|  |/  `.'   `.            .'     '. |__| / .'           |__|\        |.'      '-.            |   ||__| ' |--.\  \             ' |--.\  \   
|   .-.  .-.   '          .   .-.   ..--.. '             .--. \        .'```'.    '.          |   |.--. | |    \  '            | |    \  '  
|  |  |  |  |  |          |  '   '  ||  || |             |  |  \      |       \     \   __    |   ||  | | |     |  '    __     | |     |  ' 
|  |  |  |  |  |  _    _  |  |   |  ||  || |             |  |   |     |        |    |.:--.'.  |   ||  | | |     |  | .:--.'.   | |     |  | 
|  |  |  |  |  | | '  / | |  |   |  ||  |. '             |  |   |      \      /    ./ |   \ | |   ||  | | |     ' .'/ |   \ |  | |     ' .' 
|  |  |  |  |  |.' | .' | |  |   |  ||  | \ '.          .|  |   |     |\`'-.-'   .' `" __ | | |   ||  | | |___.' /' `" __ | |  | |___.' /'  
|__|  |__|  |__|/  | /  | |  |   |  ||__|  '. `._____.-'/|__|   |     | '-....-'`    .'.''| | |   ||__|/_______.'/   .'.''| | /_______.'/   
               |   `'.  | |  |   |  |        `-.______ /       .'     '.            / /   | |_'---'    \_______|/   / /   | |_\_______|/    
               '   .'|  '/|  |   |  |                 `      '-----------'          \ \._,\ '/                      \ \._,\ '/              
                `-'  `--' '--'   '--'                                                `--'  `"                        `--'  `"               {violeta}

             {gris} CREATED BY P3G4D0 {gris}
            {celeste} BUSCA DATOS DEL PERSONAL DE MUNICIPALIDAD DE ROSARIO.""")
    
def buscar_dato(archivo, dato_buscado):
    try:
        with open(archivo, 'r', encoding="utf-8") as archivo_txt:
            for linea in archivo_txt:
                if dato_buscado in linea:
                    print(linea)
    except FileNotFoundError:
        print(f"No se encontro el archivo {archivo}")

archivo = "C:\\Users\Usuario\Desktop\pagina web\datos.txt"
dato_buscado = input("ingresa el dato que desea buscar --> ")
buscar_dato(archivo, dato_buscado)


if __name__=='__main__':
    portada()
    buscar_dato()