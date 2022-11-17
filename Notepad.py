
#Essa automação inicializa o notepad através do Windows + R, escreve um texto e fechar sem salvar o notepad.

import pyautogui as posicaoMouse

posicaoMouse.sleep(2) #Esperar 2 Segundos

posicaoMouse.hotkey('win', 'r') #abrir a guia de comandos windows + r
posicaoMouse.sleep(2) #Esperar 2 Segundos

posicaoMouse.typewrite('notepad') #Digitou Notepad
posicaoMouse.sleep(2) #Esperar 2 Segundos

posicaoMouse.press('enter') #Clicou Enter
posicaoMouse.sleep(2) #Esperar 2 Segundos

posicaoMouse.typewrite('escreveu a primeira linha') #Escrever no notepad
posicaoMouse.sleep(2) #Esperar 2 Segundos

#clique enter
posicaoMouse.press('enter') #Clicou Enter
posicaoMouse.sleep(1) #Esperar 1 Segundo

posicaoMouse.typewrite('escreveu a segunda linha') #Escrever no notepad
posicaoMouse.sleep(2) #Esperar 2 Segundos


fecharNotepad = posicaoMouse.getActiveWindow() #F unção para fechar o notepad
posicaoMouse.sleep(2) #Esperar 2 segundos

fecharNotepad.close() #Clicou em fechar
posicaoMouse.sleep(2) #Esperar 2 segundos

posicaoMouse.press('tab') #clique tab
posicaoMouse.sleep(2) #Esperar 2 segundos

#clique enter
posicaoMouse.press('enter') #Clicou Enter
posicaoMouse.sleep(2) #Esperar 2 segundos

print('o robo abriu o notepad através do windows r, digitou o texto e não salvou')
