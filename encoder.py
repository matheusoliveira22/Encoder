import sys

encodedfname = ''
decodedfname = ''
num_bits     = 0
chars        = ''
functions    = {}
function     = ''
args         = []

def init():
    global functions, function, args
    readconfig('config.conf')

    functions  = {
        '-encode' : (func_encode,   'Codificar arquivo especificado como argumento de entrada', 1),
        '-decode' : (func_decode,   'Decodificar arquivo especificado como argumento de entrada', 1),
        '-h'      : (func_showhelp, 'Apresentar esta tela de ajuda', 0),
        '--help'  : (func_showhelp, 'Apresentar esta tela de ajuda', 0)
    }

    if len(sys.argv) < 2 or sys.argv[1] not in functions:
        func_showhelp()

    function = sys.argv[1]

    if (len(sys.argv) - 2) < functions[function][2]:
        func_showhelp()

    args = sys.argv[2:]
    
    return

def main():
    global function, functions

    init()
    functions[function][0]()
    return

def func_encode():
    global args, num_bits, chars, encodedfname

    texto = list(open(args[0], 'rb').read())

    saida = []
    p = 0

    for i in range(0,len(texto)):
        perc = (i/len(texto))*100
        if p < perc:
                print('\rPercentual de conclusão: {0:.2f}%'.format(perc), sep = '', end='')
                p = perc + 1
        c = texto[i]
        count = 8
        while count > 0:
            b = c >> num_bits
            c = (c << num_bits)%256
            saida.append(chars[b])
            count = count - num_bits

    print('\rPercentual de conclusão: 100.00%')

    fsai = open(encodedfname, 'w')
    fsai.write(''.join(saida))
    fsai.close()

    print('Arquivo gravado:', encodedfname)
    return

def func_decode():
    global args, num_bits, chars, decodedfname

    texto = list(open(args[0], 'r').read())

    saida = []
    count = 8
    b = 0
    p = 0
    for i in range(0,len(texto)):
            perc = (i/len(texto))*100
            if p < perc:
                    print('\rPercentual de conclusão: {0:.2f}%'.format(perc), sep = '', end='')
                    p = perc + 1
            c = texto[i]
            b = b + chars.index(c)
            count = count - num_bits
            if count > 0:
                    b = b << num_bits
            else:
                    saida.append(b)
                    count = 8
                    b = 0

    print('\rPercentual de conclusão: 100.00%')

    fsai = open(decodedfname, 'wb')
    fsai.write(bytearray(saida))
    fsai.close()

    print('Arquivo gravado:', decodedfname)
    return

def func_showhelp():
    print('Opções e argumentos de utilização:')

    for k, v in functions.items():
        print(k.ljust(12,' '), ':', v[1])
    exit(0)

def readconfig(cfgfile):
    global encodedfname, decodedfname, num_bits, chars

    try:
        txt_config = open(cfgfile,'r').read().split('\n')
        encodedfname = txt_config[0]
        decodedfname = txt_config[1]
        num_bits     = int(txt_config[2])
        chars        = txt_config[3]
    except Exception as e:
        print('Erro ao ler o arquivo de configuração config.conf')
        print('Abortando execução\n')
        print('Detalhes do erro ocorrido:')
        print(str(e))

        exit(8)

    return

main()