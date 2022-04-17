from  keypad import get_key
from math import *
import screen

linea1=""
valor=""
strQ=""
idMode=0
strMode=["Calculadora","Funciones","Alpha"]
strDisplay="Text"
ans=0
while 1==1 :
    strQ=get_key(Files,Columns,Caracteres,idMode)
    if strQ != "" :
        if strQ == "del" :
            linea1 = linea1[:-1]
        elif strQ == "eval" :
            try:
                ans = eval(linea1)
                valor = str(ans)
            except:
                valor = "Eval error"
        elif strQ == "exe" :
            try:
                exec(linea1)
            except:
                valor="Exec error"
            valor = "EXECUTED"
        elif strQ == "graph" :
            print("graph")
            if strDisplay=="Text":
                strDisplay="graph"
            else:
                strDisplay="Text"
        elif strQ == "mode" :
            idMode=idMode+1
            if (idMode > len(strMode)-1 ):
                idMode=0
        else :
            linea1 = linea1 + strQ
        
        if strDisplay=="Text":
            display.fill(0)
            display.text(""+linea1,4,10)
            #display.hline(50, 20, 120, 1)
            display.text("= "+valor,20,22)
            #display.hline(50, 38, 120, 1)
            display.hline(4, 55, 120, 1) 
            display.text("* "+strMode[idMode],10,57)
            display.show()
        else :
            try : F
            except NameError : F='2*X*X+5*X-5'
            screen.mode_graph(display,F)
        
