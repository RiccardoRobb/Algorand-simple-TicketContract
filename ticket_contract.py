from pyteal import *

TICKET_TYPES = [Bytes("one-time"), Bytes("life-time")]

class Ticket:
    class Variables:
        type = Bytes("Type")
        id = Bytes("Number")
        name = Bytes("Name")

    class AppMethods:
        generate = Bytes("Generate ticket")
        validate = Bytes("Validate ticket")

    def application_creation(self):
        return Seq([
            Assert(Txn.application_args.length() == Int(3), comment="error on number of arg"),
            Assert(Txn.note() == Bytes("ticket:uv1"), comment="error on txn note"),  
            Assert(Btoi(Txn.application_args[1]) > Int(0), comment="negative number not allowed"),       
            #Assert(Txn.application_args[0] in TICKET_TYPES),
            App.globalPut(self.Variables.type, Txn.application_args[0]),
            App.globalPut(self.Variables.id, Btoi(Txn.application_args[1])),
            App.globalPut(self.Variables.name, Txn.application_args[2]),
            Approve()
        ])
    
    def generate(self):
        valid_number_of_tansactions = Global.group_size() == Int(1)

        valid_payament_to_seller = And(
            Gtxn[1].type_enum() == TxnType.Payment,
            Gtxn[1].receiver() == Global.creator_address(),
            Gtxn[1].amount() == Int(1),
            Gtxn[1].sender() == Gtxn[0].sender()
        )

        can_buy = And(
            valid_number_of_tansactions,
            valid_payament_to_seller
        )

        actual_count = App.globalGet(self.Variables.id)

        update_state = Seq([
            App.globalPut(self.Variables.id, actual_count + Int(1)),
            Assert(actual_count + Int(1) == App.globalGet(self.Variables.id), comment="ticket number not incremented"),
            Approve()
        ])
        
        return If(can_buy).Then(update_state).Else(Reject())

    # Delete ticket (useless ?)
    def application_deletion(self):
        return Return(Txn.sender() == Global.creator_address())

    def application_start(self):
        return Cond(
            [Txn.application_id() == Int(0), self.application_creation()],                      #if   id==0 -> create application
            [Txn.on_completion() == OnComplete.DeleteApplication, self.application_deletion()], #elif function to complete == deletion -> call deletion method
            [Txn.application_args[0] == self.AppMethods.generate, self.generate()]              #else generate methon invoked -> call generate method
        )

    ## Must have functions
    # process all the Calls to the contract
    def approval_program(self):
        return self.application_start()

    # remove the contract from the balance record of the "caller"
    def clear_program(self):
        return Return(Int(1))