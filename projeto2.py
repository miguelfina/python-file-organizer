import os
from tkinter.filedialog import askdirectory # importa a função askdirectory do módulo filedialog, que permite acessar seu explorador de arquivos

caminho = askdirectory(title="Selecione uma pasta")
print(caminho)

