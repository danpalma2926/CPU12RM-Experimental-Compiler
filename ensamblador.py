"""
PRACTICA 4/18

PALMA GARCÍA DANIEL
218292653

SEMINARIO DE SOLUCION DE PROBLEMAS DE TRADUCTORES DE LENGUAJE I

"""
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
              "ADDD": {"IMM": ["C3", "ii"],
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
              "ASRB": {"INH": ["57"]}
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


def main():
    # Abrir archivo y separar por lineas
    with open("test.asm", "r") as file:
        linea_instrucciones = file.readlines()
    
    # Verificar que comience con ORG y que termine con END
    # Implementar manejo de errores aqui

    org = 0
    # Ejecutar línea por línea
    for line in linea_instrucciones:
        # Convertir linea en lista de mnemonicos y valores
        instrucciones_linea = line.replace("\n", "").split(" ")
        # Si la linea actual cuenta con el mnemonico ORG, establecer como referencia a ese valor
        if instrucciones_linea[0] == "ORG":
            org = conv_decimal(instrucciones_linea[1])
            print(instrucciones_linea[0], instrucciones_linea[1])
        elif instrucciones_linea[0] in mnemonicos:
            if len(instrucciones_linea) == 1:
                bytes_instruccion = mnemonicos[instrucciones_linea[0]]["INH"]
            elif instrucciones_linea[1].startswith("#"):
                bytes_instruccion = mnemonicos[instrucciones_linea[0]]["IMM"]
            else:
                valor = conv_decimal(instrucciones_linea[1])
                if valor < 255:
                    bytes_instruccion = mnemonicos[instrucciones_linea[0]]["DIR"]
                elif valor < 65536:
                    bytes_instruccion = mnemonicos[instrucciones_linea[0]]["EXT"]
            print(hex(org), bytes_instruccion, instrucciones_linea[0]) 
            org += len(bytes_instruccion)
            continue
        elif instrucciones_linea[0] == "END":
            print(hex(org), "END")
            continue
        else:
            print("Mnemonico no soportado!!!")
            break;

if __name__ == "__main__":
    main()