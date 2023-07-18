import json

class DataManager:

    def __init__(self):
        pass


    def update_data(self, player_name="Unknown", score=0):
        new_score_data = {player_name: score}
        try:
            with open("data.json", "r") as data_file:
                self.data = json.load(data_file)
                if player_name in self.data and self.data[player_name] < score :
                    self.data.update(new_score_data)
                if player_name not in self.data :
                    self.data.update(new_score_data)
                print("data updated")
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_score_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(self.data, data_file, indent=4)


    def read_data(self):
        try:
            with open("data.json", "r") as json_file:
                file_data = json.load(json_file)
        except FileNotFoundError:
            return
        else:
            return file_data


