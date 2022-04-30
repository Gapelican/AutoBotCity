from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.execute(r"C:\Users\Pelic\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams (work or school).lnk")

        
        if not self.find( "pesquisar", matching=0.97, waiting_time=10000):
            self.not_found("pesquisar")
        self.click()
        self.paste("Anderson Liberato")

        if not self.find( "anderson", matching=0.97, waiting_time=10000):
            self.not_found("anderson")
        self.click()
        
        if not self.find( "msg", matching=0.97, waiting_time=10000):
            self.not_found("msg")
        self.click()

        self.paste("Apenas um teste")

        if not self.find( "submit", matching=0.97, waiting_time=10000):
            self.not_found("submit")
        self.click()



    def not_found(self, label):
        print(f"Element not found: {label}")



if __name__ == '__main__':
    Bot.main()











