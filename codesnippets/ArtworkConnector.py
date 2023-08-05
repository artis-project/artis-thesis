def safeMint(self, to: bytes, data: Artwork):
  owner, mint_data = data.to_sc_mint()
  tx_hash = self._contract.functions.safeMint(
    to if not owner else owner, mint_data
  ).transact()
  event_args = self._handleEvent(tx_hash, "Transfer")
  return event_args.get("tokenId")

def updateArtworkData(self, newArtworkData: Artwork, sender: bytes):
  tx_hash = self._contract.functions.updateArtworkData(
    newArtworkData.to_sc_update(), sender
  ).transact()
  event_args = self._handleEvent(tx_hash, "Updated")
  new_data = event_args.get("newData")
  new_data = dict(new_data, **{"owner": event_args.get("owner")})
  new_data["status"] = dict(
    new_data["status"], **{"approvals": event_args.get("approvals")}
  )
  return Artwork.load(data=new_data)

def getArtworkIdsByAddress(self, address: str):
  artwork_ids = (
    self._contract.functions.getArtworkIdsByAddress(address).call()._asdict()
  )
  # incoming lists are zero padded to the total supply of tokens
  remove_zeros = lambda d: {
    k: list(filter(lambda x: x != 0, v)) for k, v in d.items()
  }
  return remove_zeros(artwork_ids)

def getArtworkData(self, artworkId: int, sender: str):
  data=self._contract.functions.getArtworkData(artworkId, sender).call()
  return Artwork.load(data=dict(data._asdict()))