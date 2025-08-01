from brewery import Brewery
from beer import Beer

def main():
    user_input_city = input('Please input an American city you would like to see a random brewery from: ')
    
    beer = Beer()
    brewery = Brewery(user_input_city)
    
    brewery_info = brewery.get_one_brewery()
    if brewery_info == brewery.city_fail:
        return
    
    total_breweries = brewery.get_total_breweries()
    random_beer = beer.get_random_beer()
    beer_rating = beer.get_rating(random_beer)
    total_beers = beer.get_total_beers()
    brewery_type_info = brewery.get_brewery_type_info(brewery_info)
    
    brewery_prompt1 = f'The city you have selected is {user_input_city} and out of the {total_breweries} total breweries the one selected randomly is {brewery_info['name']}.'
    brewery_prompt2 = f'The type of brewery is {brewery_type_info}.'
    brewery_prompt3 = f'You can find this brewery on {brewery_info['address']} and can be accessed at {brewery_info['website']}.'
    beer_prompt1 = f'Out of the {total_beers} beers in the database, a randomly selected one you may be interested in is "{random_beer['name']}".'
    beer_prompt2 = f'It is priced at {random_beer['price']} and has an average rating of {beer_rating} out of 5 by consumers.'
    
    print_list = brewery_prompt1, brewery_prompt2, brewery_prompt3, beer_prompt1, beer_prompt2
    for i in print_list:
        print(i)



main()





