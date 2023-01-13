<center>

# Create virtual environment
python -m venv venv<br></br>
**activate venv** source venv/bin/activate

# Install PyTeal
pip3 install pyteal

**create** ticket_contract.py<br></br>
**create** compile_contract.py

# Compile contract
python3 compile_contract.py

# Algorand sandbox for testing
git clone https://github.com/algorand/sandbox.git<br></br>
cd sandbox<br></br>
**run sandbox** ./sandbox up -v<br></br>    
**list accounts** ./sandbox goal account list<br></br>

# Deploy contract
./sandbox copyTo *PATH-TO-APPROVAL-PROGRAM*<br></br>
./sandbox copyTo *PATH-TO-CLEAR-PROGRAM*<br></br>
-<br></br>
**create application**<br></br>
./sandbox goal app create --creator *ACCOUNT-ADDRESS* --approval-prog *PATH-TO-APPROVAL-PROGRAM* --clear-prog *PATH-TO-CLEAR-PROGRAM*.teal --note *CONTRACT-NOTE* <br></br>
~~--global-byteslices 2 --global-ints 1 --local-byteslices 0 --local-ints 0~~ <- **args types** <br></br> ~~--app-arg str:one-time --app-arg int:1 --app-arg str:entry-ticket~~ <- **contract args**
-<br></br>
**delete application**<br></br>
./sandbox goal app delete --app-id *APP-ID* --from *ACCOUNT-ADDRESS* <br></br>

# Create wallet
https://wallet.myalgo.com/new-account <br></br>
**select** testnet <br></br>
new account button <br></br>
- <br></br>
**add funding** https://bank.testnet.algorand.network/

# Create React Dapp



</center>