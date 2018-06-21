import pynput

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def on_click(x, y, button, pressed):
    if button == pynput.mouse.Button.left:
        keyboard.press('2')

with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
    

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

def on_click(x, y, button, pressed):
    keyboard.press('2')
    keyboard.release('2')

with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
    
    
def on_click(x, y, button, pressed):  
    if button == mouse.Button.left:  
        #do stuff  
