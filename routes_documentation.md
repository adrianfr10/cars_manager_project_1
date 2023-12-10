## CARS SERVICE ROUTES

### 1. Group cars by given params

Running the route with example parameters:

> http://localhost/given_param/mileage-1?token=8vdsQp-4VBMOMxaq3hTjsg

Will produce results similar to this:

[

    {
        "color": "WHITE",
        "components": [
            "AIR CONDITIONING",
            "BLUETOOTH"
        ],
        "mileage": 2500,
        "model": "MAZDA",
        "price": "120000"
    },
    {
        "color": "WHITE",
        "components": [
            "AIR CONDITIONING",
            "BLUETOOTH"
        ],
        "mileage": 2500,
        "model": "FIAT",
        "price": "140000"
    },
    {
        "color": "BLACK",
        "components": [
            "ABS",
            "ALLOY WHEELS"
        ],
        "mileage": 1500,
        "model": "BMW",
        "price": "160000"
    }
]

Description:

The result is a json list of cars sorted by mileage - descending.

### 2. Cars with mileage greater than

Running the route with example parameters:

> http://localhost/mileage_threshold/1800?token=8vdsQp-4VBMOMxaq3hTjsg


Will produce results similar to this:

[

    {
        "color": "WHITE",
        "components": [
            "AIR CONDITIONING",
            "BLUETOOTH"
        ],
        "mileage": 2500,
        "model": "MAZDA",
        "price": "120000"
    },
    {
        "color": "WHITE",
        "components": [
            "AIR CONDITIONING",
            "BLUETOOTH"
        ],
        "mileage": 2500,
        "model": "FIAT",
        "price": "140000"
    }
]


Description:

Result is a json list of cars that have mileage higher than
specified value, in this case 1800

### 3. Count cars colors

Running the route with example parameters:

> http://localhost/cars/counted/color?token=8vdsQp-4VBMOMxaq3hTjsg

Will produce results similar to this:

{

    "BLACK": 1,
    "WHITE": 2
}


Description:
Result is a json of color names and values - count of cars in the
collection with this color.

### 4. Most expensive cars from models

Running the route with example parameters:

> http://localhost/models?token=8vdsQp-4VBMOMxaq3hTjsg


Will produce results similar to this:

{

    "BMW": [
        {
            "color": "BLACK",
            "components": [
                "ABS",
                "ALLOY WHEELS"
            ],
            "mileage": 1500,
            "model": "BMW",
            "price": "160000"
        }
    ],
    "FIAT": [
        {
            "color": "WHITE",
            "components": [
                "AIR CONDITIONING",
                "BLUETOOTH"
            ],
            "mileage": 2500,
            "model": "FIAT",
            "price": "140000"
        }
    ],
    "MAZDA": [
        {
            "color": "WHITE",
            "components": [
                "AIR CONDITIONING",
                "BLUETOOTH"
            ],
            "mileage": 2500,
            "model": "MAZDA",
            "price": "120000"
        }
    ]
}


Description:

Result is a json of a structure: key: car model name ,
value: list of most expensive car(s) from given model

### 5. Cars with sorted components

Running the route with example parameters:

> http://localhost/cars/sort/components?token=8vdsQp-4VBMOMxaq3hTjsg


Will produce results similar to this:

[

    {
        "color": "BLACK",
        "components": [
            "ABS",
            "ALLOY WHEELS"
        ],
        "mileage": 1500,
        "model": "BMW",
        "price": "160000"
    },
    {
        "color": "WHITE",
        "components": [
            "AIR CONDITIONING",
            "BLUETOOTH"
        ],
        "mileage": 2500,
        "model": "MAZDA",
        "price": "120000"
    },
    {
        "color": "WHITE",
        "components": [
            "AIR CONDITIONING",
            "BLUETOOTH"
        ],
        "mileage": 2500,
        "model": "FIAT",
        "price": "140000"
    }
]


Description:
Result is a collection of cars with components sorted phonetically

### 6. Cars statistics

Running the route with example parameters:

> http://localhost/cars/statistics/mileage?token=8vdsQp-4VBMOMxaq3hTjsg

Will produce results similar to this:

{

    "MILEAGE": {
        "avg": 2166.666,
        "max": 2500,
        "min": 1500
    }
}

Description:
Result is a json of statistics of the cars collection:
min, max and avg of a specified parameter, in this case - mileage

### 7. Group cars by price range
Running the route with example parameters:

> http://localhost/price/130000-300000?token=8vdsQp-4VBMOMxaq3hTjsg

Will produce results similar to this:

[

    {
        "color": "BLACK",
        "components": [
            "ABS",
            "ALLOY WHEELS"
        ],
        "mileage": 1500,
        "model": "BMW",
        "price": "160000"
    },
    {
        "color": "WHITE",
        "components": [
            "AIR CONDITIONING",
            "BLUETOOTH"
        ],
        "mileage": 2500,
        "model": "FIAT",
        "price": "140000"
    }
]

Description:
Result is a collection of cars with a price between specified
min and max value

### 8. Most expensive cars

Running the route with example parameters:

> http://localhost/?token=8vdsQp-4VBMOMxaq3hTjsg

Will produce results similar to this:

[

    {
        "color": "BLACK",
        "components": [
            "ABS",
            "ALLOY WHEELS"
        ],
        "mileage": 1500,
        "model": "BMW",
        "price": "160000"
    }
]

Description:

Result is a list of most expensive cars from the entire collection

### 9. Group cars by components

Running the route with example parameters:

> http://localhost/components?token=8vdsQp-4VBMOMxaq3hTjsg

Will produce results similar to this:

{

    "ABS": [
        {
            "color": "BLACK",
            "components": [
                "ABS",
                "ALLOY WHEELS"
            ],
            "mileage": 1500,
            "model": "BMW",
            "price": "160000"
        }
    ],
    "AIR CONDITIONING": [
        {
            "color": "WHITE",
            "components": [
                "AIR CONDITIONING",
                "BLUETOOTH"
            ],
            "mileage": 2500,
            "model": "MAZDA",
            "price": "120000"
        },
        {
            "color": "WHITE",
            "components": [
                "AIR CONDITIONING",
                "BLUETOOTH"
            ],
            "mileage": 2500,
            "model": "FIAT",
            "price": "140000"
        }
    ],
    "ALLOY WHEELS": [
        {
            "color": "BLACK",
            "components": [
                "ABS",
                "ALLOY WHEELS"
            ],
            "mileage": 1500,
            "model": "BMW",
            "price": "160000"
        }
    ],
    "BLUETOOTH": [
        {
            "color": "WHITE",
            "components": [
                "AIR CONDITIONING",
                "BLUETOOTH"
            ],
            "mileage": 2500,
            "model": "MAZDA",
            "price": "120000"
        },
        {
            "color": "WHITE",
            "components": [
                "AIR CONDITIONING",
                "BLUETOOTH"
            ],
            "mileage": 2500,
            "model": "FIAT",
            "price": "140000"
        }
    ]
}

Description:

Result is a collection of keys: components and values: cars
with this component

## SECURITY ROUTES

### 1. Verify token

Running the route with example parameters:

> http://localhost/verify?token=8vdsQp-4VBMOMxaq3hTjsg


Will produce results similar to this:

{

    "message": "Token is valid"

}

Description:

Result is a message telling if the token you provided as a parameter is valid

### 2. Register user

Running the route with example parameters:

> http://localhost/register

And providing your email in the request body like that:

{

    "email": "your_email@gmail.com"
}

Will produce results similar to this:

{

    "message": "Email with token sent"
}

Description:
Result is a message telling if sending an email with token
is successful or not