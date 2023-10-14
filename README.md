# Virtualness
Two APIs are created for this project.

To add input of cards:
```
curl --location --request POST 'http://127.0.0.1:5000/input' \
--header 'Content-Type: application/json' \
--data-raw '{
    "entry_list": [
        {
            "source": "l2",
            "destination": "l3",
            "journey_mode": "j2-j3",
            "reserve_seat": "",
            "additional_info": "a2-a3"
        },
        {
            "source": "l3",
            "destination": "l4",
            "journey_mode": "j3-j4",
            "reserve_seat": "r3-r4",
            "additional_info": "a3-a4"
        },
        {
            "source": "l1",
            "destination": "l2",
            "journey_mode": "j1-j2",
            "reserve_seat": "r1-r2",
            "additional_info": "a1-a2"
        }
    ]
}'
```

To get sorted journey cards as output:
```
curl --location --request GET 'http://127.0.0.1:5000/output'
```

There are unit tests added for service module. 
Project follows standard Model, Service, Controller pattern with exposed APIs through controller and access to model via service.

To start with project install dependencies with:
```
 sudo pip3 install flask-restful 
```

To start project:
```
python3 virtualness_controller.py
```
