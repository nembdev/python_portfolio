#! python3
"""
a program that stores multiple phrases
"""
import optparse as opt
import pyperclip as pc

parser = opt.OptionParser()

parser.add_option(
    "-m",
    "--message",
    dest="msg",
    help="Message to be copied and pasted, Options: AGREE BUSY UPSELL",
)

(options, arguments) = parser.parse_args()

msg_choice = options.msg

print(msg_choice)

TEXT = {
    "AGREE": """Yes, I agree. That sounds fine to me.""",
    "BUSY": """Sorry, can we do this later this week or next week?""",
    "UPSELL": """Would you consider making this a monthly donation?""",
}

if msg_choice in TEXT:
    pc.copy(TEXT[msg_choice])
    print("Choice: ", msg_choice, " copied to clipboard")
else:
    print("Message not found")

pc.paste()
