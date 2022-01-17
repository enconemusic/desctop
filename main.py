from pywinauto.application import Application
import time
# старт сервер UI
app = Application().start(r'D:\builds\3.1 RL\MDC v3.1.1.4527scenario\ServerUI\Industry.ServerUI.exe')
time.sleep(15)
# ожидаем запуска службы
dlg_spec = app.MDCplus

# ожидаем реального открытия окна
actionable_dlg = dlg_spec.wait('visible')

app.sbAdd.click()
