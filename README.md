GNU Radio Blocks for USRP Applications
========
**How to Build:**
```sh
$ git https://github.com/daniSi90/gr-myBlocks.git
$ cd gr-myBlocks/
$ mkdir build         #make build folder
$ cd build/
$ cmake ../           #build makefiles
$ make                #build toolbox
$ sudo make install
```

**1. Example: Angle of Arrival with MUSIC Algorithm**

Hardware used:
- 2x X310 USRP (Receiving)
- 1x NI USRP-2922 (Target Signal)
- 1x NI USRP-2920 (Reference Signal)

Development platform
- GNU Radio 3.7.10
- UHD 3.10.00
- Ubuntu 14.04

Dependencies
- Qt 4.8.6
- Qwt 6.0.0
- Armadillo C++ Library

**2. Example:**