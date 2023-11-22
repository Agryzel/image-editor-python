from datetime import datetime

logFile = 'filtre.log'

def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%H:%M:%S %Y/%m/%d')
    formatted = f'{timestamp} - {msg}'
    with open(logFile, 'a') as logger:
        logger.write(formatted + '\n')

def display_log():
    try:
        with open(logFile, 'r') as logger:
            print(logger.read())
    except FileNotFoundError as e:
        print(f'Ne peut pas être lu : {logFile}. Erreur={e}')
