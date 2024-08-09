prepare:
	sudo mkdir -p /usr/lib/uebf
	sudo chown $$(whoami) /usr/lib/uebf
	sudo cp bl.sh /usr/lib/uebf/bl.sh
	sudo chmod +x /usr/lib/uebf/bl.sh

tempinstall:
	sudo ln -sf $$PWD/main.py /usr/lib/uebf/bl.py

install:
	sudo cp -f bl.sh /usr/lib/uebf/bl.sh
	sudo chmod +x /usr/lib/uebf/bl.sh
	rm -f /usr/lib/uebf/bl.py
	sudo cp -f main.py /usr/lib/uebf/bl.py

addfmt:
	echo ':UEBF:M::ebf::/usr/lib/uebf/bl.sh:' | sudo tee /proc/sys/fs/binfmt_misc/register
