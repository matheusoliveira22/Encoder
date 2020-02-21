arqsai = 'decodificado'
config = 'config.conf'

txt_config = open(config,'r').read().split('\n')
bits = int(txt_config[0])
chars = list(txt_config[1])

#print(bits)
#print(chars)
#print(len(chars))

print('Digite o nome do arquivo que deseja decodificar:',end=' ')
arqent = input()

texto = list(open(arqent, 'r').read())

saida = []
count = 8
b = 0
for i in range(0,len(texto)):
        print('\rPercentual de conclusão: {0:.2f}%'.format((i/len(texto))*100), sep = '', end='')
        c = texto[i]
        b = b + chars.index(c)
        count = count - bits
        if count > 0:
                b = b << bits
        else:
                saida.append(b)
                count = 8
                b = 0

print('\rPercentual de conclusão: 100.00%')

fsai = open(arqsai, 'wb')
fsai.write(bytearray(saida))
fsai.close()

input()
