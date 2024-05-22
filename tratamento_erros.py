## open("/path/to/mars.jpg")
# FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

#Te dá a chamada, linha do erro
 
#def fnc_open():
#    open("/path/to/mars.jpg")
#if __name__ == '__main__':
#  fnc_open()


#Tratamento por execeção
try:
     open('config.txt')
except FileNotFoundError:
     print("Arquivo config.txt não encontrado!")


def fnc():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    fnc()


#dá para atribuir o erro e chamar no print 
try:
    open("mars.jpg")
except FileNotFoundError as erro:
     print("Got a problem trying to read the file:", erro)