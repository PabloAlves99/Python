from log import logPrintMixin, logFileMixin

lp = logPrintMixin()
lp.log_error('Qualquer coisa')
lp.log_success('Que legal')
lf = logFileMixin()
lf.log_error('Qualquer coisa')
lf.log_success('Que legal')