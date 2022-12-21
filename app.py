import pyautogui
from time import sleep

#Clicando no usuário
pyautogui.click(2575,119,duration=1)
pyautogui.write('leandro')

#clicando na senha
pyautogui.click(2568,146,duration=1)
pyautogui.write('123456')

#clicando em entrar
pyautogui.click(2472,173,duration=1)

#Dica para cancelar o percurso automático da seta, basta 
#elevar até o topo da tela no lado esquerdo.

#Extraindo dado
with open('produtos.txt','r') as files:
      for linha in files:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #Clicando e digitando o produto.
        pyautogui.click( , ,duration=1)
        pyautogui.write(produto)
        #Clicando e digitando a quantidade.
        pyautogui.click( , ,duration=1)
        pyautogui.write(quantidade)
        #Clicando e digitando o preço.
        pyautogui.click( , ,duration=1)
        pyautogui.write(preco)
        #Clicando e registrando.
        pyautogui.click( , ,duration=1)
        sleep(1)