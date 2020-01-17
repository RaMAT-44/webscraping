import pandas as pd 
import json
from bs4 import BeautifulSoup
import os


def fn():       # 1.Get file names from directory
    file_list=os.listdir(r"E:/UNT/R/courtlistner/extract/maincolumbia")
    return file_list
    
file_list = fn()

dest = 'E:/UNT/R/courtlistner/extract/maincolumbia/'

file_listpath = [dest + s  for s in file_list]

for path in file_listpath:
    case_text = ' '
    input_file=open(str(path), 'r', encoding="utf8")
    html = BeautifulSoup(input_file,'html.parser')
    for para in html.find_all('p'):
        para_text = para.text
        case_text = case_text + para_text + '\n'
    path_main = 'E://UNT//R//courtlistner//parse//maincolumbia//' + path.rsplit('/',1)[1].partition('.')[0] + '.txt'
    text_file = open(path_main, "a",encoding='utf-8')
    text_file.write(case_text)
    

