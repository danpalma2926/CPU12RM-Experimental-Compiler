START
ABA
VAR2 ADCA #@30
ORG $4000
ABA
INICIO ADCA #30
ADCA 30
ADCA 300
PUERTA EQU $1000
VAR1 EQU 100
ADDD #15
ADDD 15
BNE INICIO
BNE FIN
DBEQ A,INICIO
DBEQ B,INICIO
DBEQ B,FIN
LBNE VAR2
DC.B 5,5
DC.W 10,10
FIN BSZ 3
END