from tronpy import Tron
import time

PRIVATE_KEY = "d7495b9abd05be025749bb5e6d3c83aa45f4f0d948a0e2d96d9f99f8131a70e2"
MONITORING_ADDR = "TUL16qQxphAR8nEYVy6wdRadZobZmbP5fs"
CHECK_INTERVAL = 30

client = Tron()

def check_positions():
    bal = client.get_account_balance(MONITORING_ADDR)
    usdt = client.get_contract("TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t")
    usdt_bal = usdt.functions.balanceOf(MONITORING_ADDR) / 1e6
    return {"trx": bal, "usdt": usdt_bal}

if __name__ == "__main__":
    while True:
        pos = check_positions()
        print(f"TRX: {pos['trx']} | USDT: {pos['usdt']}")
        time.sleep(CHECK_INTERVAL)
