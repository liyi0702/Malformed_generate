#coding:UTF-8
from enum import Enum
import re,random
import os, sys



file_num = len([j for i in [i[2] for i in os.walk(os.getcwd())] for j in i])

normal = \
'''REGISTER sip:[Server_Uri] {SIP/2.0}
Call-ID: [Call_Id]@[IP]
CSeq: [CSeq] REGISTER
From: \"linfeng\" <sip:[From_User]@[Server_Uri]>;tag=[Tag]
To: \"linfeng\" <sip:[From_User]@[Server_Uri]>
Via: SIP/2.0/UDP [IP]:[PORT];branch=[Branch]
Max-Forwards: 20
Expires: 10800
Authorization: Digest username=\"[From_User]@[Server_Uri]\",realm=\"[Server_Uri]\",nonce=\"\",response=\"\",uri=\"sip:[Server_Uri]\"
Supported: path
Contact: <sip:[IP]:[PORT]>
P-Preferred-Identity: \"linfeng\" <sip:[From_User]@[Server_Uri]>
P-Access-Network-Info: 3GPP-UTRAN-TDD; utran-cell-id-3gpp=00000000
Privacy: none
User-Agent: Fraunhofer FOKUS/NGNI Java IMS UserEndpoint FoJIE 0.1 (jdk1.3)
Allow: INVITE,ACK,CANCEL,BYE,MESSAGE,NOTIFY
Content-Length: 0
'''


Fields = ["HEAD", "Call-ID", "CSeq", "From", "To", "Via", "Max-Forwards", "Expires", "Authorization", "Support",
          "Contact", "P-Preferred-Identity", "P-Access-Network-Info", "Privacy", "User-Agent", "Allow", "Content-Length"]

a1 = re.compile(r'\[.*?\]')

def field_missing(message):
    field_slice = message.split('\n')
    # print [i for i in field_slice]
    missing_field = random.choice(field_slice)
    field_slice.remove((missing_field))
    print missing_field
    print
    new_message = "\n".join(field_slice)
    return new_message

def field_repeat(message):
    field_slice = message.split('\n')
    # print [i for i in field_slice]
    repeat_field = random.choice(field_slice)
    field_slice.insert(field_slice.index(repeat_field), repeat_field)
    new_message = "\n".join(field_slice)
    print new_message
    return new_message

def misorder(message):
    return

def field_empty():
    return ""

def field_overflow_general():
    dup_length = random.randint(1024, 32768)
    char_set = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789~!`@#$%^&*()_+-=.<>?:;/|'
    char_set_len = len(char_set) - 1
    dup_char = char_set[random.randint(0, char_set_len)]
    # general_str = "%s(%d)" % (dup_char, dup_length)
    general_str = dup_char * dup_length
    return general_str

def field_overflow_null():
    dup_length = random.randint(1024, 32768)
    dup_char = ' '
    # char_set = ' \t\n\r'
    # char_set_len = len(char_set) - 1
    # dup_char = char_set[random.randint(0, char_set_len)]
    # null_str = " (%d)" % (dup_length)
    null_str = dup_char * dup_length
    return null_str

def field_UTF8():
    dup_length = random.randint(1024, 32768)
    dup_char = ' \\xe'
    # UTF8_str = "\\xe(%d)" % (dup_length)
    UTF8_str = dup_char * dup_length
    return UTF8_str


sub_list = a1.findall(normal)
message_malformed_list = ["field_missing", "field_repeat", "field_normal"]
field_malformed_list = ["field_empty", "field_overflow_general",  "field_overflow_null", "field_UTF8"]


lis = []
for i in range(len(sub_list)):
    malformed_type = random.choice(field_malformed_list)
    s = eval(malformed_type)()
    lis.append(s)

# for i in sub_list:
#     print(i)
#
# for i in lis:
#     print (i)

def malfromed_message_genernate():
    for i in range(10):
        print i
        new = normal
        for j in range(len(sub_list)):
            new = new.replace(sub_list[j], lis[j])
        file_name = 'data%d.txt' % i
        output = open(file_name, 'w')
        output.write(new)
        output.close()
    return

field_missing(normal)
field_repeat(normal)

