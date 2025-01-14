#pip install pyautogui
import pyautogui
import time
#sempre q for pausar coloque o mouse no canto superior esquerdo
#pyautogui.click -> clicar
#pyautogui.press -> pressionar tecla
#pyautogui.write -> escrever
#pyautogui.hotkey -> atalho de teclado (ctrl, C) modelo -> pyautogui.hotkey("ctrl", "c")
#para aprender mais vai no google e pesquisa pyautogui primeiro link depois -> cheat sheet

pyautogui.PAUSE = 0.3
#passo 1: abrir site
#    sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
#comando para abrir windows  depois apertar enter (dica é dividir em cada função parte por parte) 
pyautogui.press("win") 
#depois escrever chroma
pyautogui.write("opera")

#depois apertar enter (dica é dividir em cada função parte por parte) 
pyautogui.press("enter")
time.sleep(2)
#escrever link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# pedir para o computador esperar 3 segundos
time.sleep(3)

#passo 2:    login: dasbdabsiu@gmail.com 
pyautogui.press("tab")
#pyautogui.click(x=871, y=376)
pyautogui.write("robertin@gmail.com")
pyautogui.press("tab") #passou para senha
pyautogui.write("senha123")
pyautogui.press("tab") #passou para o botao
pyautogui.press("enter")


#passo 3: importar base de dados
#instalar o pandas e openpyxl -> pip install pandas openpyxl
import pandas

#ler arquivo
tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(2)
for linha in tabela.index: 
    #passo 4: cadastrar 1 produto
    pyautogui.click(x=1680, y=245) #click no primeiro campo
    #dica -> sempre faça manualmente e depois faça a automatização
    #codigo
    pyautogui.press("tab")
    # tabela.loc[linha, coluna]
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")

    #scroll -> numero positivo scroll pra cima, scroll pra baixo numero negativo 
    pyautogui.scroll(10000)


#passo 5 repetir o passo 4 ate acabar os produtos

