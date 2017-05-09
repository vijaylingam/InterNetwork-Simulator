__author__ = 'vijaychandra'

S1ip = '192.168.1.99'
S2ip = '192.168.2.99'
S3ip = '192.168.3.99'
S4ip = '192.168.4.99'
S5ip = '192.168.5.99'

final = []

def H1(sourceip, destip, message):
    ip = '192.168.1.1'
    mask = '255.255.255.0'
    subnetID = '192.168.1.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S1(sourceip, destip, message, 'no')

def H11(sourceip, destip, message):
    ip = '192.168.1.11'
    mask = '255.255.255.0'
    subnetID = '192.168.1.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S1(sourceip, destip, message, 'no')

def H2(sourceip, destip, message):
    ip = '192.168.1.2'
    mask = '255.255.255.0'
    subnetID = '192.168.1.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S1(sourceip, destip, message)

def S1(sourceip, destip, message, switch):
    MTU = 150
    print('Length of message at Switch 1 is: ', len(message))
    if len(message) > 150:
        x = 0
        for i in range(-(-len(message)//MTU)):
            no = (-(-len(message)//MTU))
            msg = message[x:x+MTU]
            x = x+MTU
            if destip == '192.168.1.1':
                print('Switch 1 sending packet ',i+1,'/',no, ' to ', destip)
                H1(sourceip, destip, msg)
            elif destip == '192.168.1.11':
                print('Switch 1 sending packet ',i+1,'/',no, ' to ', destip)
                H11(sourceip, destip, msg)
            elif destip == '192.168.1.2':
                print('Switch 1 sending packet ',i+1,'/',no, ' to ', destip)
                H2(sourceip, destip, msg)
            else:
                if (destip[:10] == S4ip[:10]) or (destip[:10] == S5ip[:10]):
                    print('Switch 1 sending packet ',i+1,'/',no, ' to Switch 4')
                    S4(sourceip, destip, msg, 'S1')
                if (destip[:10] == S2ip[:10]) or (destip[:10] == S3ip[:10]):
                    print('Switch 1 sending packet ',i+1,'/',no, ' to Switch 2')
                    S2(sourceip, destip, msg, 'S1')
    else:
        if destip == '192.168.1.1':
            H1(sourceip, destip, message)
        elif destip == '192.168.1.11':
            H11(sourceip, destip, message)
        elif destip == '192.168.1.2':
            H2(sourceip, destip, message)
        else:
            if (destip[:10] == S4ip[:10]) or (destip[:10] == S5ip[:10]):
                S4(sourceip, destip, message, 'S1')
            if (destip[:10] == S2ip[:10]) or (destip[:10] == S3ip[:10]):
                S2(sourceip, destip, message, 'S1')


def H7(sourceip, destip, message):
    ip = '192.168.2.7'
    mask = '255.255.255.0'
    subnetID = '192.168.2.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S2(sourceip, destip, message, 'no')

def S2(sourceip, destip, message, switch):
    MTU = 50
    print('Length of message at Switch 2 is: ', len(message))
    if len(message) > MTU:
        x = 0
        for i in range(-(-len(message)//MTU)):
            no = (-(-len(message)//MTU))
            msg = message[x:x+MTU]
            x = x+MTU
            if destip == '192.168.2.7':
                print('Switch 2 sending packet ',i+1,'/',no, ' to ', destip)
                H7(sourceip, destip, msg)
            else:
                if (destip[:10] == S1ip[:10] or destip[:10] == S4ip[:10] or destip[:10] == S5ip[:10]) and switch != 'S1':
                    print('Switch 2 sending packet ',i+1,'/',no, ' to Switch 1')
                    S1(sourceip, destip, msg, 'S2')
                if destip[:10] == S3ip[:10] and switch != 'S3':
                    print('Switch 2 sending packet ',i+1,'/',no, ' to Switch 3')
                    S3(sourceip, destip, msg, 'S2')
    else:
        if destip == '192.168.2.7':
            H7(sourceip, destip, message)
        else:
            if (destip[:10] == S1ip[:10] or destip[:10] == S4ip[:10] or destip[:10] == S5ip[:10]) and switch != 'S1':
                S1(sourceip, destip, message, 'S2')
            if destip[:10] == S3ip[:10] and switch != 'S3':
                S3(sourceip, destip, message, 'S2')

def H5(sourceip, destip, message):
    ip = '192.168.3.5'
    mask = '255.255.255.0'
    subnetID = '192.168.3.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S3(sourceip, destip, message, 'no')

def H10(sourceip, destip, message):
    ip = '192.168.3.10'
    mask = '255.255.255.0'
    subnetID = '192.168.3.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S3(sourceip, destip, message, 'no')

def H6(sourceip, destip, message):
    ip = '192.168.3.6'
    mask = '255.255.255.0'
    subnetID = '192.168.3.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S3(sourceip, destip, message, 'no')

def S3(sourceip, destip, message, switch):
    MTU = 100
    print('Length of message at Switch 3 is: ', len(message))
    if len(message) > MTU:
        x = 0
        for i in range(-(-len(message)//MTU)):
            no = (-(-len(message)//MTU))
            msg = message[x:x+MTU]
            x = x+MTU
            if destip == '192.168.3.5':
                print('Switch 3 sending packet ',i+1,'/',no, ' to ', destip)
                H5(sourceip, destip, msg)
            elif destip == '192.168.3.10':
                print('Switch 3 sending packet ',i+1,'/',no, ' to ', destip)
                H10(sourceip, destip, msg)
            elif destip == '192.168.3.6':
                print('Switch 3 sending packet ',i+1,'/',no, ' to ', destip)
                H6(sourceip, destip, msg)
            else:
                if destip[:10] == S2ip[:10] or destip[:10] == S1ip[:10] or destip[:10] == S4ip[:10] or destip[:10] == S5ip[:10]:
                    print('Switch 3 sending packet ',i+1,'/',no, ' to Switch 2')
                    S2(sourceip, destip, msg, 'S3')
    else:
        if destip == '192.168.3.5':
            H5(sourceip, destip, message)
        elif destip == '192.168.3.10':
            H10(sourceip, destip, message)
        elif destip == '192.168.3.6':
            H6(sourceip, destip, message)
        else:
            if destip[:10] == S2ip[:10] or destip[:10] == S1ip[:10] or destip[:10] == S4ip[:10] or destip[:10] == S5ip[:10]:
                S2(sourceip, destip, message, 'S3')

def H3(sourceip, destip, message):
    ip = '192.168.4.3'
    mask = '255.255.255.0'
    subnetID = '192.168.4.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S4(sourceip, destip, message, 'no')

def H4(sourceip, destip, message):
    ip = '192.168.4.4'
    mask = '255.255.255.0'
    subnetID = '192.168.4.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S4(sourceip, destip, message, 'no')

def S4(sourceip, destip, message, switch):
    MTU = 50
    print('Length of message at Switch 4 is: ', len(message))
    if len(message) > MTU:
        x = 0
        for i in range(-(-len(message)//MTU)):
            no = (-(-len(message)//MTU))
            msg = message[x:x+MTU]
            x = x+MTU
            if destip == '192.168.4.3':
                print('Switch 4 sending packet ',i+1,'/',no, ' to ', destip)
                H3(sourceip, destip, msg)
            elif destip == '192.168.4.4':
                print('Switch 4 sending packet ',i+1,'/',no, ' to ', destip)
                H4(sourceip, destip, msg)
            else:
                if (destip[:10] == S1ip[:10] or destip[:10] == S2ip[:10] or destip[:10] == S3ip[:10]) and switch != 'S1':
                    print('Switch 4 sending packet ',i+1,'/',no, ' to Switch 1')
                    S1(sourceip, destip, msg, 'S4')
                if destip[:10] == S5ip[:10]:
                    print('Switch 4 sending packet ',i+1,'/',no, ' to Switch 5')
                    S5(sourceip, destip, msg, 'S4')
    else:
        if destip == '192.168.4.3':
            H3(sourceip, destip, message)
        elif destip == '192.168.4.4':
            H4(sourceip, destip, message)
        else:
            if (destip[:10] == S1ip[:10] or destip[:10] == S2ip[:10] or destip[:10] == S3ip[:10]) and switch != 'S1':
                S1(sourceip, destip, message, 'S4')
            if destip[:10] == S5ip[:10]:
                S5(sourceip, destip, message, 'S4')

def H8(sourceip, destip, message):
    ip = '192.168.5.8'
    mask = '255.255.255.0'
    subnetID = '192.168.5.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S5(sourceip, destip, message, 'no')

def H12(sourceip, destip, message):
    ip = '192.168.5.12'
    mask = '255.255.255.0'
    subnetID = '192.168.5.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S5(sourceip, destip, message, 'no')

def H9(sourceip, destip, message):
    ip = '192.168.5.9'
    mask = '255.255.255.0'
    subnetID = '192.168.5.0/24'
    if destip == ip:
        final.append(message)
        print(ip + ' received message', message, 'from', sourceip)
    else:
        S5(sourceip, destip, message, 'no')

def S5(sourceip, destip, message, switch):
    MTU = 200
    print('Length of message at Switch 5 is: ', len(message))
    if len(message) > MTU:
        x = 0
        for i in range(-(-len(message)//MTU)):
            no = (-(-len(message)//MTU))
            msg = message[x:x+MTU]
            x = x+MTU
            if destip == '192.168.5.8':
                print('Switch 5 sending packet ',i+1,'/',no, ' to ', destip)
                H8(sourceip, destip, msg)
            elif destip == '192.168.5.12':
                print('Switch 5 sending packet ',i+1,'/',no, ' to ', destip)
                H12(sourceip, destip, msg)
            elif destip == '192.168.5.9':
                print('Switch 5 sending packet ',i+1,'/',no, ' to ', destip)
                H9(sourceip, destip, msg)
            else:
                print('Switch 5 sending packet ',i+1,'/',no, ' to Switch 4')
                S4(sourceip, destip, msg, 'S5')
    else:
        if destip == '192.168.5.8':
            H8(sourceip, destip, message)
        elif destip == '192.168.5.12':
            H12(sourceip, destip, message)
        elif destip == '192.168.5.9':
            H9(sourceip, destip, message)
        else:
            S4(sourceip, destip, message, 'S5')


################################
#        Host Details          #
################################
print("\t\tHOST DETAILS")
print("IP address of H1: 192.168.1.1")
print("IP address of H11: 192.168.1.11")
print("IP address of H2: 192.168.1.2")
print("IP address of H3: 192.168.4.3")
print("IP address of H4: 192.168.4.4")
print("IP address of H5: 192.168.3.5")
print("IP address of H10: 192.168.3.10")
print("IP address of H6: 192.168.3.6")
print("IP address of H7: 192.168.2.7")
print("IP address of H8: 192.168.5.8")
print("IP address of H12: 192.168.5.12")
print("IP address of H9: 192.168.5.9")
print("********************************")
print("\t\tMTU DETAILS")
print("MTU of Switch 1: 150bytes")
print("MTU of Switch 2: 50bytes")
print("MTU of Switch 3: 100bytes")
print("MTU of Switch 4: 50bytes")
print("MTU of Switch 5: 200bytes")
print("********************************")

# TEST CASES
#H11('192.168.1.11', '192.168.1.2', 'text1')
# H6('192.168.3.6', '192.168.5.9', 'text2')
# H4('192.168.4.4', '192.168.3.5', 'text3')
# H12('192.168.5.12', '192.168.3.5', 'text4')

while(True):
    sourceip = input('Enter source IP address: ')
    destip = input('Enter destination IP address: ')
    msg = input('Enter message: ')
    eval("H"+sourceip[10:]+"("+"'"+sourceip+"'"+","+"'"+destip+"'"+","+"'"+msg+"'"+")")
    print("Final Message received by H"+ str(sourceip[10:]) +' is: ', ''.join(final))
    final.clear()
    print("***************************************************")

