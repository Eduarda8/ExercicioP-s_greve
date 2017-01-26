def ValorPagamento(ValorPrestacao, DiasAtraso):
 
    PercentualMulta = 3
    ValorMulta = (ValorPrestacao * PercentualMulta)/100
 
    PercentualJurosDias = 0.1
    ValorJurosDia = (ValorPrestacao * PercentualJurosDias)/ 100
 
    ValorTotalJurosDia = ValorJurosDia * DiasAtraso
    ValorTotal = ValorPrestacao + ValorMulta + ValorTotalJurosDia
 
    return ValorTotal
 
ValorPrestacao = float(input("informe o valor da prestação: "))
QuantidadePrestacoesPagas = 0
ValorPrestacoesPagas = 0
 
while ValorPrestacao!=0:
    QuantidadePrestacoesPagas += 1
 
    DiasAtraso = int(input("informe os dias em atraso: "))
 
    ValorTotalPagamento = ValorPagamento(ValorPrestacao, DiasAtraso)
    ValorPrestacoesPagas += ValorTotalPagamento
 
    print ("o valor total a ser pago é ", ValorTotalPagamento)
 
    ValorPrestacao = float(input("informe o valor da prestação: "))
 
print("Relatorio do dia:")
print("Número de prestações pagas: ", QuantidadePrestacoesPagas)
print("Valor de prestações pagas: ", ValorPrestacoesPagas)
