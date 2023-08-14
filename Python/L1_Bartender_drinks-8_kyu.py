# https://www.codewars.com/kata/568dc014440f03b13900001d
# 2023-08-02T11:55:23.187+0000
drinks_dict = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
}
def get_drink_by_profession(param):
    return drinks_dict.get(param.lower(), "Beer")