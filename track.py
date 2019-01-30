import datetime
import json


class Prompts(object):
    TASK = "Task: "
    DESCRIPTION = "Description: "

class Actvities(dict):

    def list_tasks(self):
        return self.keys()

    def task(self):
        task = None
        while task is None:
            response = input(Prompts.TASK)
            if response == '?':
                print(self.list_tasks())
            elif response.lower() in self.keys():
                task = self[response]
            else:
                task = Task()

    @staticmethod
    def description(task):
        description = None
        while description is None:
            response = input(Prompts.DESCRIPTION)
            if response == '?':
                print('Description:\n{text}'.format(text="\n + ".join(task.descriptions)))
            else:
                description = response.strip("\n")
                task.description.append(description)
        return description


class Task(object):

    def __init__(self, name):
        self.starts = []
        self.stops = []
        self.duration = 0
        self.descriptions = []
        self.name = name

    def add_description(self, description):
        self.descriptions.append(description)

    def get_description_list(self):
        return self.descriptions

    def start(self, time=None):
        self.starts.append(datetime.datetime.now() if time is None else time)

    def stop(self, time=None):
        self.stops.append(datetime.datetime.now() if time is None else time)
        self.duration += (self.stops[-1] - self.starts[-1]).totalseconds

    def is_synced(self):
        return len(self.starts) == len(self.stops)

    def _serialize_(self):
        pass

def main():
    pass


if __name__ == '__main__':
    main()