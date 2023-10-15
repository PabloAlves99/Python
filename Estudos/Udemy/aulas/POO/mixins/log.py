# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent

class log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        self._log(f'Error: {msg}')
 
    def log_success(self, msg):
        self._log(f'Success: {msg}')
        
class logFileMixin(log):
    def _log(self,msg):
        print(msg)
           
class logPrintMixin(log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    x = logPrintMixin()
    x.log_error('Qualquer coisa')
    x.log_success('Que legal')
    print(LOG_FILE)