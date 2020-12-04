#Convertir horas
print("Programa para convertir las horas en formato de"
      "24 a formato de 12 horas \n ")

periodo="a.m"
#Datos de entrada
h24=int(input("Ingrese la hora en formato  24 a transofrmar"))

m24=int(input("Ingrese los minutos a transformar:  "))
#Proceso
if h24<24 and h24>0:
      if h24 >= 0 and h24 <= 24 and m24 >=0 and m24 <= 60:
            if m24==60:
                  h24=h24+1
                  m24=0

            else:
                  m12=m24

            if h24>=12:
                  if h24==12:
                        h12=h24
                  else:
                        h12=h24-12
                  periodo="p.m"

            print(f"El tiempo de {h24} horas y {m24} minutos en formato de 24 horas ")
            print(f"Equivale a {h12} horas y {m12}minutos {periodo} ")

else:
      if h24==0:
            h12=h24
            if m24==60:
                  h12=h12+1
                  m24=0
            else:
                m12=m24

            print(f"El tiempo de {h24} horas y {m24} minutos en formato de 24 horas ")
            print(f"Equivale  {h12} horas y {m12} minutos  {periodo} ")

      else:
            if h24==24:
                  h12=0
                  if m24==60:
                        h12=h12+1
                        m24=0

                  else:
                        m12=m24

                  print(f"El tiempo de {h24} horas y {m24} minutos en formato de 24 horas ")
                  print(f"Equivale  {h12} horas y {m12} minutos  {periodo} ")
