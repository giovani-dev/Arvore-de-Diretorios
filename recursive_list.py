# -*- coding: <encoding name> -*-
# from errors.errors import ArvoreDiretorioError
import time
import sys
import os
from os import *
from os.path import *
import time

class ArvoreDiretorio(object):
    def __init__(self):
        self.geral = {}
        self.lst_geral = []

    def __dict__(self):
        return self.geral

    def caminho(self, caminho_list):
        for x in caminho_list:
            try:
                if not '.git' in x and not '__pycache__' in x:
                    self.lista_dir(listdir(os.chdir(x+"/")))
                    os.chdir('../')
            except NotADirectoryError:
                pass
            except UnboundLocalError:
                pass
            except FileNotFoundError:
                pass
            except PermissionError:
                pass

    def lista_dir(self, dir_ent):
        for pasta in range(0, len(dir_ent)):
            try:
                os.chdir(dir_ent[pasta])
                os.chdir('../')
            except NotADirectoryError:
                pass
            except FileNotFoundError:
                pass
            except PermissionError:
                pass
        self.geral.update({os.getcwd(): dir_ent})
        self.lst_geral.append({os.getcwd(): dir_ent})
        self.caminho(dir_ent)
        return self
    
    def list(self):
        self.lista_dir(listdir(os.getcwd())).__dict__()
        # print(self.geral)
        return self

    def set_origem(self, **kwargs):
        try:
            os.chdir(kwargs['origem'])
        except KeyError:
            raise KeyError
            # raise ArvoreDiretorioError().OrigemDoesNotExist()
        return self


def main():
    print(sys.argv[1])
    os.chdir(sys.argv[1])
    return ArvoreDiretorio().set_origem(origem=os.getcwd()).list().__dict__()
    
    
if __name__ == '__main__':
    main()