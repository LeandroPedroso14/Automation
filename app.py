import pyautogui
from time import sleep

#Clicando no usuário
pyautogui.click(2575,119,duration=2)
pyautogui.write('leandro')

#clicando na senha
pyautogui.click(2568,146,duration=2)
pyautogui.write('123456')

#clicando em entrar
pyautogui.click(2472,173,duration=2)

#Dica para cancelar o percurso automático da seta, basta 
#elevar até o topo da tela no lado esquerdo.

#Extraindo dado
with open('produtos.txt','r') as files:
      for linha in files:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #Clicando e digitando
        pyautogui.click( , ,duration=2)