from config.sfmc_credentials import sfmc_credentials

def retrieve_business_units():

    business_units = []

    for business in sfmc_credentials:
        business_units.append(business['name'])

    return business_units
