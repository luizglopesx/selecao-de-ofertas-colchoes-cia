import os, sys, json, urllib.request, urllib.parse

IG_ACCOUNT_ID = os.environ["IG_ACCOUNT_ID"]
IG_TOKEN      = os.environ["IG_PAGE_TOKEN"]
IMAGE_URL     = sys.argv[1]
MEDIA_TYPE    = sys.argv[2]   # POST ou STORY
CAPTION       = os.environ.get("CAPTION", "")

base = "https://graph.facebook.com/v19.0"

# Criar container
params = {"image_url": IMAGE_URL, "access_token": IG_TOKEN}
if MEDIA_TYPE == "STORY":
    params["media_type"] = "STORIES"
else:
    params["caption"] = CAPTION

data = urllib.parse.urlencode(params).encode()
req  = urllib.request.Request(f"{base}/{IG_ACCOUNT_ID}/media", data=data, method="POST")
with urllib.request.urlopen(req) as r:
    creation_id = json.loads(r.read())["id"]
print(f"Container: {creation_id}")

# Publicar
data2 = urllib.parse.urlencode({"creation_id": creation_id, "access_token": IG_TOKEN}).encode()
req2  = urllib.request.Request(f"{base}/{IG_ACCOUNT_ID}/media_publish", data=data2, method="POST")
with urllib.request.urlopen(req2) as r2:
    print(f"Publicado! ID: {json.loads(r2.read())['id']}")
