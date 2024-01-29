from matplotlib.markers import MarkerStyle
import numpy as np
import matplotlib as mpl

from matplotlib import pyplot as plt


""" definiere die gegebenen Konstanten"""

m = 4 * 10**4       # Masse Saturn, es wird angenommen der Saturn ruht im Ursprung

# Masse, Anfangsort, Anfangsgeschwindigkeit von Epithemeus
m_1 = 1                                
x_0_1 = -155  
y_0_1 = 0
v_0_x_1 = 0
v_0_y_1 = -16.1

# Masse, Anfangsort, Anfangsgeschwindigkeit von Janus
m_2 = 4             
x_0_2 = 150  
y_0_2 = 0
v_0_x_2 = 0
v_0_y_2 = 16.3

t_max = 3000              # Zeit bis zu der gerechnet werden soll
delta_t = 0.1           # kleiner Zeitschritt
unteriterationen = 100  # variablen implizit gegeben, wird angenähert indem immer wieder eingesetzt wird und wieder ausgerechnet wird

"""definiere die zu lösenden DGL"""

def v_dot_x_1(x_1, y_1, x_2, y_2): #Beschleunigung von Epimetheus in X-Richtung          
    return -m_2*(x_1-x_2) * ((x_1-x_2)**2 + (y_1-y_2)**2)**(-3/2) - m*x_1 * (x_1**2 + y_1**2)**(-3/2)

def v_dot_y_1(x_1, y_1, x_2, y_2):  #Beschleunigung von Epimetheus in Y-Richtung          
    return   -m_2*(y_1-y_2) * ((x_1-x_2)**2 + (y_1-y_2)**2)**(-3/2) - m*y_1 * (x_1**2 + y_1**2)**(-3/2)         
    
def v_dot_x_2(x_1, y_1, x_2, y_2):  #Beschleunigung von Janus in X-Richtung          
    return  -m*x_2 * (x_2**2 + y_2**2)**(-3/2) + m_1*(x_1-x_2) * ((x_1-x_2)**2 + (y_1 - y_2)**2)**(-3/2)

def v_dot_y_2(x_1, y_1, x_2, y_2):  #Beschleunigung von Janus in Y-Richtung          
    return  m_1*(x_1-x_2) * ((x_1-x_2)**2 + (y_1-y_2)**2)**(-3/2) - m*y_2 * (x_2**2+y_2**2)**(-3/2) 


"""löse die DGL"""


def Euler():                            #explizites und implizites Eulerverfahren

    """Berechnet die einzelnen Werte für die Variablen und gibt sie als Listen wieder aus"""

    t_plot = np.empty(0)                         #kreieren von Listen für die Werte
    x_1_plot = np.empty(0)
    y_1_plot = np.empty(0)
    x_2_plot = np.empty(0)
    y_2_plot = np.empty(0)

    t = 0                               #Variablen auf den Anfangswert setzen
    v_n_x_1 = v_0_x_1
    v_n_y_1 = v_0_y_1
    v_n_x_2 = v_0_x_2
    v_n_y_2 = v_0_y_2

    x_n_1 = x_0_1
    y_n_1 = y_0_1
    x_n_2 = x_0_2
    y_n_2 = y_0_2

    while t <= t_max:                   #Schleife zur Berechnung der Numerischen Werte

        x_1_plot = np.append(x_1_plot, x_n_1)          #Wert in Liste eintragen
        y_1_plot = np.append(y_1_plot, y_n_1)
        x_2_plot = np.append(x_2_plot, x_n_2)
        y_2_plot = np.append(y_2_plot, y_n_2)
        t_plot = np.append(t_plot, t)


        v_nplus_x_1 = v_n_x_1 + v_dot_x_1(x_n_1, y_n_1, x_n_2, y_n_2) * delta_t     #die nächsten Werte berechnen
        v_nplus_y_1 = v_n_y_1 + v_dot_y_1(x_n_1, y_n_1, x_n_2, y_n_2) * delta_t
        v_nplus_x_2 = v_n_x_2 + v_dot_x_2(x_n_1, y_n_1, x_n_2, y_n_2) * delta_t
        v_nplus_y_2 = v_n_y_2 + v_dot_y_2(x_n_1, y_n_1, x_n_2, y_n_2) * delta_t

        x_nplus_1 = x_n_1 + v_nplus_x_1 * delta_t
        y_nplus_1 = y_n_1 + v_nplus_y_1 * delta_t
        x_nplus_2 = x_n_2 + v_nplus_x_2 * delta_t
        y_nplus_2 = y_n_2 + v_nplus_y_2 * delta_t


        v_n_x_1 = v_nplus_x_1           #Wieder die Laufvariablen verwenden
        v_n_y_1 = v_nplus_y_1  
        v_n_x_2 = v_nplus_x_2  
        v_n_y_2 = v_nplus_y_2  
        
        x_n_1 = x_nplus_1
        y_n_1 = y_nplus_1
        x_n_2 = x_nplus_2
        y_n_2 = y_nplus_2

        t = t + delta_t                 #Zeit einen Schritt weiter gehen
        
    return x_1_plot, y_1_plot, x_2_plot, y_2_plot, t_plot 

x_1_plot, y_1_plot, x_2_plot, y_2_plot, t_plot = Euler()

'''
def plot_Bahnen():

    plt.plot(x_1_plot, y_1_plot)
    plt.plot(x_2_plot, y_2_plot)
    plt.axis([-200, 200 , -200, 200]) 
    plt.show()
    

plot_Bahnen()
'''

def plot_Distanzen():
    
    distance_janus_epimetheus = np.sqrt((x_1_plot - x_2_plot)**2 + (y_1_plot - y_2_plot)**2)
    distance_saturn_epimetheus = np.sqrt(x_1_plot**2 + y_1_plot**2)
    distance_saturn_janus = np.sqrt(x_2_plot**2 + y_2_plot**2)

    plt.plot(t_plot, distance_janus_epimetheus, label="Abstand Janus-Epimetheus")
    plt.plot(t_plot, distance_saturn_epimetheus, label="Abstand Saturn-Epimetheus")
    plt.plot(t_plot, distance_saturn_janus, label="Abstand Saturn-Janus")
    plt.xlabel("Zeit")
    plt.ylabel("Distanz")
    plt.legend(loc="upper right")
    plt.title("Grafik der Abstände der Himmelskörper")
    plt.axis([0, t_max, 0, 320]) 

    plt.show()
 
plot_Distanzen()





