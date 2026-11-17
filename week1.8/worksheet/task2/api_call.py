
import httpx

base_url = "https://dummyjson.com/"

# responseCode = 200
# index = 1
# sum = 0
# while responseCode == 200:
#     content = "product/" + str(index)
content = "posts/5"

url = base_url + content  # API request

response = httpx.get(url)   # API call

#responseCode = response.status_code   # HTTP response

content = response.json()   # JSON data

print(content)

#for i in content.values():
   # if type(i) != str:
        #    continue
  #  if "apple" in i:
      #  sum+=1
      #  continue

#for i in content.keys():
   # if type(i) != str:
      #  continue
   # if "apple" in i:
      #  sum+=1
      #  continue
#index+=1
#print(index)

#print(sum)
