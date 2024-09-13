import xml.etree.ElementTree as ET

# Carregar o arquivo XML
tree = ET.parse('exemplo_nfe.xml')
root = tree.getroot()

# Acessar dados específicos
nome_emitente = root.find('.//{http://www.portalfiscal.inf.br/nfe}emit/{http://www.portalfiscal.inf.br/nfe}xNome').text
data_emissao = root.find('.//{http://www.portalfiscal.inf.br/nfe}ide/{http://www.portalfiscal.inf.br/nfe}dEmi').text

# Exibir dados
print(f'Nome do Emitente: {nome_emitente}')
print(f'Data de Emissão: {data_emissao}')
