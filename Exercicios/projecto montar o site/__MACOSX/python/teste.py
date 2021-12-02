import openpyxl

#criar uma folha (book)
book = openpyxl.workbook()
# como visulaizar paginas existentes
print(book.sheetnames)
#como criar uma pagina
book.create_sheet('Frutas')
#selecionar pagina
frutas_page = book['Frutas']
frutas_page.append(['Banana', '5', '€3,90'])
frutas_page.append(['Fruta 1', '2', '€17,90'])
frutas_page.append(['Fruta 2', '7', '€45,00'])
frutas_page.append(['Fruta 3', '8', '€12,12'])
# salvar o ficheiro
book.save('Planilha de compras.xlsx')

