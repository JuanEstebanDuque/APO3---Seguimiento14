from experta import *
import tkinter as tk
from tkinter import ttk

class User(Fact):
  def user(self, name, lastname, age, carreer):
    super().__init__()
    self.name = name
    self.lastname = lastname
    self.age = age
    self.email = carreer 
    pass

class Carreer(Fact):
  def carreer(self, name, price):
    super().__init__()
    self.name = name
    self.price = price
    pass

class Skill(Fact):
  def skill(self, names):
    super().__init__()
    self.names = names
    pass

class Weakness(Fact):
  def weakness(self, names):
    super().__init__()
    self.names = names
    pass

class Competence(Fact):
  def competence(self, names):
    super().__init__()
    self.names = names
    pass

class CarreerExpert(KnowledgeEngine):
  @DefFacts()
  def needed_data():
    yield Carreer(name="Ingeniería en sistemas", price=12960000)
    yield Carreer(name="Diseño de medios interactivos", price=12960000)
    yield Carreer(name="Mercadeo internacional", price=13580000)
    yield Carreer(name="Finanzas", price=13580000)
    yield Carreer(name="Derecho", price=12960000)
    yield Carreer(name="Psicología", price=11450000)

  

def main():

  nameUser = ""
  lastNameUser = ""
  ageUser = ""
  carreerUser = ""

  user_competence_list = []

  root = tk.Tk()

  name = tk.StringVar()
  lastName = tk.StringVar()
  age = tk.IntVar()
  carreer = tk.StringVar()

  
  myFrame = tk.Frame(root, width=1200, height=900, padx=30, pady=30)
  myFrame.pack()

  tk.Label(myFrame, text="Información personal", font=("Times new roman", 20)).grid(row=0, column=0, sticky="w", pady=20)

  tk.Label(myFrame, text="Nombre", font=("Arial", 10)).grid(row=1, column=0, sticky="w")
  inputName = tk.Entry(myFrame, textvariable=name)
  inputName.config(width=50)
  inputName.grid(row=2, column=0, pady=5, sticky="w")

  tk.Label(myFrame, text="Apellido", font=("Arial", 10)).grid(row=1, column=1, padx= 20, sticky="w")
  inputLastName = tk.Entry(myFrame)
  inputLastName.config(width=50)
  inputLastName.grid(row=2, column=1, pady=5, padx=20)

  tk.Label(myFrame, text="Edad", font=("Arial", 10)).grid(row=3, column=0, sticky="w")
  inputAge = tk.Entry(myFrame)
  inputAge.config(width=50)
  inputAge.grid(row=4, column=0, sticky="w")  

  tk.Label(myFrame, text="Carrera", font=("Arial", 10)).grid(row=3, column=1, padx=20, sticky="w")
  inputEmail = tk.Entry(myFrame)
  inputEmail.config(width=50)
  inputEmail.grid(row=4, column=1)  


  tk.Label(myFrame, text="Información de la carrera", font=("Times new roman", 20)).grid(row=5, column=0, sticky="w", pady=20)

  cb_Creatividad = tk.IntVar()
  cb_Visual = tk.IntVar()
  cb_Logico = tk.IntVar()
  cb_Matematicas = tk.IntVar()
  cb_Oportunidades = tk.IntVar()
  cb_Analitico = tk.IntVar()
  cb_Problemas = tk.IntVar()
  cb_Datos = tk.IntVar()
  cb_Persudir = tk.IntVar()
  cb_Negociar = tk.IntVar()
  cb_Empatia = tk.IntVar()
  cb_Humano = tk.IntVar()

  def cbAptitudesEscogida():

    if cb_Creatividad.get() == 1:
      user_competence_list.append("Creatividad y pensamiento innovador.")
    else:
      if "Creatividad y pensamiento innovador." in user_competence_list:
        user_competence_list.remove("Creatividad y pensamiento innovador.")

    if cb_Visual.get() == 1:
      user_competence_list.append("Habilidad para el diseño visual.")
    else:
      if "Habilidad para el diseño visual." in user_competence_list:
        user_competence_list.remove("Habilidad para el diseño visual.")

    if cb_Logico.get() == 1:
      user_competence_list.append("Pensamiento lógico.")
    else:
      if "Pensamiento lógico." in user_competence_list:
        user_competence_list.remove("Pensamiento lógico.")

    if cb_Matematicas.get() == 1:
      user_competence_list.append("Destreza en matemáticas.")
    else:
      if "Destreza en matemáticas." in user_competence_list:
        user_competence_list.remove("Destreza en matemáticas.")

    if cb_Oportunidades.get() == 1:
      user_competence_list.append("Capacidad para identificar oportunidades.")
    else:
      if "Capacidad para identificar oportunidades." in user_competence_list:
        user_competence_list.remove("Capacidad para identificar oportunidades.")

    if cb_Analitico.get() == 1:
      user_competence_list.append("Pensamiento analítico.")
    else:
      if "Pensamiento analítico." in user_competence_list:
        user_competence_list.remove("Pensamiento analítico.")

    if cb_Problemas.get() == 1:
      user_competence_list.append("Capacidad para resolver problemas.")
    else:
      if "Capacidad para resolver problemas." in user_competence_list:
        user_competence_list.remove("Capacidad para resolver problemas.")

    if cb_Datos.get() == 1:
      user_competence_list.append("Capacidad para tomar decisiones basadas en datos.")
    else:
      if "Capacidad para tomar decisiones basadas en datos." in user_competence_list:
        user_competence_list.remove("Capacidad para tomar decisiones basadas en datos.")

    if cb_Persudir.get() == 1:
      user_competence_list.append("Capacidad para argumentar persuasivamente.")
    else:
      if "Capacidad para argumentar persuasivamente." in user_competence_list:
        user_competence_list.remove("Capacidad para argumentar persuasivamente.")

    if cb_Negociar.get() == 1:
      user_competence_list.append("Capacidad de negociación.")
    else:
      if "Capacidad de negociación." in user_competence_list:
        user_competence_list.remove("Capacidad de negociación.")

    if cb_Empatia.get() == 1:
      user_competence_list.append("Habilidades empáticas y de escucha activa.")
    else:
      if "Habilidades empáticas y de escucha activa." in user_competence_list:
        user_competence_list.remove("Habilidades empáticas y de escucha activa.")

    if cb_Humano.get() == 1:
      user_competence_list.append("Capacidad para comprender el comportamiento humano.")
    else:
      if "Capacidad para comprender el comportamiento humano." in user_competence_list:
        user_competence_list.remove("Capacidad para comprender el comportamiento humano.")

  tk.Label(myFrame, text="Aptitudes", font=("Arial", 12)).grid(row=6, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Creatividad y pensamiento innovador.", variable=cb_Creatividad, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=6, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Habilidad para el diseño visual.", variable=cb_Visual, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=7, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Pensamiento lógico.", variable=cb_Logico, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=8, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Destreza en matemáticas.", variable=cb_Matematicas, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=9, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Capacidad para identificar oportunidades.", variable=cb_Oportunidades, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=10, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Pensamiento analítico.", variable=cb_Analitico, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=11, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Capacidad para resolver problemas.", variable=cb_Problemas, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=12, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Capacidad para tomar decisiones basadas en datos.", variable=cb_Datos, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=13, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Capacidad para argumentar persuasivamente.", variable=cb_Persudir, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=14, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Capacidad de negociación.", variable=cb_Negociar, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=15, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Habilidades empáticas y de escucha activa.", variable=cb_Empatia, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=16, column=0, sticky="w")
  tk.Checkbutton(myFrame, text="Capacidad para comprender el comportamiento humano.", variable=cb_Humano, onvalue=1, offvalue=0, command=lambda: cbAptitudesEscogida()).grid(row=17, column=0, sticky="w")
  

  def send():

    nameUser = name.get()
    lastNameUser = lastName.get()
    ageUser = age.get()
    carreerUser = carreer.get()

    expert_system =  CarreerExpert()
    expert_system.reset

    expert_system.declare(User(name=nameUser, lastName=lastNameUser, age= ageUser, carreer=carreerUser))
    expert_system.declare(Competence(names=user_competence_list))

    expert_system.run()

  buttonSend = tk.Button(myFrame, text="Continuar", command=lambda: send(), width=10, bg="blue", fg="white")
  buttonSend.grid(row=5, column=1, sticky="e", padx=20, pady=20)

  root.mainloop()

if __name__ == "__main__":
  main()