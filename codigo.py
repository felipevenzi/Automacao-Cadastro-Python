# Intalar pip install pyautogui
# Intalar pip install pandas
import pyautogui
import time
import pandas

    # pyautogui.write → escrever um texto
    # pyautogui.click → clicar com o mouse
    # pyautogui.press → apertar uma tecla
    # pyautogui.hotkey → apertar um atalho de teclado → (Ctrol, C)

pyautogui.PAUSE = 0.5

    # abrir o navegador
    # apertar a tecla win
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')

    # entrar no link ↣ https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 1: Entrar no sistema da empresa ↣ https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

    # quero dar uma PAUSA de 3 segundos
time.sleep(3)

# maximizar tela Google Chrome
# pyautogui.click(x=1125, y=18)

# e-mail
email = 'teste@gmail.com'
pyautogui.click(x=903, y=398)
pyautogui.write(email)

# senha
    # pyautogui.click(x=928, y=495)
senha = 'teste123'
pyautogui.press('tab')
pyautogui.write(senha)

# Posso 2: Fazer login ↣ apertar o botão de login
    # pyautogui.click(x = 958, y = 536)
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

# Passo 3: Importar a base de dados
tabela = pandas.read_csv('dataset\produtos.csv')
print(tabela)

# Passo 4: Cadastrar 1 produto
    # selecionar o primeiro campo
pyautogui.click(x=674, y=281)

# linha = 0
# para cada linha da minha tabela
for linha in tabela.index:
        # selecionar o primeiro campo
    pyautogui.click(x=674, y=281)

        # Códigp
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

        # Marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

        # Tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

        # Categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

        # Preço Unitário
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

        # Custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

        # OBS
            # nam = Not a Number = vazio
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs): # isna ↣ verifica se ta fazio!
        pyautogui.write(str(obs))    
    pyautogui.press('tab')

        # salvar formulário
    pyautogui.press('enter')
    pyautogui.scroll(5000)

# limpar formulário
    # pyautogui.press('enter')


# Passo 5: Repetir o processo de cadastro até acabar os produtos
# HORA VIDEO 02:00:00