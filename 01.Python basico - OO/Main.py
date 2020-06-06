from veiculo import Veiculo


caminhao_preto = Veiculo("Preto", 6 , "Volvo",80)
print("Cor:",caminhao_preto.cor,", Rodas:",caminhao_preto.rodas,", Marca:",caminhao_preto.marca,", Tanque:",caminhao_preto.tanque)

caminhao_preto.pintar('azul')
print(f"Pintamos o caminha preto de {caminhao_preto.cor}")

caminhao_preto.abastecer(20)

caminhao_preto.viagem(90)






