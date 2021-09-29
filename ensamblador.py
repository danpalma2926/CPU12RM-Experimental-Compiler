"""
PRACTICA 4/20

PALMA GARCÍA DANIEL
218292653

SEMINARIO DE SOLUCION DE PROBLEMAS DE TRADUCTORES DE LENGUAJE I

"""
import pdb

directivas = {"ORG", "BSZ", "END", "FILL", "START", "DC.W", "EQU", "FCC", "DC.B", "FCB", "ZMB"} 
mnemonicos = {"ABA": {"INH": ["18","06"]}, 
              "ABX": {"IDX": ["1A", "E5"]},
              "ABY": {"IDX": ["19", "ED"]},
              "ADCA": {"IMM": ["89", "ii"],
                       "DIR": ["99", "dd"],
                       "EXT": ["B9", "hh", "ll"],
                       "IDX": ["A9", "xb"],
                       "IDX1": ["A9", "xb", "ff"],
                       "IDX2": ["A9", "xb", "ee", "ff"],
                       "[D,IDX]": ["A9", "xb"],
                       "[IDX2]": ["A9", "xb", "ee", "ff"]},
              "ADCB": {"IMM": ["C9", "ii"],
                       "DIR": ["D9", "dd"],
                       "EXT": ["F9", "hh", "ll"],
                       "IDX": ["E9", "xb"],
                       "IDX1": ["E9", "xb", "ff"],
                       "IDX2": ["E9", "xb", "ee", "ff"],
                       "[D,IDX]": ["E9", "xb"],
                       "[IDX2]": ["E9", "xb", "ee", "ff"]},
              "ADDA": {"IMM": ["8B", "ii"],
                       "DIR": ["9B", "dd"],
                       "EXT": ["BB", "hh", "ll"],
                       "IDX": ["AB", "xb"],
                       "IDX1": ["AB", "xb", "ff"],
                       "IDX2": ["AB", "xb", "ee", "ff"],
                       "[D,IDX]": ["AB", "xb"],
                       "[IDX2]": ["AB", "xb", "ee", "ff"]},
              "ADDB": {"IMM": ["CB", "ii"],
                       "DIR": ["DB", "dd"],
                       "EXT": ["FB", "hh", "ll"],
                       "IDX": ["EB", "xb"],
                       "IDX1": ["EB", "xb", "ff"],
                       "IDX2": ["EB", "xb", "ee", "ff"],
                       "[D,IDX]": ["EB", "xb"],
                       "[IDX2]": ["EB", "xb", "ee", "ff"]},
              "ADDD": {"IMM": ["C3", "ii", "jj"],
                       "DIR": ["D3", "dd"],
                       "EXT": ["F3", "hh", "ll"],
                       "IDX": ["E3", "xb"],
                       "IDX1": ["E3", "xb", "ff"],
                       "IDX2": ["E3", "xb", "ee", "ff"],
                       "[D,IDX]": ["E3", "xb"],
                       "[IDX2]": ["E3", "xb", "ee", "ff"]},
              "ANDA": {"IMM": ["84", "ii"],
                       "DIR": ["94", "dd"],
                       "EXT": ["B4", "hh", "ll"],
                       "IDX": ["A4", "xb"],
                       "IDX1": ["A4", "xb", "ff"],
                       "IDX2": ["A4", "xb", "ee", "ff"],
                       "[D,IDX]": ["A4", "xb"],
                       "[IDX2]": ["A4", "xb", "ee", "ff"]},
              "ANDB": {"IMM": ["C4", "ii"],
                       "DIR": ["D4", "dd"],
                       "EXT": ["F4", "hh", "ll"],
                       "IDX": ["E4", "xb"],
                       "IDX1": ["E4", "xb", "ff"],
                       "IDX2": ["E4", "xb", "ee", "ff"],
                       "[D,IDX]": ["E4", "xb"],
                       "[IDX2]": ["E4", "xb", "ee", "ff"]},
              "ANDCC": {"IMM": ["10", "ii"]},
              "ASL":  {"EXT": ["78", "hh", "ll"],
                       "IDX": ["68", "xb"],
                       "IDX1": ["68", "xb", "ff"],
                       "IDX2": ["68", "xb", "ee", "ff"],
                       "[D,IDX]": ["68", "xb"],
                       "[IDX2]": ["68", "xb", "ee", "ff"]}, 
              "ASLA": {"INH": ["48"]},
              "ASLB": {"INH": ["58"]},
              "ASLD": {"INH": ["59"]},
              "ASR":  {"EXT": ["77", "hh", "ll"],
                       "IDX": ["67", "xb"],
                       "IDX1": ["67", "xb", "ff"],
                       "IDX2": ["67", "xb", "ee", "ff"],
                       "[D,IDX]": ["67", "xb"],
                       "[IDX2]": ["67", "xb", "ee", "ff"]},
              "ASRA": {"INH": ["47"]},
              "ASRB": {"INH": ["57"]},
              "BCC": {"REL": ["24", "rr"]},
              "BCLR": {"DIR": ["4D", "dd", "mm"],
                       "EXT": ["1D", "hh", "ll", "mm"],
                       "IDX": ["0D", "xb", "mm"],
                       "IDX1": ["0D", "xb", "ff", "mm"],
                       "IDX2": ["0D", "xb", "ee", "ff", "mm"]},
              "BCS": {"REL": ["25", "rr"]},
              "BEQ": {"REL": ["27", "rr"]},
              "BGE": {"REL": ["2C", "rr"]},
              "BGND": {"INH": ["00"]},
              "BGT": {"REL": ["2E", "rr"]},
              "BHI": {"REL": ["22", "rr"]},
              "BHS": {"REL": ["24", "rr"]},
              "BITA": {"IMM": ["85", "ii"],
                       "DIR": ["95", "dd"],
                       "EXT": ["B5", "hh", "ll"],
                       "IDX": ["A5", "xb"],
                       "IDX1": ["A5", "xb", "ff"],
                       "IDX2": ["A5", "xb", "ee", "ff"],
                       "[D,IDX]": ["A5", "xb"],
                       "[IDX2]": ["A5", "xb", "ee", "ff"]},
              "BITB": {"IMM": ["C5", "ii"],
                       "DIR": ["D5", "dd"],
                       "EXT": ["F5", "hh", "ll"],
                       "IDX": ["E5", "xb"],
                       "IDX1": ["E5", "xb", "ff"],
                       "IDX2": ["E5", "xb", "ee", "ff"],
                       "[D,IDX]": ["E5", "xb"],
                       "[IDX2]": ["E5", "xb", "ee", "ff"]},
              "BLE": {"REL": ["2F", "rr"]},
              "BLO": {"REL": ["25", "rr"]},
              "BLS": {"REL": ["23", "rr"]},
              "BLT": {"REL": ["2D", "rr"]},
              "BMI": {"REL": ["2B", "rr"]},
              "BNE": {"REL": ["26", "rr"]},
              "BPL": {"REL": ["2A", "rr"]},
              "BRA": {"REL": ["20", "rr"]},
              "BRCLR": {"DIR": ["4F", "dd", "mm", "rr"],
                       "EXT": ["1F", "hh", "ll", "mm", "rr"],
                       "IDX": ["0F", "xb", "mm", "rr"],
                       "IDX1": ["0F", "xb", "ff", "mm", "rr"],
                       "IDX2": ["0F", "xb", "ee", "ff", "mm", "rr"]},
              "BRN": {"REL": ["21", "rr"]},
              "BRSET": {"DIR": ["4E", "dd", "mm", "rr"],
                       "EXT": ["1E", "hh", "ll", "mm", "rr"],
                       "IDX": ["0E", "xb", "mm", "rr"],
                       "IDX1": ["0E", "xb", "ff", "mm", "rr"],
                       "IDX2": ["0E", "xb", "ee", "ff", "mm", "rr"]},
              "BSET": {"DIR": ["4C", "dd", "mm"],
                       "EXT": ["1C", "hh", "ll", "mm"],
                       "IDX": ["0C", "xb", "mm"],
                       "IDX1": ["0C", "xb", "ff", "mm"],
                       "IDX2": ["0C", "xb", "ee", "ff", "mm"]},
              "BSR": {"REL": ["07", "rr"]},
              "BVC": {"REL": ["28", "rr"]},
              "BVS": {"REL": ["29", "rr"]},

            }

