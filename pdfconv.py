from PyPDF2 import PdfReader
import json

def convert_pdf_to_word_list(pdf_path):
    word_list = []

    # Abrir o arquivo PDF
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)

        # Iterar pelas páginas do PDF
        for page in pdf_reader.pages:
            text = page.extract_text()

            # Dividir o texto em palavras
            words = text.split()

            # Adicionar as palavras à lista geral
            word_list.extend(words)

    return word_list

# Exemplo de uso
pdf_path = './arquivo.pdf'
word_list = convert_pdf_to_word_list(pdf_path)

# Salvar a lista de palavras em um arquivo JSON
output_path = 'pdf.json'
with open(output_path, 'w') as file:
    json.dump(word_list, file, indent=4)

print(f"Arquivo JSON salvo em: {output_path}")
