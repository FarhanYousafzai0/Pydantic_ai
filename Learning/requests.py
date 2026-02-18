# from httpx import AsyncClient
# import asyncio

# async def fetch_data():
#     async with httpx.AsyncClient() as client:
#         url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
#         response = await client.get(url)

#         response.raise_for_status()  # Professional safety

#         data = response.json()

#         # Check success properly
#         if data.get("success") and "data" in data:
#             user_data = data["data"]

#             username = user_data["login"]["username"]
#             country = user_data["location"]["country"]

#             return f"Username: {username}, Country: {country}"

#         else:
#             raise Exception("API returned unsuccessful response")

# async def main():
#     try:
#         result = await fetch_data()
#         print(result)
#     except Exception as e:
#         print(f"Error: {e}")

# asyncio.run(main())
