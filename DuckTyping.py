class Pycharm:

    def execute(self):
        print('Running', 'Compiling')

class laptop():

    def code(self,ide):
        ide.execute()

ide = Pycharm()
lap1 = laptop()
lap1.code(ide)