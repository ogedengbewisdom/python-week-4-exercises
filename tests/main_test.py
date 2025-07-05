import unittest
from main import *

class TestBitcoinUtils(unittest.TestCase):

    def test_parse_txid(self):
        txid = "aabbccdd"
        self.assertEqual(parse_txid(txid), ("aa", "bb", "cc", "dd"))

    def test_create_utxo(self):
        utxo = create_utxo("tx1", 0, 1000)
        self.assertEqual(utxo, {"txid": "tx1", "vout": 0, "amount": 1000})

    def test_update_utxo(self):
        utxo = {"txid": "tx1", "vout": 0, "amount": 1000}
        update_utxo(utxo, 1500)
        self.assertEqual(utxo["amount"], 1500)

    def test_unpack_utxo(self):
        utxo = {"txid": "abc", "vout": 1, "amount": 5000}
        result = unpack_utxo(utxo)
        self.assertIn("TXID: abc", result)

    def test_swap_addresses(self):
        a, b = swap_addresses("addr1", "addr2")
        self.assertEqual((a, b), ("addr2", "addr1"))

    def test_unique_addresses(self):
        addresses = ["a", "b", "a"]
        unique = unique_addresses(addresses)
        self.assertEqual(unique, {"a", "b"})

    def test_bitcoin_wallet(self):
        self.wallet = BitcoinWallet()
        self.utxo1 = create_utxo("tx1", 0, 1.0)
        self.utxo2 = create_utxo("tx1", 1, 0.5)
        self.assertEqual(self.wallet.get_balance(), 0.0)
        self.wallet.add_utxo(self.utxo1)
        self.assertEqual(self.wallet.get_balance(), 1.0)
        self.wallet.add_utxo(self.utxo2)
        self.assertEqual(self.wallet.get_balance(), 1.5)

    def test_transaction_pool(self):
        pool = TransactionPool()
        self.assertEqual(pool.get_pool_size(), 0)
        self.assertTrue(pool.add_transaction("tx1"))
        self.assertEqual(pool.get_pool_size(), 1)
        self.assertFalse(pool.add_transaction("tx1"))  # Duplicate
        self.assertEqual(pool.get_pool_size(), 1)

    def test_block_height_generator(self):
        heights = list(block_height_generator(100, 103))
        self.assertEqual(heights, [100, 101, 102])

if __name__ == '__main__':
    unittest.main()
