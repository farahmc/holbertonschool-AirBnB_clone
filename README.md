# hbnb - an AirBnB clone :city_sunrise:

<p align="center" width="100%">
    <img src="https://github.com/farahmc/holbertonschool-AirBnB_clone/blob/main/hbnb.png">
</p>

## Description :speech_balloon:

The first step towards building a full web application, this repository contains a back-end console which will manage the coming projects: HTML/CSS templating, database storage, API and front-end integration.

### Coding Style :technologist:
All files are written in Python programming language and follows [PyCodeStyle](https://pypi.org/project/pycodestyle/).

### Usage :clapper:
The hbnb console works in both interactive and non-interactive mode. In interactive mode, a prompt is printed and it waits for input from the user.
```
$ ./console.py
(hbnb)
```
In non-interactive mode, a command can be piped:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Console Commands :computer:
| Command | Description |
| -------| ----------- |
| quit | Quits the console |
|EOF | Quits the console |
| help | Displays help page |
| create <class> | Creates a new instance of a given class with a unique ID and saves it to a JSON file |
| show <class> <id> | Prints the string representation of a class instance based on the class name and ID|
| destroy <class> <id> | Deletes and instance based on the class name and id and saves it to a JSON file |
| all | Prints all string representation of all instances based or not on the class name |
| update | Updates an instance based on the class name and id by adding or updating attribute and saves changes to a JSON file |

### File Descriptions :floppy_disk:
- **console.py:** hbnb console
- *models* directory:
  - **amenity.py:** Class Amenity. Attributes: name.
  - **base_model.py:** Class BaseModel which all other classes inherit from. Attributes: id, created_at, updated_at.
  - **city.py:** Class City. Attributes: state_id, name.
  - **place.py:** Class Place. Attributes: city_id, user_id, name, description, number_rooms, number_bathrooms, max_gest, price_by_night, latitude, longitude, amenity_ids.
  - **review.py:** Class Review. Attributes: place_id, user_id, text.
  -  **state.py:** Class State. Attributes: name.
  - **user.py:** Class User. Attributes: email, password, first_name, last_name.
  - *engine* directory:
    - **file_storage.py**: serializes instances to a JSON file and deserializes JSON file to instances
  
 ## Unit Testing
 Unit tests are stored in the *tests* directory. To run unit tests, run the following command:
 ```
 python3 -m unittest discover tests
 ```
  
 ## Authors :pencil2:
- Jacqueline Lu [[Jql11](https://github.com/Jql11)]
- Farah McCurdy [[farahmc](https://github.com/farahmc)]
- Karoline Silva [[Karoline-S](https://github.com/Karoline-S)]
