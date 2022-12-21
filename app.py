import pyautogui
from time import sleep

#Clicando no usuário
pyautogui.click(1214,49,duration=1)
pyautogui.write('leandro')

#clicando na senha
pyautogui.click(1216,74,duration=1)
pyautogui.write('123456')

#clicando em entrar
pyautogui.click(1125,100,duration=1)

#Dica para cancelar o percurso automático da seta, basta 
#elevar até o topo da tela no lado esquerdo.

#Extraindo dado
with open('produtos.txt','r') as files:
      for linha in files:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #Clicando e digitando o produto.
        pyautogui.click(395,373,duration=1)
        pyautogui.write(produto)
        #Clicando e digitando a quantidade.
        pyautogui.click(394,399,duration=1)
        pyautogui.write(quantidade)
        #Clicando e digitando o preço.
        pyautogui.click(394,425,duration=1)
        pyautogui.write(preco)
        #Clicando e registrando.
        pyautogui.click(310,582,duration=1)
        sleep(1)