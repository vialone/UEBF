import sys, os

infp = sys.argv[1]

data = {}

for line in open(infp, 'rb'):
    if line.startswith(b'#!'):
        continue
    if line == b'---\n':
        break
    line = line.strip()
    if line == b'':
        continue
    key, value = line.split(b'/')
    data[key] = value

if data[b'BL'] == b'TESTBL':
    begin = False
    for line in open(infp):
        if not begin:
            if line == '---\n':
                begin = True
            continue
        cmd = line.strip().split(None, 1)[0]
        if cmd == 'echo':
            print(line.strip().split(None, 1)[1])
        elif cmd == 'exit':
            exit(int(line.strip().split(None, 1)[1]))
        else:
            print('Unknown command:', cmd)
            exit(1)
    else:
        print('Implicit exit')
        exit(0)
elif data[b'BL'] == b'ELF' and data[b'TYPE'] == b'ELFW':
    with open(infp, 'rb') as f:
        data = f.read()
    with open("/tmp/ebfelf.elf", 'wb') as f:
        f.write(data.split(b'---\n', 1)[1])
    os.system("chmod +x /tmp/ebfelf.elf")
    os.system("/tmp/ebfelf.elf")
else:
    print('Unknown bootloader:', data['BL'])
    exit(1)
