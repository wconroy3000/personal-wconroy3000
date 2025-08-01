import requests
import random

class Beer:
    def __init__(self):
        '''
        Initializes the Beer class with the beer API
        '''
        self.api_url = 'https://api.sampleapis.com/beers/ale'
    
    def get(self):
        '''
        Retrieves the list of beers from the API
        return:
            list: list of dictionaires for each beer in the database
        '''
        response = requests.get(self.api_url)
        result = response.json()  
        return result
    
    def get_total_beers(self):
        '''
        Gets the total number of breweries in the city from the API database
        return:
            int: The total number of beers in the database 
        '''
        result = self.get()
        return len(result)


    def get_random_beer(self):
        '''
        Selects a random beer from the database 
        return:
            dict: A single dictionary with information on a beer from the list of dictionaries given by the API
        '''
        beers = self.get()
        random_beer = random.choice(beers)  
        return random_beer
    
    def get_rating(self, random_beer=None):
        '''
        Changes the beer rating to only have the first four characters if the average rating is longer than 4 characters 
        args:
            random_beer: dict - A dictionary with the information on a beer 
        return:
            str: the average rating with a rounded result 
        '''
        random_beer_rating = str(random_beer['rating']['average'])
        if len(random_beer_rating) >= 5 and int(random_beer_rating[4]) >= 5:
            rounded_rating = f'{random_beer_rating[:3]}{int(random_beer_rating[3]) + 1}'
        else:
            rounded_rating = random_beer_rating[:4]
        return rounded_rating

