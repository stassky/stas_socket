import datetime
import socket

print(datetime.datetime.now())

_HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
_PORT = 65432  # Port to listen
# Create a TCP/IP socket
def Listening (HOST,PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  ## Associate with spesific Host and Port
        s.listen()

        conn, addr = s.accept()  ## Server accepts connection and Listen

        with conn:

            print('Connected by IP: ', addr)
            conn.close()
    return str(addr)

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
'D': '-..',    'E': '.',      'F': '..-.',
'G': '--.',    'H': '....',   'I': '..',
'J': '.---',   'K': '-.-',    'L': '.-..',
'M': '--',     'N': '-.',     'O': '---',
'P': '.--.',   'Q': '--.-',   'R': '.-.',
'S': '...',    'T': '-',      'U': '..-',
'V': '...-',   'W': '.--',    'X': '-..-',
'Y': '-.--',   'Z': '--..',

'0': '-----',  '1': '.----',  '2': '..---',
'3': '...--',  '4': '....-',  '5': '.....',
'6': '-....',  '7': '--...',  '8': '---..',
'9': '----.',

',': ' , '
 }

morse = ""


for x in Listening(_HOST,_PORT):
    try:
        morse += CODE[x.lower()]+ " "

    except: pass
print("Morse: " + morse)
