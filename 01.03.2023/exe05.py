# EXERCICIO 05
t = float(
  input("Digite a tensão do circuito (em volts): "))  # Define tensão em volts
c = float(input("Digite a corrente do circuito (em amperes): ")
          )  # Define corrente em amperes
r = t / c  # formula da resistencia
print("A resistência do circuito é de", round(r, 2),
      "ohms.")  #resultado da resistência
p = c * t  # formula da potencia
print("A potência que o resistor deve ter é de", round(p, 2),
      "watts.")  # resultado da potencia
