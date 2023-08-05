def generate_client_auth_payload(self, address: str, chain_id: str):
  return {
    "payload": {
      "version": "1",
      "type": "evm",
      "domain": "artis-project",
      "address": address,
      "chain_id": chain_id,
      "nonce": str(uuid4()),
      "issued_at": datetime.now(self.timezone).strftime(self.timeformat),
      "expiration_time": (
          datetime.now(self.timezone) + timedelta(hours=1)
      ).strftime(self.timeformat),
    }
}

def verify(
  self,
  domain: str,
  payload: LoginPayload,
  options: VerifyOptions = VerifyOptions(),
) -> str:

  ... # perform checks (e.g. expiration date)

  message = self._generate_message(payload.payload)
  user_address = self._recover_address(message, payload.signature)
  if user_address.lower() != payload.payload.address.lower():
      raise Unauthorized(
          f"The intended payload address '{payload.payload.address.lower()}' is not the payload signer"
      )
  return user_address