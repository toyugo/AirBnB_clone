# AirBnB_clone

### Description of the project

This project is part of a larger project in order to build a copy of the AirBnb web site (from back-end to front-end).

This project is the first step and built the back-end console of the website. This back-end is created from scratch and do not use any framework as learning purpose.

### Description of the back-end system
The back-end system is based on 3 components and build with Python 3:

1. **The storage engine**, based on a JSON file, it handle all the process of serialization/deserialization of objects.

2. **The model system**, this component contains all the function in order to create, update, delete, display any object stored in the storage engine. 
It will handle the creation of object by uniq ID, update creation time and all others attribute depending of the specify object.

3. **The console system**, is a basic console used to control the storage_engine by using any function of the model system.

### How to use
* Download all part of the project

* Launch the console.py

* Enter any command

### List of command
![GitHub function list](/img/Function_list.png)
 
### List of possible object

**Common base attribute**

* **Base Model** : id, created_at, updated_at

*It's the base of all other object-attribute*

**Specific object-attribute**

* **User** : email, password, first_name, last_name

* **Review** : place_id, user_id, text

* **Place** : city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids

* **Amenity** : name

* **State** : name

* **City** : state_id, name

### Contributor
Olivier Guyot <>
