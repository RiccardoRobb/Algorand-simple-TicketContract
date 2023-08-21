<center>

[Check for more info](./infoDict/)

---

# Create virtual environment
python -m venv venv

**activate venv** source venv/bin/activate

# Install PyTeal
pip3 install pyteal

**create** ticket_contract.py

**create** compile_contract.py

# Compile contract
python3 compile_contract.py

# Algorand sandbox for testing
git clone https://github.com/algorand/sandbox.git

cd sandbox

**run sandbox** ./sandbox up -v   

**list accounts** ./sandbox goal account list

# Deploy contract
./sandbox copyTo *PATH-TO-APPROVAL-PROGRAM*

./sandbox copyTo *PATH-TO-CLEAR-PROGRAM*

**create application**
./sandbox goal app create --creator *ACCOUNT-ADDRESS* --approval-prog *PATH-TO-APPROVAL-PROGRAM* --clear-prog *PATH-TO-CLEAR-PROGRAM*.teal --note *CONTRACT-NOTE*

~~--global-byteslices 2 --global-ints 1 --local-byteslices 0 --local-ints 0~~ <- **args types** 

~~--app-arg str:one-time --app-arg int:1 --app-arg str:entry-ticket~~ <- **contract args**

**delete application**
./sandbox goal app delete --app-id *APP-ID* --from *ACCOUNT-ADDRESS*

# Create wallet
https://wallet.myalgo.com/new-account 

**select** testnet

new account button

**add funding** https://bank.testnet.algorand.network/

</center>
