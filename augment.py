import os

abs_path = os.path.dirname(__file__)
image_dir = os.path.join(abs_path, "input")

#Função para padronização dos nomes dos arquivos de entrada
def rename_input():
    os.chdir(image_dir)
    files = os.listdir(image_dir)

    for i, filename in enumerate(files):
        in_path = os.path.join(image_dir, filename)
        out_path = os.path.join(image_dir, f'{i}.jpg')

        os.rename(in_path, out_path)
