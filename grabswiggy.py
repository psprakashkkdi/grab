import traceback
import csv
import requests

"""
This function calls the swiggy api and returns the result
"""


def swiggy():
    lat = '12.9279232'
    slug = 'thottathil-restaurant-btm-btm'
    lng = '77.62710779999999'
    base_Url = 'https://www.swiggy.com/dapi/menu/v4/full'

    final_Url = '{}?lat={}&lng={}&slug={}'.format(base_Url, lat, lng, slug)
    try:
        Response = requests.get(final_Url)
        if Response.status_code == 200:
            saveitems(Response.json())
            savebasic(Response.json())
            savesla(Response.json())

    except Exception as e:
        print("The error is :" + traceback.format_exc())


"""
This function saves items from result json
"""


def saveitems(response_json):
    items = response_json['data']['menu']['items']
    with open(response_json['data']['name']+'-items.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(
            ['Name', 'Category', 'Price', 'ImageUrl', 'Description', 'Diet Type', 'Recommended', 'Available',
             'nextAvailableAtMessage'])
        for single in items:
            image_url = items[single]['cloudinaryImageId'] if 'cloudinaryImageId' in items[single] else "none"
            diet_type = ('veg', 'nonveg')[int(items[single]['isVeg']) == 0]
            recommended = ('Not Recommended', 'Recommended')[int(items[single]['recommended']) == 1]
            available = ('Not Available', 'Available')[int(items[single]['inStock']) == 1]
            description = items[single]['description'] if 'description' in items[single] else "none"
            nxt_available = items[single]['nextAvailableAtMessage'] if 'nextAvailableAtMessage' in items[single] else "none"
            filewriter.writerow(
                [items[single]['name'], items[single]['category'], items[single]['price'], image_url, description,
                 diet_type, recommended, available, nxt_available])

    print(items)

"""
This function  saves BasicDetails from result json
"""


def savebasic(response_json):
    data = response_json['data']
    with open(response_json['data']['name']+'-BasicDetails.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        diet_type = ('veg', 'nonveg')[int(data['isVeg']) == 0]
        filewriter.writerow(
            ['name', 'latLong', 'city', 'area',
             'areaPostalCode', 'locality', 'avgRatingString', 'totalRatingsString',
             'cloudinaryImageId',  'cuisines', 'diet_type'])
        filewriter.writerow(
            [data['name'], data['latLong'], data['city'], data['area'],
             data['areaPostalCode'], data['locality'], data['avgRatingString'], data['totalRatingsString'],
             data['cloudinaryImageId'], data['cuisines'], diet_type])


"""
This function  saves sla from result json
"""


def savesla(response_json):
    data = response_json['data']['sla']

    with open(response_json['data']['name']+'-SLA-Details.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        filewriter.writerow(
            ['slaString', 'deliveryTime', 'minDeliveryTime', 'maxDeliveryTime',
             'lastMileTravel', 'thirtyMinOrFree', 'longDistance', 'rainMode'])
        filewriter.writerow(
            [data['slaString'], data['deliveryTime'], data['minDeliveryTime'], data['maxDeliveryTime'],
             data['lastMileTravel'], data['thirtyMinOrFree'], data['longDistance'], data['rainMode']])


if __name__ == '__main__':
    swiggy()
