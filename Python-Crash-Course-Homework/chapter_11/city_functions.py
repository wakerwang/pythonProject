# coding:utf-8

def city_full_name(city, country, population=0):
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string.title()
