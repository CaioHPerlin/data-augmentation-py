import os
import re
import Augmentor

abs_path = os.path.dirname(__file__)

image_dir = os.path.join(abs_path, "input")
output_dir =  os.path.join(abs_path, "output")

files = os.listdir(image_dir)

#Aumentação de dados
pipeline = Augmentor.Pipeline(image_dir, output_dir)
pipeline.flip_left_right(probability=0.5)
pipeline.flip_top_bottom(probability=1)
pipeline.sample(len(files)*2)

output_files = os.listdir(output_dir)

for i, filename in enumerate(output_files):

    in_path = os.path.join(output_dir, filename)
    out_path = os.path.join(output_dir, f'aug-{i}.jpg')

    os.rename(in_path, out_path)

#Função para padronização dos nomes dos arquivos de entrada
def rename_input():

    for i, filename in enumerate(files):
        in_path = os.path.join(image_dir, filename)
        out_path = os.path.join(image_dir, f'{i}.jpg')

        os.rename(in_path, out_path)