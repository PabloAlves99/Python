# Abstração
class log:
    def log(self, msg):
        raise NotImplementedError('Implemente o método log')
 
class logFileMixin(log):
    def log(self,msg):
        print(msg)
           

if __name__ == '__main__':
    x = logFileMixin()
    x.log('Qualquer coisa')