Nome = ["Bob Smith", "Sue Jones", "Carl Max"]
Resposta = ""

for i in Nome:
    NomeSeparado = i.slit()
    Resposta += NomeSeparado[1] + ", "+
NomeSeparado[0] + "; "

print(Resposta)
