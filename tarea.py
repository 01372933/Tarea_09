#Encoding: UTF-8
#Blanca Flor
#Tarea 9- Archivos
from Graphics import*
'''#Define unavetana de 800x600
v 800 600 "Archivos"
#Rectangulo de 0,0 a 799,599 (Toda la ventana) relleno de verde
r 0,0 799,599 green
# Otro rectangulo blanco de 20,20 a 780,780 blanco
r 20,20 780,580 white
# Lineas
l 20 20 400 380
l 780 20 400 380
l 20 580 400 200 lightgray
l 780 580 400 200 lightgray
#Circulo en el centro 400,300 con radio 100 color cafe
c 400 300 100 brown
'''

def main():
    instrucciones=open("tarea.txt","r")
    instrucciones.seek(5)
    cadena=[]
    for linea in instrucciones:
       if linea!="\n":
            if linea!= "#":
                linea.split()
                cadena += linea
#aegun esto me debe de dar una lsita de 39 casillas de la 0-38                
        #for i in range(40):
            #posicion=i
#aquí planeaba, en vez de poner de uno por uno (0,1,2,3,6...) hacer un for para que me generara estos numeros
#pero no sé si funciones y además creo que entonces todos tendrían en el primer ciclo 0, en el segundo ciclo todos mis variables i
#serian 1 y así. y luego pensé en asignarselos  a una variablee para que la variable fuera cambiando, pero volví a los mismo
#cadena[posision]=Window(cadena[posicion],cadena[posicion],cadena[posicion])     
    cadena[0]=Window((cadena[1]),(cadena[2]),cadena[3])
    cadena[4]=Rectangle(int(cadena[5]),int(cadena[6]))
    cadena[4].Color(str(cadena[7]))
    cadena[4].draw(cadena[0])
    cadena[8]=Rectangle(int(cadena[9]),int(cadena[10]))
    cadena[8].Color(str(cadena[11]))
    cadena[8].draw(cadena[0])
    cadena[12]=Line((int(cadena[13]),int(cadena[14])),(int(cadena[15]),int(cadena[16])))
    cadena[12].draw(cadena[0])
    cadena[17]=Line((int(cadena[18]),int(cadena[19])),(int(cadena[20]),int(cadena[21])))
    cadena[17].draw(cadena[0])
    cadena[22]=Line((int(cadena[23]),int(cadena[24])),(int(cadena[25]),int(cadena[26])))
    cadena[22].Color(str(cadena[27]))
    cadena[22].draw(cadena[0])
    cadena[28]=Line((int(cadena[29]),int(cadena[30])),(int(cadena[31]),int(cadena[32])))
    cadena[28].Color(str (cadena[33]))
    cadena[28].draw(cadena[0])
    cadena[34]=Circle((int(cadena[35]),int(cadena[36])),int(cadena[37]))
    cadena[34].Color(str(cadena[38]))
    cadena[34].draw(cadena[0])
    
  #Creo que esto es lo que pedia la tarea       
  #medio me confundieron las instrucciones       
  # mis programas nunca corren profe, y me es muy hartante el saber que no pienso con suficiente logica para un
  #simple programa. Pero eso es punto y aparte.
  #ya cambié un buen de cosas y si reparo una otra esta mal
  #por cienrto, no encntre sobre los comentarios, de verdad que si busqué en la pagina pero esta todo bien raro
  #me marca no se que error que no le entiendo que intenta decirme 
  #veamos como me va 
    instruciones.close()
main()