def conv_decimal(dato):
    if dato.startswith("$"):
        return int(dato.replace("$", "0x"), 16)
    elif dato.startswith("@"):
        return int(dato.replace("@", "0o"), 8)
    elif dato.startswith("%"):
        return int(dato.replace("%", "0b"), 2)
    else:
        return int(dato)

def conv_hexadecimal(dato):
    pass

def interpretar_directiva(lista_mnemonicos, archivo_lst, org):
    if lista_mnemonicos[0] == "ORG":
        org = conv_decimal(lista_mnemonicos[1])
        archivo_lst += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), "-- --", lista_mnemonicos[0]) + "\n"
        return archivo_lst, org
    elif lista_mnemonicos[0] == "BSZ":
        bytes_a_asignar = int(lista_mnemonicos[1])
        archivo_lst += "{:9s}".format("0x" + hex(org)[2:].zfill(4))
        for byte in range(0, bytes_a_asignar):
            archivo_lst += "{:2s}".format("00") + " "
        archivo_lst += "{:>16}".format(lista_mnemonicos[0]) + "\n"
        org += bytes_a_asignar
        return archivo_lst, org
    elif lista_mnemonicos[0] == "FILL":
        operadores = lista_mnemonicos[1].split(",")
        constante = operadores[0]
        bytes_a_asignar = int(operadores[1])
        archivo_lst += "{:9s}".format("0x" + hex(org)[2:].zfill(4))
        for byte in range(0, bytes_a_asignar):
            archivo_lst += "{:2s}".format(hex(int(constante))[2:].zfill(2).upper()) + " "
        archivo_lst += "{:>16}".format(lista_mnemonicos[0]) + "\n"
        org += bytes_a_asignar

        return archivo_lst, org
    elif lista_mnemonicos[0] == "START":
        org = 0
        archivo_lst += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), "-- --", lista_mnemonicos[0]) + "\n"
        return archivo_lst, org
    elif lista_mnemonicos[0] == "DC.W":
        if len(lista_mnemonicos) == 1:
            archivo_lst += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), "00 00", lista_mnemonicos[0]) + "\n"
            org += 2
        else:
            bytes_a_asignar = lista_mnemonicos[1].split(",")
            archivo_lst += "{:9s}".format("0x" + hex(org)[2:].zfill(4))
            for byte in bytes_a_asignar:
                if int(byte) < 256:
                    archivo_lst += "{:2s}".format("00") + " "
                    archivo_lst += "{:2s}".format(hex(int(byte))[2:].zfill(2).upper()) + " "
                else:
                    # Implementar manejo de valores mayores a 255
                    pass
            archivo_lst += "{:>16}".format(lista_mnemonicos[0]) + "\n"
            org += len(bytes_a_asignar) * 2
        return archivo_lst, org
    elif lista_mnemonicos[0] == "DC.B":
        #pdb.set_trace()
        if len(lista_mnemonicos) == 1:
            archivo_lst += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), "00", lista_mnemonicos[0]) + "\n"
            org += 1
        # elif len(lista_mnemonicos) == 2:
        #     org += 1
        #     archivo_lst += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), hex(int(lista_mnemonicos[1])), lista_mnemonicos[0]) + "\n"
        else:
            bytes_a_asignar = lista_mnemonicos[1].split(",")
            #pdb.set_trace()
            archivo_lst += "{:9s}".format("0x" + hex(org)[2:].zfill(4))
            for byte in bytes_a_asignar:
                archivo_lst += "{:2s}".format(hex(int(byte))[2:].zfill(2).upper()) + " "
            archivo_lst += "{:>16}".format(lista_mnemonicos[0]) + "\n"
            org += len(bytes_a_asignar)
        return archivo_lst, org
    elif lista_mnemonicos[0] == "FCC":
        cadena = lista_mnemonicos[1].replace("/", "")
        archivo_lst += "{:9s}".format("0x" + hex(org)[2:].zfill(4))
        for caracter in cadena:
            archivo_lst += "{:2s}".format(hex(int(ord(caracter)))[2:].zfill(2).upper()) + " "
        archivo_lst += "{:>16}".format(lista_mnemonicos[0]) + "   '" + cadena + "'" + "\n"
        org += len(cadena)

        return archivo_lst, org
    elif lista_mnemonicos[0] == "FCB":
        if int(lista_mnemonicos[1]) < 256:
            archivo_lst += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), hex(int(lista_mnemonicos[1]))[2:].zfill(2).upper(), lista_mnemonicos[0]) + "\n"
        else:
            # Implementar manejo de valores mayores a 255
            pass
        org += 1
        return archivo_lst, org
    elif lista_mnemonicos[0] == "END":
        archivo_lst += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), "-- --", lista_mnemonicos[0]) + "\n"
        return archivo_lst, org

