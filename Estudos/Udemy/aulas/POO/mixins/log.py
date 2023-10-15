# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
 
    def log_success(self, msg):
        self._log(f'Success: {msg}')
        
class logFileMixin(log):
    def _log(self,msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log: ', msg_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        print(msg)
           
class logPrintMixin(log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = logPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Que legal')
    lf = logFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Que legal')
    