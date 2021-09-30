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
              "CALL": {"EXT": ["4A", "hh", "ll", "pg"],
                       "IDX": ["4B", "xb", "pg"],
                       "IDX1": ["4B", "xb", "ff", "pg"],
                       "IDX2": ["4B", "xb", "ee", "ff", "pg"],
                       "[D,IDX]": ["4B", "xb"],
                       "[IDX2]": ["4B", "xb", "ee", "ff"]},
              "CBA": {"INH": ["18", "17"]},
              "CLC": {"IMM": ["10", "FE"]},
              "CLI": {"IMM": ["10", "EF"]},
              "CLR": {"EXT": ["79", "hh", "ll"],
                      "IDX": ["69", "xb"],
                      "IDX1": ["69", "xb", "ff"],
                      "IDX2": ["69", "xb", "ee", "ff"],
                      "[D,IDX]": ["69", "xb"],
                      "[IDX2]": ["69", "xb", "ee", "ff"]},
              "CLRA": {"INH": ["87"]},
              "CLRB": {"INH": ["C7"]},
              "CLV": {"IMM": ["10", "FD"]},
              "CMPA": {"IMM": ["81", "ii"],
                       "DIR": ["91", "dd"],
                       "EXT": ["B1", "hh", "ll"],
                       "IDX": ["A1", "xb"],
                       "IDX1": ["A1", "xb", "ff"],
                       "IDX2": ["A1", "xb", "ee", "ff"],
                       "[D,IDX]": ["A1", "xb"],
                       "[IDX2]": ["A1", "xb", "ee", "ff"]},
              "CMPB": {"IMM": ["C1", "ii"],
                       "DIR": ["D1", "dd"],
                       "EXT": ["F1", "hh", "ll"],
                       "IDX": ["E1", "xb"],
                       "IDX1": ["E1", "xb", "ff"],
                       "IDX2": ["E1", "xb", "ee", "ff"],
                       "[D,IDX]": ["E1", "xb"],
                       "[IDX2]": ["E1", "xb", "ee", "ff"]},
              "COM": {},
              "COMA": {"INH": ["41"]},
              "COMB": {"INH": ["51"]},
              "CPD": {},
              "CPS": {},
              "CPX": {},
              "CPY": {},
              "DAA": {"INH": ["18", "07"]},
              "DBEQ": {"REL": ["04", "lb", "rr"]},
              "DBNE": {"REL": ["04", "lb", "rr"]},
              "DEC": {},
              "DECA": {"INH": ["43"]},
              "DECB": {"INH": ["53"]},
              "DES": {"IDX": ["1B", "9F"]},
              "DEX": {"INH": ["09"]},
              "DEY": {"INH": ["03"]},
              "EDIV": {"INH": ["11"]},
              "EDIVS": {"INH": ["18", "14"]},
              "EMACS": {"Special": ["18", "12", "hh", "ll"]},
              "EMAXD": {},
              "EMAXM": {},
              "EMIND": {},
              "EMINM": {},
              "EMUL": {"INH": ["13"]},
              "EMULS": {"INH": ["18", "13"]},
              "EORA": {},
              "EORB": {},
              "ETBL": {"IDX": ["18", "3F", "xb"]},
              "EXG": {"INH": ["B7", "eb"]},
              "FDIV": {"INH": ["18", "11"]},
              "IBEQ": {"INH": ["04", "lb", "rr"]},
              "IBNE": {"REL": ["04", "lb", "rr"]},
              "IDIV": {"INH": ["18", "10"]},
              "IDIVS": {"INH": ["18", "15"]},
              "INC": {},
              "INCA": {"INH": ["42"]},
              "INCB": {"INH": ["52"]},
              "INS": {"IDX": ["1B", "81"]},
              "INX": {"INH": ["08"]},
              "INY": {"INH": ["02"]},
              "JMP": {},
              "JSR": {},
              "LBCC": {"REL": ["18", "24", "qq", "rr"]},
              "LBCS": {"REL": ["18", "25", "qq", "rr"]},
              "LBEQ": {"REL": ["18", "27", "qq", "rr"]},
              "LBGE": {"REL": ["18", "2C", "qq", "rr"]},
              "LGBT": {"REL": ["18", "2E", "qq", "rr"]},
              "LBHI": {"REL": ["18", "22", "qq", "rr"]},
              "LBHS": {"REL": ["18", "24", "qq", "rr"]}, #  "24" repetido falta "2F"?
              "LBLS": {"REL": ["18", "23", "qq", "rr"]},
              "LBLT": {"REL": ["18", "2D", "qq", "rr"]},
              "LBMI": {"REL": ["18", "2B", "qq", "rr"]},
              "LBNE": {"REL": ["18", "26", "qq", "rr"]},
              "LBPL": {"REL": ["18", "2A", "qq", "rr"]},
              "LBRA": {"REL": ["18", "20", "qq", "rr"]},
              "LBRN": {"REL": ["18", "21", "qq", "rr"]},
              "LBVC": {"REL": ["18", "28", "qq", "rr"]},
              "LBVS": {"REL": ["18", "29", "qq", "rr"]},
              "LDAA": {},
              "LDAB": {},
              "LDD": {},
              "LDS": {},
              "LDX": {},
              "LDY": {},
              "LEAS": {},
              "LEAX": {},
              "LEAY": {},
              "LSL": {},
              "LSLA": {"INH": ["48"]},
              "LSLB": {"INH": ["58"]},
              "LSLD": {"INH": ["59"]},
              "LSR": {},
              "LSRA": {"INH": ["44"]},
              "LSRB": {"INH": ["54"]},
              "LSRD": {"INH": ["49"]},
              "MAXA": {},
              "MAXM": {},
              "MEM": {"Special": ["01"]},
              "MINA": {},
              "MINM": {},
              "MOVB": {},
              "MOVW": {},
              "MUL": {"INH": ["12"]},
              "NEG": {},
              "NEGA": {"INH": ["40"]},
              "NEGB": {"INH": ["50"]},
              "NOP": {"INH": ["A7"]},
              "ORAA": {},
              "ORAB": {},
              "ORCC": {"IMM": ["14", "ii"]},
              "PSHA": {"INH": ["36"]},
              "PSHB": {"INH": ["37"]},
              "PSHC": {"INH": ["39"]},
              "PSHD": {"INH": ["3B"]},
              "PSHX": {"INH": ["34"]},
              "PSHY": {"INH": ["35"]},
              "PULA": {"INH": ["32"]},
              "PULB": {"INH": ["33"]},
              "PULC": {"INH": ["38"]},
              "PULD": {"INH": ["3A"]},
              "PULX": {"INH": ["30"]},
              "PULY": {"INH": ["31"]},
              "REV": {"Special": ["18", "3A"]},
              "REVW": {"Special": ["18", "3B"]},
              "ROL": {},
              "ROLA": {"INH": ["45"]},
              "ROLB": {"INH": ["55"]},
              "ROR": {},
              "RORA": {"INH": ["46"]},
              "RORB": {"INH": ["56"]},
              "RTC": {"INH": ["0A"]},
              "RTI": {"INH": ["0B"]},
              "RTS": {"INH": ["3D"]},
              "SBA": {"INH": ["18", "16"]},
              "SBCA": {},
              "SBCB": {},
              "SEC": {"IMM": ["14", "01"]},
              "SEI": {"IMM": ["14", "10"]},
              "SEV": {"IMM": ["14", "02"]},
              "SEX": {"INH": ["B7", "eb"]},
              "STAA": {},
              "STAB": {},
              "STD": {},
              "STOP": {"INH": ["18", "3E"]},
              "STS": {},
              "STX": {},
              "STY": {},
              "SUBA": {},
              "SUBB": {},
              "SUBD": {},
              "SWI": {"INH": ["3F"]},
              "TAB": {"INH": ["18", "0E"]},
              "TAP": {"INH": ["B7", "02"]},
              "TBA": {"INH": ["18", "0F"]},
              "TBEQ": {"REL": ["04", "lb", "rr"]},
              "TBL": {"IDX": ["18", "3D", "xb"]},
              "TBNE": {"REL": ["04", "lb", "rr"]},
              "TFR": {"INH": ["B7", "eb"]},
              "TPA": {"INH": ["B7", "20"]},
              "TRAP": {}, # ?
              "TST": {},
              "TSTA": {"INH": ["97"]},
              "TSTB": {"INH": ["D7"]},
              "TSX": {"INH": ["B7", "75"]},
              "TSY": {"INH": ["B7", "76"]},
              "TXS": {"INH": ["B7", "57"]},
              "TYS": {"INH": ["B7", "67"]},
              "WAI": {"INH": ["3E"]},
              "WAV": {"INH": ["18", "3C"]},
              "XGDX": {"INH": ["B7", "C5"]},
              "XGDY": {"INH": ["B7", "C6"]}
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