def interpretar_instruccion(lista_mnemonicos, archivo_lst, org):
                # Si solo tiene un argumento, asumir que es de tipo inherente
    bytes_instruccion = {}
    if len(lista_mnemonicos) == 1:
        try: 
            bytes_instruccion = mnemonicos[lista_mnemonicos[0]]["INH"]
        except KeyError as e:
            archivo_lst += f"'{lista_mnemonicos[0]}' no puede ser de tipo inherente"
            #break;
    # Si el segundo argumento contiene un numeral al principio, asumir que es de tipo inmediato 
    elif lista_mnemonicos[1].startswith("#"):
        try:
            bytes_instruccion = mnemonicos[lista_mnemonicos[0]]["IMM"]
        except KeyError as e:
            archivo_lst += f"'{lista_mnemonicos[0]}' no puede ser de tipo inmediato"
            #break;
    # Si no cumple con las 2 condiciones anteriores, entonces
    else:
        valor = conv_decimal(lista_mnemonicos[1])
        try:
            if valor < 256:
                bytes_instruccion = mnemonicos[lista_mnemonicos[0]]["DIR"]
            elif valor < 65536:
                bytes_instruccion = mnemonicos[lista_mnemonicos[0]]["EXT"]
        except KeyError as e:
            archivo_lst += f"'{lista_mnemonicos[0]} {lista_mnemonicos[1]}' no es compatible con los modos de direccionamiento soportados"
            #break;
    byte_str = ""
    for byte in bytes_instruccion:
        byte_str += byte + " "
    archivo_lst += "{:8s} {:14s} {:6} {}".format("0x" + hex(org)[2:].zfill(4), byte_str, lista_mnemonicos[0], "LI=" + str(len(bytes_instruccion))) + "\n"
    org += len(bytes_instruccion)
    return archivo_lst, org

