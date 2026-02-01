import os
from tkinter.filedialog import askdirectory # importa a função askdirectory do módulo filedialog, que permite acessar seu explorador de arquivos

caminho = askdirectory(title="Selecione uma pasta")
print(caminho)

lista_arquivos = os.listdir(caminho) # lista todos os arquivos e pastas dentro do diretório selecionado

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "documentos": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "musicas": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "compactados": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

for arquivo in lista_arquivos: 
    # 01. Arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}") # separa o nome do arquivo da sua extensão
    for pasta in locais:
        if extensao in locais[pasta]: # verifica se a extensão do arquivo está na lista de extensões daquela pasta
            if not os.path.exists(f"{caminho}/{pasta}"): # verifica se a pasta já existe
                os.mkdir(f"{caminho}/{pasta}") # cria a pasta caso ela não exista
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") # move o arquivo para a pasta correspondente