# Run this using "asyncio"

from pyodide.http import pyfetch
from pyodide import JsException
import asyncio

py

async def login(email, password):
    headers = {
        'Authorization': 'Bearer ' + '1|akFo3mhPxK3uP6M6cMkKIx0tryIFbm3cAbC1z0U8',
        'Content-Type': 'application/json'
    }
    try:
        response = await pyfetch(
            url="http://127.0.0.1:8000/api/v1/licenses",
            method="GET",
            headers=headers
           # body=json.dumps({"email": email, "password": password})
        )
        if response.ok:
            data = await response.json()
            return data.get("token")
    except JsException:
        return None

token = await loop.run_until_complete(
    login("eve.holt@reqres.in", "cityslicka")
)
print(token)