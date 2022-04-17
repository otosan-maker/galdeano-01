from math import *
import random

rangoGraph={'xmin':-5,'xmax':5,'ymin':-25,'ymax':25}


def mode_graph(display,F):
    display.fill(0)
    display.hline(0, 30, 128, 1)
    display.vline(64, 0, 64, 1)
    dicEval={'X':0}
    print(F)
    
    for xStep in range (0,127):
        Xlocal=rangoGraph['xmin']+(rangoGraph['xmax']-rangoGraph['xmin'])*xStep/128
        dicEval['X']=Xlocal
        Y=eval(F,dicEval)
        yVal=60-(30+60*Y/(rangoGraph['ymax']-rangoGraph['ymin']))
        #print(xStep,Xlocal,Y,yVal)
        display.vline(xStep,ceil(yVal),1,1)
       
    display.show()

if __name__=='__main__' :
    try : F
    except NameError : F='2*X*X+5*X-5'
    mode_graph(display,F)