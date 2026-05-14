# Description: This script practices using dictionaries for address information
# Author: Mohamed Mouatakid

contact_info = {
    "name": "Mohamed Mouatakid",
    "address": "123 Main Street",
    "city": "Alexandria",
    "state": "VA",
    "zip": "22314"
}

print(f"""{contact_info["name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")

contact_info.pop("name")

full_name = {
    "first name": "Mohamed",
    "last name": "Mouatakid"
}

full_name.update({"honorific": "Mr."})
contact_info.update({"full_name": full_name})

print("\nUpdated address:")
print(f"""{contact_info["full_name"]["honorific"]} {contact_info["full_name"]["first name"]} {contact_info["full_name"]["last name"]}
{contact_info["address"]}
{contact_info["city"]}, {contact_info["state"]} {contact_info["zip"]}""")
