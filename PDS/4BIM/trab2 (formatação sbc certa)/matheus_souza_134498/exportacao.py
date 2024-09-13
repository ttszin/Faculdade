import xml.etree.ElementTree as ET

# Criar a estrutura do XML
root = ET.Element('NFe', xmlns="http://www.portalfiscal.inf.br/nfe")
infNFe = ET.SubElement(root, 'infNFe', {'Id': 'NFe123', 'versao': '1.10'})
ide = ET.SubElement(infNFe, 'ide')
ET.SubElement(ide, 'cUF').text = '35'
ET.SubElement(ide, 'natOp').text = 'Venda a vista'

# Adicionar mais elementos conforme necessário...

# Criar uma árvore a partir da raiz
tree = ET.ElementTree(root)

# Salvar o XML em um arquivo
tree.write('nfe_exportada.xml', encoding='utf-8', xml_declaration=True)
