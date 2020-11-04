# Lexa_name_service
this code must implement work with IPFS nodes, but for now it just can generate keys, sign text and check data.

There is two different programs on py. Key manager can generate you a pair of ECDSA keys, and also can sign your input.

Main is working with storage.
It have two modes, set and get. If mode is set to "set", you must type in your UID with key -u, IPFS link with key -i, and also signature of that IPFS link, which you can generate in key_manager.

Eventually code will be upgraded.
