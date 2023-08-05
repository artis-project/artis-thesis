@app.get("/artworks")
@auth_required(authenticator)
def get_all() -> dict:
  return {"artworks": sc.getArtworkIdsByAddress(g.sender)}

@app.post("/artworks")
@auth_required(authenticator)
def mint() -> dict:
  artworkData = Artwork.load_from_mint(request.get_json())
  return {"tokenId": sc.safeMint(to=g.sender, data=artworkData)}

@app.get("/artworks/<int:artwork_id>")
@auth_required(authenticator)
def get(artwork_id: int) -> dict:
  return sc.getArtworkData(artwork_id, g.sender).dump()

@app.patch("/artworks/<int:artwork_id>")
@auth_required(authenticator)
def update(artwork_id: int) -> dict:
  newArtworkData = Artwork.load(request.get_json() | {"id": artwork_id})
  return sc.updateArtworkData(newArtworkData, g.sender).dump()
