import time
import pyautogui as pg

# Número de iterações (ajuste conforme necessário)
num_iteracoes = 10118
print(f"Total de iterações: {num_iteracoes}")

# Coordenadas dos cliques
posicao_trocar_aba = (355, 751)
posicao_seta = (475, 143)
posicao_aba_desejada = (537, 484)
posicao_confirmacao = (587, 456)

# Trocar de aba inicial
pg.click(*posicao_trocar_aba)

for i in range(num_iteracoes):
    pg.click(*posicao_seta)  # Clicar na seta
    time.sleep(3)
    
    pg.click(*posicao_aba_desejada)  # Clicar na aba desejada
    pg.press('tab')
    time.sleep(3)
    
    pg.press('del', presses=9)  # Excluir informações
    pg.press('tab')
    pg.press('del', presses=9)
    time.sleep(3)
    
    pg.click(627, 565)  # Outro clique para a exclusão
    pg.press('del', presses=9)
    pg.press('tab')
    pg.press('del', presses=9)
    
    pg.hotkey('alt', 'g')  # Confirmar
    time.sleep(4)
    
    pg.click(*posicao_confirmacao)  # Clique de confirmação
    time.sleep(10)
    
    print(f"Iteração {i+1}/{num_iteracoes} concluída")

pg.position()  # Verificar posição do mouse
