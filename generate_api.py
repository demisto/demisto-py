import requests
import json

data = {
  "swaggerUrl": ""
}

res = requests.request(
            'POST',
            'https://generator.swagger.io/api/gen/clients/python',
            data=data,
)