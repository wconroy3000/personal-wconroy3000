import requests 
import json
import random

class Brewery:
    def __init__(self,city):
        '''
        Initializes the Brewery class with the brewery API and an empty string to be used to determine if the user_input passes
        args:
            city: str - the name of the city the API is to retrieve the brewery information from
        '''
        self.api_url = f'https://api.openbrewerydb.org/v1/breweries?by_city={city}&per_page=200'
        self.city_fail = ''

    def get(self):
        '''
        Gets the information from the brewery API and returns the json content
        return:
            list: The list of brewery information dictionaries from the API
        '''
        response = requests.get(self.api_url)
        result = response.json()
        return result
    
    def get_total_breweries(self):
        '''
        Gets the total number of breweries in the city from the API json contents
        return:
            int: The number of breweries available in the city or 0 if there is none
        '''
        result = self.get()
        if result:
            return len(result)
        else:
            return 0

    def get_one_brewery(self):
        '''
        Randomly selects a brewery from the list of breweries in the city
        return:
            dict: A dictionary with the information on the random brewery
            str: A message indicating there are no breweries in the city
        '''
        result = self.get()
        if result: 
            random_brewery = random.choice(result)
            brewery_info = {
                'name' : f"{random_brewery['name']}",
                'type' : f"{random_brewery['brewery_type']}",
                'address': f"{random_brewery['street']}, {random_brewery['city']}, {random_brewery['state_province']}",
                'website': f"{random_brewery.get('website_url', 'No website available')}"
            }
            return brewery_info
        else:
            self.city_fail = print("No breweries found for the given city, maybe you spelt the city wrong?")
            return self.city_fail
        
        
    def get_brewery_type_info(self, brewery_info=None):
        '''
        Explains what the types of breweries mean
        args:
            brewery_info: dict - contains information and the type on the randomly selected brewery
        return:
            str: A description of the brewery type  
        '''
        brewery_type = brewery_info['type']
        if brewery_type == 'micro':
            return 'Micro (most craft breweries. For example, Samual Adams is still considered a micro brewery)'
        elif brewery_type == 'nano':
            return 'Nano (an extremely small brewery which typically only distributes locally)'
        elif brewery_type == 'regional':
            return 'Regional (a regional location of an expanded brewery. Ex. Sierra Nevada’s Asheville, NC location)'
        elif brewery_type == 'brewpub':
            return 'a Brewpub (a beer-focused restaurant or restaurant/bar with a brewery on-premise)'
        elif brewery_type == 'large':
            return 'Large (a very large brewery. Likely not for visitors. Ex. Miller-Coors. (deprecated))'
        elif brewery_type == 'planning': 
            return 'Planned (a brewery in planning or not yet opened to the public)'
        elif brewery_type == 'bar':
            return 'a Bar (no brewery equipment on premise. (deprecated))'
        elif brewery_type == 'contract':
            return 'Contract (a brewery that uses another brewery’s equipment)'
        elif brewery_type == 'proprietor':
            return 'Proprietor (a brewery that uses another brewery’s incubator)'
        elif brewery_type == 'closed':
            return 'Closed'
        else:
            return  

