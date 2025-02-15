#Kypton Lantz
#February 14, 2025
#Module 7 - Assignment 2: Test Cases
#Write a program that produces the required results. Document those results, then add unit tests to test whether functions work as required.

def city_country(city, country, language=None, population=None):
    """Return a city, country, and optionally population neatly formatted."""
    if population and language:
        return f"{city.title()}, {country.title()} - population {population:,}, {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population:,}"
    elif language:
        return f"{city.title()}, {country.title()}, {language.title()}"
    else:
        return f"{city.title()}, {country.title()}"

#Call the function 3 times with different city-country pairs, and print the results.
print("\n--- City, Country, Population, and Language ---")
print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan', population=13929286))
print(city_country('new york', 'united states', 'english', 8419000))
print("\n\n Thank you for using my program!\n")