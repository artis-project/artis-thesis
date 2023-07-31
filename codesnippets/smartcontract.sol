struct ArtworkData {
  uint256 id;
  string objectId;
  address carrier;
  address logger;
  address recipient;
  Status status;
  uint256 violationTimestamp;
}

struct StatusApprovals {
  bool carrier;
  bool owner;
  bool recipient;
}

struct Status {
  string currentStatus;
  string requestedStatus;
}

enum StatusValue {
  IN_TRANSIT,
  TO_BE_DELIVERED,
  DELIVERED,
  NONE
}

mapping(uint256 => ArtworkData) internal artworks;

mapping(uint256 => mapping(StatusValue => StatusApprovals))
  internal approvals;

event Updated(
  uint256 indexed tokenId,
  ArtworkData newData,
  address owner,
  StatusApprovals approvals
);

event StatusApproved(
  uint256 indexed tokenId,
  StatusApprovals approvals,
  address approver
);

event ApprovalMissing(
  uint256 indexed tokenId,
  string requestedStatus,
  address missingApproval
);

constructor() ERC721("Artwork", "ARTIS") {
  smartcontractAdmin = msg.sender;
}


modifier exists(uint256 tokenId) {
require(_exists(tokenId), "Token does not exist 404");
_;
}

modifier onlyAdmin() {
require(
  msg.sender == smartcontractAdmin,
  "only accessible by smartcontractAdmin wallet 403"
);
_;
}

modifier onlyOwner(address sender, uint256 tokenId) {
require(ownerOf(tokenId) == sender, "sender is not authorized 403");
_;
}

modifier onlyLogger(address sender, uint256 tokenId) {
require(loggerOf(tokenId) == sender, "sender is not authorized 403");
_;
}

modifier onlyAdmin() {
  require(
    msg.sender == smartcontractAdmin,
    "only accessible by smartcontractAdmin wallet 403"
  );  
  _;
}

modifier read(address sender, uint256 tokenId) {
  require(
    ownerOf(tokenId) == sender ||
    carrierOf(tokenId) == sender ||
    recipientOf(tokenId) == sender,
    "sender is not authorized 403"
  );
  _;
}

modifier write(address sender, ArtworkData memory data) {
  if (data.violationTimestamp != 0) {
    require(
      sender == loggerOf(data.id),
      "only logger is allowed to add a violationTimestamp 403"
    );
  }
  require(
    bytes(data.status.currentStatus).length == 0,
    "currentStatus is updated automatically 403"
  );
  if (sender != ownerOf(data.id)) {
    require(
      bytes(data.objectId).length == 0 &&
        // address(1) is submitted if the field did not change
        data.carrier == address(1) &&
        data.recipient == address(1) &&
        data.logger == address(1),
      "only owner has write permissions 403"
    );
  }
  _;
}

function updateArtworkData(ArtworkData memory data, address sender)
        public
        onlyAdmin
        exists(data.id)
        write(sender, data)
    {
        if (data.violationTimestamp != 0) { ... }
        if (bytes(data.status.requestedStatus).length != 0) { ... }
        if ((bytes(data.objectId).length != 0)) { ... }
        if (data.carrier != address(1)) { ... }
        if (data.recipient != address(1)) { ... }
        if (data.logger != address(1)) { ... }

        emit Updated( ... );
    }
