#!/usr/bin/python3
# author: T4wngPh4
import xml.etree.ElementTree as ET
from py_trans import PyTranslator
import os
from pathlib import Path

translator = PyTranslator()


def main():
    file_path = input("Enter your file path: ")
    tran_lang = input("Enter your language that you want to translate: ")
    dir_path = f'out/values-{tran_lang}/'
    tree = ET.parse(file_path)
    root = tree.getroot()

    # loop for array from strings.xml
    for i in range(len(root)):
        if (root[i].tag == 'string-array') and (root[i].get('translatable') != 'false'):
            # for string-array that can be translatable
            for j in range(len(root[i])):
                if root[i][j].tag == 'item':
                    # print(root[i][j].text)
                    root[i][j].text = translator.translate(root[i][j].text, tran_lang)['translation']
                    print(root[i][j].text)
        else:
            # normal string
            isTranslatable = root[i].get('translatable')
            if isTranslatable != 'false':
                root[i].text = translator.translate(root[i].text, tran_lang)['translation']
                print(f"Tran completed: {root[i].text}")

    # check dir exists or not
    if not Path(dir_path).exists():
        os.makedirs(dir_path)
    # write xml file back
    tree.write(f'{dir_path}strings.xml', encoding='utf-8')


if __name__ == "__main__":
    main()
