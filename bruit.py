from scipy  import signal
import numpy as np
import matplotlib.pyplot as plt
redonnance = lambda u1,u2,u3,u4: ([(u2+u3+u4)%2,(u1+u3+u4)%2,(u1+u2+u4)%2])
def canal_com(mot_code):
    bruit= np.random.uniform(0,1,len(mot_code))
    mess_bruit= mot_code+bruit
    mess_clair=mess_bruit-bruit
    x = np.linspace(0, len(mot_code), len(mot_code))
    plt.plot(x, mot_code)
    plt.title("message sans bruit")
    plt.show()
    plt.plot(x, mess_bruit)
    plt.title("message avec bruit")
    plt.show()
    plt.plot(x, mess_clair)
    plt.title("message décodé")
    plt.show()
    redon_recu=[mess_clair[4],mess_clair[5],mess_clair[6]]
    redon_cal=redonnance(mess_clair[0],mess_clair[1],mess_clair[2],mess_clair[3])
    syndrome= [round((redon_recu[i]+redon_cal[i])%2,0) for i in range(3)]
    print("la redonnance est",syndrome)
    if syndrome.count(1)==2:
        print("erreur de transmission entre y1 ou y2 ou y3")
        position=syndrome.index(0)
        mess_clair[position]=(mess_clair[position]+1)%2
    elif syndrome.count(1)==3:
        print("erreur de transmission au niveau de y4")
        mess_clair[3]=(mess_clair[3]+1)%2
    elif syndrome.count(1)==1:
         print("erreur de transmission entre y5 ou y6 ou y7")
    else:
         print("pas d'erreur de transmission")
    print("le code corrigé est : ", mess_clair)
        
