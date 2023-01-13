from pyteal import *
from ticket_contract import Ticket

if __name__ == "__main__":
    approval_program = Ticket().approval_program()
    clear_program = Ticket().clear_program()

    compiled_approval = compileTeal(approval_program, Mode.Application, version=6)

    with open("ticket_approval.teal", "w") as teal:
        teal.write(compiled_approval)
        teal.close()

    compiled_clear = compileTeal(clear_program, Mode.Application, version=6)

    with open("ticket_clear.teal", "w") as teal:
        teal.write(compiled_clear)
        teal.close()
        