def main():
    # Abrir archivo y separar por lineas
    with open("P6.asm", "r") as file:
        linea_instrucciones = file.readlines()
    

    # Implementar manejo de errores aqui

    org = 0
    archivo_lista = ""
    etiquetas = {}
    #pdb.set_trace()
    # Ejecutar línea por línea
    for line in linea_instrucciones:
        # Convertir linea en lista de mnemonicos y valores
        instrucciones_linea = line.replace("\n", "").split(" ")
        #pdb.set_trace()
        # Si la linea actual cuenta con el mnemonico ORG, establecer como referencia a ese valor
        if instrucciones_linea[0] in directivas:
            archivo_lista, org = interpretar_directiva(instrucciones_linea, archivo_lista, org)
            #org = conv_decimal(instrucciones_linea[1])
            #archivo_lista += "{:8s} {:14s} {}".format("0x" + hex(org)[2:].zfill(4), "-- --", instrucciones_linea[0]) + "\n"
        # Si no, revisar si el primer argumento de la línea es un mnemónico válido
        elif instrucciones_linea[0] in mnemonicos:
            # Si solo tiene un argumento, asumir que es de tipo inherente
            archivo_lista, org = interpretar_instruccion(instrucciones_linea, archivo_lista, org)
            # if len(instrucciones_linea) == 1:
            #     try: 
            #         bytes_instruccion = mnemonicos[instrucciones_linea[0]]["INH"]
            #     except KeyError as e:
            #         archivo_lista += f"'{instrucciones_linea[0]}' no puede ser de tipo inherente"
            #         break;
            # # Si el segundo argumento contiene un numeral al principio, asumir que es de tipo inmediato 
            # elif instrucciones_linea[1].startswith("#"):
            #     try:
            #         bytes_instruccion = mnemonicos[instrucciones_linea[0]]["IMM"]
            #     except KeyError as e:
            #         archivo_lista += f"'{instrucciones_linea[0]}' no puede ser de tipo inmediato"
            #         break;
            # # Si no cumple con las 2 condiciones anteriores, entonces
            # else:
            #     valor = conv_decimal(instrucciones_linea[1])
            #     try:
            #         if valor < 256:
            #             bytes_instruccion = mnemonicos[instrucciones_linea[0]]["DIR"]
            #         elif valor < 65536:
            #             bytes_instruccion = mnemonicos[instrucciones_linea[0]]["EXT"]
            #     except KeyError as e:
            #         archivo_lista += f"'{instrucciones_linea[0]} {instrucciones_linea[1]}' no es compatible con los modos de direccionamiento soportados"
            #         break;
            # byte_str = ""
            # for byte in bytes_instruccion:
            #     byte_str += byte + " "
            # archivo_lista += "{:8s} {:14s} {:6} {}".format("0x" + hex(org)[2:].zfill(4), byte_str, instrucciones_linea[0], "LI=" + str(len(bytes_instruccion))) + "\n"
            # org += len(bytes_instruccion)
            continue
        else:
            if instrucciones_linea[0] not in etiquetas:
                if instrucciones_linea[1] == "EQU":
                    etiquetas[instrucciones_linea[0]] = hex(int(instrucciones_linea[2]))[2:].zfill(4)
                else:
                    if instrucciones_linea[1] != 'END':
                        etiquetas[instrucciones_linea[0]] = hex(int(instrucciones_linea[1]))[2:].zfill(4)
                        archivo_lista, org = interpretar_instruccion(instrucciones_linea[1:], archivo_lista, org)
                    else:
                        archivo_lista, org = interpretar_directiva(instrucciones_linea[1:], archivo_lista, org)
                        etiquetas[instrucciones_linea[0]] = hex(org)[2:].zfill(4)
                        break;
            else:
                print("Etiqueta repetida!!!")
                break
    print(archivo_lista)
    print(etiquetas)
    with open("P6.lst", "w") as file:
        file.write(archivo_lista)
    
    with open("p6.tabsim", "w") as file:
        for k, v in etiquetas.items():
            file.writelines(v + "\t" + k + "\n")
    
if __name__ == "__main__":
    main()