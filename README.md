# Encoder
A função básica deste programa é codificar e decodificar um arquivo de texto com base nas configurações contidas no documento config.conf

# Disposição do config.conf
As primeiras duas linhas contém respectivamente os nomes dos arquivos de saída gerados após a codificação e decodificação.
As próximas duas linhas definem os valores utilizados na codificação e decodificação, sendo que a primeira linha contém um número que indica quantos bits de um byte serão utilizado para cada conversão e a linha abaixo indica os valores a serem substituídos.

Exemplo:
No arquivo contido junto ao projeto, temos o número 4 indicado que cada byte será dividido em 2 nibbles e o valor obtido em cada nibble será substituído pela coluna respectiva encontrada na última linha.
Na codificação, caso tenhamos o caractere 'A' (0x41) no arquivo de entrada, o mesmo será substituído por 'eb' no arquivo de saída.
Na decodificação, caso tenhamos os caracteres 'eb' no arquivo de entrada, o mesmo voltará como 'A' no arquivo de saída gerado.
