# https://www.codewars.com/kata/54acc128329e634e9a000362/train/python


def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always
    
    # Define the state transition table as a dictionary
    transitions = {
        "CLOSED": {
            "APP_PASSIVE_OPEN": "LISTEN",
            "APP_ACTIVE_OPEN": "SYN_SENT"
        },
        "LISTEN": {
            "RCV_SYN": "SYN_RCVD",
            "APP_SEND": "SYN_SENT",
            "APP_CLOSE": "CLOSED"
        },
        "SYN_RCVD": {
            "APP_CLOSE": "FIN_WAIT_1",
            "RCV_ACK": "ESTABLISHED"
        },
        "SYN_SENT": {
            "RCV_SYN": "SYN_RCVD",
            "RCV_SYN_ACK": "ESTABLISHED",
            "APP_CLOSE": "CLOSED"
        },
        "ESTABLISHED": {
            "APP_CLOSE": "FIN_WAIT_1",
            "RCV_FIN": "CLOSE_WAIT"
        },
        "FIN_WAIT_1": {
            "RCV_FIN": "CLOSING",
            "RCV_FIN_ACK": "TIME_WAIT",
            "RCV_ACK": "FIN_WAIT_2"
        },
        "CLOSING": {
            "RCV_ACK": "TIME_WAIT"
        },
        "FIN_WAIT_2": {
            "RCV_FIN": "TIME_WAIT"
        },
        "TIME_WAIT": {
            "APP_TIMEOUT": "CLOSED"
        },
        "CLOSE_WAIT": {
            "APP_CLOSE": "LAST_ACK"
        },
        "LAST_ACK": {
            "RCV_ACK": "CLOSED"
        }
    }
    
    # Process each event
    for event in events:
        if state in transitions and event in transitions[state]:
            state = transitions[state][event]
        else:
            return "ERROR"
    
    return state
