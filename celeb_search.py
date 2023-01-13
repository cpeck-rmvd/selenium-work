import wikipediaapi

def find_dob_dod(celebrity):
    wiki = wikipediaapi.Wikipedia(language='en', extract_format=wikipediaapi.ExtractFormat.WIKI)
    try:
        p = wiki.page(celebrity)
    except wikipediaapi.exceptions.PageError:
        return "Sorry, we couldn't find the celebrity you've entered. Please try again with a different name"
    
    if p.exists():
        # Extracting the date of birth
        dob_string = p.text.split('date of birth')[1].split('\n')[0]
        dob = dob_string.strip()
        # Extracting the date of death
        if 'date of death' in p.text:
            dod_string = p.text.split('date of death')[1].split('\n')[0]
            dod = dod_string.strip()
            return f"{celebrity} was born on {dob} and died on {dod}."
        else:
            return f"{celebrity} was born on {dob} and is still alive."
    else:
        return "Sorry, we couldn't find the celebrity you've entered. Please try again with a different name"

celebrity = input("Enter a celebrity's name: ")
print(find_dob_dod(celebrity))
