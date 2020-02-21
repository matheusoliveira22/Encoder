arqsai = 'codificado'
config = 'config.conf'

txt_config = open(config,'r').read().split('\n')
bits = int(txt_config[0])
chars = txt_config[1]

#print(bits)
#print(chars)
#print(len(chars))

print('Digite o nome do arquivo que deseja codificar:',end=' ')
arqent = input()

texto = list(open(arqent, 'rb').read())

saida = []

for i in range(0,len(texto)):
	print('\rPercentual de conclusão: {0:.2f}%'.format((i/len(texto))*100), sep = '', end='')
	c = texto[i]
	count = 8
	while count > 0:
		b = c >> bits
		c = (c << bits)%256
		#print(bits, b, c)
		saida.append(chars[b])
		count = count - bits

print('\rPercentual de conclusão: 100.00%')

fsai = open(arqsai, 'w')
fsai.write(''.join(saida))
fsai.close()

input()
