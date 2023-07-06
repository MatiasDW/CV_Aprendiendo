from django.http import HttpResponse
import datetime
from django.template import Template, Context 
#from django.shortcuts import render


class Persona(object):
    
    def __init__(self, estudios, institucion):
        
        self.estudios = estudios
        self.institucion = institucion


def saludo(request):
    
    p1 = Persona("Estudiante Ingeniaria en Data science, con estudios previos en ingenieria civil industrial 50% de la malla cursada", "Universitat Carlemany, España")
    skills = ["Python", "SQL", "Html", "Pandas", "Django", "React", "Javascript", "Machine Learning", "Excel", "Numpy", "Linux", "Chatgpt"]

    ahora = datetime.datetime.now()
    nombre= "Matias"
    apellido = "Davila"
    doc_externo = open("C:/Users/Matias/proyecto1/mi_cv/plantillas/miplantilla.html")
    plt = Template(doc_externo.read())   
    doc_externo.close()
    ctx= Context({"nombre_persona": nombre,  "apellido_persona": apellido, "momento_actual": ahora, "estudios": p1.estudios, "institucion": p1.institucion,
                  "skills_show":skills})
    documento = plt.render(ctx)
        
    return HttpResponse(documento)


def dameFecha(request):
    
    fecha_actual = datetime.datetime.now()
    
    documento = """ <html>
    <body>
    <h1>
    Fecha y hora actuales %s 
    </h1>
    </body>
    </html>""" %fecha_actual
    
    return HttpResponse(documento)

def calculaEdad(request, agno):
    
    edadActual = 18
    periodo = agno - 2023
    edadFutura = edadActual + periodo
    documento = "<html><body><h2>En el ano %s tendras %s</h2></body></html>" %(agno, edadFutura)
    
    return HttpResponse(documento)