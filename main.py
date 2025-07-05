from typing import Dict, Tuple, List, Generator, Set

def parse_txid(txid: str) -> tuple:
    """
    Converts a hexadecimal txid string into a tuple of byte pairs.
    Example: 'deadbeef' -> ('de', 'ad', 'be', 'ef')
    """
    # TODO: Return a tuple of 2-character segments from txid
    pass

def create_utxo(txid: str, vout: int, amount: int) -> dict:
    """
    Creates a dictionary representing a UTXO with the given txid, vout, and amount.
    """
    # TODO: Return a dict with keys 'txid', 'vout', and 'amount'
    pass

def update_utxo(utxo: dict, new_amount: int) -> None:
    """
    Updates the 'amount' field in a UTXO dictionary to a new value.
    """
    # TODO: Use update to set new 'amount'
    pass

def unpack_utxo(utxo: dict) -> str:
    """
    Unpacks a UTXO dictionary and returns a formatted string representation.
    """
    # TODO: Unpack the dictionary and return formatted string
    pass

def swap_addresses(addr1: str, addr2: str) -> tuple:
    """
    Swaps two Bitcoin addresses and returns them in reversed order.
    """
    # TODO: Swap the values and return as tuple
    pass

def unique_addresses(addresses: list) -> set:
    """
    Returns a set of unique Bitcoin addresses from the provided list.
    """
    # TODO: Convert the list to a set
    pass

class BitcoinWallet:
    def __init__(self):
        """
        Initializes the wallet with an empty UTXO set.
        """
    
    def add_utxo(self, utxo: Dict) -> None:
        """
        Adds a UTXO to the wallet using a unique txid:vout key.
        """
        # TODO: Create key from 'txid' and 'vout', store UTXO in self.utxos
        pass
    
    def get_balance(self) -> float:
        """
        Returns the total balance of all UTXOs in the wallet.
        """
        # TODO: Sum the 'amount' of all UTXOs
        pass

class TransactionPool:
    def __init__(self):
        """
        Initializes an empty transaction pool.
        """
    
    def add_transaction(self, txid: str) -> bool:
        """
        Adds a txid to the transaction pool.
        Returns True if it was not already present, False otherwise.
        """
        # TODO: Check for presence and add if not present
        pass
    
    def get_pool_size(self) -> int:
        """
        Returns the total number of unique transactions in the pool.
        """
        # TODO: Return length of tx_pool
        pass

def block_height_generator(start: int, end: int) -> Generator[int, None, None]:
    """
    Yields block heights from start to end (exclusive).
    """
    # TODO: Use a generator loop to yield block heights
    pass
