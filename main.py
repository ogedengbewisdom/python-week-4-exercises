from typing import Dict, Tuple, List, Generator, Set

def parse_txid(txid: str) -> tuple:
    """
    Converts a hexadecimal txid string into a tuple of byte pairs.
    Example: 'deadbeef' -> ('de', 'ad', 'be', 'ef')
    """
    # TODO: Return a tuple of 2-character segments from txid

    list_tx = []

    for i in range(0,len(txid), 2):
        list_tx.append(txid[i: i + 2])

    return tuple(list_tx)


def create_utxo(txid: str, vout: int, amount: int) -> dict:
    """
    Creates a dictionary representing a UTXO with the given txid, vout, and amount.
    """
    # TODO: Return a dict with keys 'txid', 'vout', and 'amount'
    utxo = {
        "txid": txid, "vout": vout, "amount":amount
    }
    return utxo

def update_utxo(utxo: dict, new_amount: int) -> None:
    """
    Updates the 'amount' field in a UTXO dictionary to a new value.
    """
    # TODO: Use update to set new 'amount'
    utxo.update({"amount": new_amount})

def unpack_utxo(utxo: dict) -> str:
    """
    Unpacks a UTXO dictionary and returns a formatted string representation.
    """
    #   self.assertIn("TXID: abc", result)
    return ", ".join(f"{key.upper()}: {value}" for key, value in utxo.items())

def swap_addresses(addr1: str, addr2: str) -> tuple:
    """
    Swaps two Bitcoin addresses and returns them in reversed order.
    """
    # TODO: Swap the values and return as tuple

    return addr2, addr1

def unique_addresses(addresses: list) -> set:
    """
    Returns a set of unique Bitcoin addresses from the provided list.
    """
    # TODO: Convert the list to a set
    return set(addresses)

class BitcoinWallet:
    def __init__(self):
        """
        Initializes the wallet with an empty UTXO set.
        """
        self.utxos = set()
    
    def add_utxo(self, utxo: Dict) -> None:
        """
        Adds a UTXO to the wallet using a unique txid:vout key.
        """
        # TODO: Create key from 'txid' and 'vout', store UTXO in self.utxos

        keys = (utxo["txid"], utxo["vout"], utxo["amount"])
        self.utxos.add(keys)
    def get_balance(self) -> float:
        """
        Returns the total balance of all UTXOs in the wallet.
        """
        # TODO: Sum the 'amount' of all UTXOs
        sum = 0

        for utx in self.utxos:
            sum += utx[2]

        return sum

class TransactionPool:
    def __init__(self):
        """
        Initializes an empty transaction pool.
        """
        self.transaction_pool = set()
    
    def add_transaction(self, txid: str) -> bool:
        """
        Adds a txid to the transaction pool.
        Returns True if it was not already present, False otherwise.
        """
        # TODO: Check for presence and add if not present
        
        if txid in self.transaction_pool:
            return False
        self.transaction_pool.add(txid)
        return True
    
    def get_pool_size(self) -> int:
        """
        Returns the total number of unique transactions in the pool.
        """
        # TODO: Return length of tx_pool
        return len(self.transaction_pool)

def block_height_generator(start: int, end: int) -> Generator[int, None, None]:
    """
    Yields block heights from start to end (exclusive).
    """
    # TODO: Use a generator loop to yield block heights
    for i in range(start, end):
        yield i


# utxo_bit = BitcoinWallet()
# print(utxo_bit.add_utxo(create_utxo("tx1", 0, 1.0)))

# print("utxo", utxo_bit.utxos)

# print(utxo_bit.add_utxo(create_utxo("tx2", 0, 3.0)))

# print("utxo", utxo_bit.utxos)