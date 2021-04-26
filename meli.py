from pip._vendor import requests
import json

def request_data():
	
    # Test ID --> 179571326
	user_id = input("Ingrese el ID del usuario que desea buscar: ")
	info_request = requests.get(f"https://api.mercadolibre.com/sites/MLA//search?seller_id={user_id}").json()
	
	info_request = info_request['results']
	
	try:
		with open(f"{user_id}.log", "w+") as file:
		
			file.write("ID - TITLE - CATEGORY_ID - NAME\n")
		
			for key in info_request:
				id = key["id"]
				title = key["title"]
				category_id = key["category_id"]
				name = key["domain_id"]
			
				file.writelines(f"{id} - {title} - {category_id} - {name}\n")
			
			print("Archivo log se ha guardado sin errores")
			
	except IOError:
		print("Se ha producido un error")

request_data()