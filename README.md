# MadPy

A simple Python interface to run MadGraph

# How to use this module 

Requirements:
- Python 3.6+
- MadGraph 3.6+
- AND Python 2.7 (for MadDM compatibility)
- AND MadGraph 2.9 (for MadDM compatibility)
- ghostscript

 sudo apt-get install ghostscript


## (Optional) Create a virtual env

```sh
python3 -m venv my_virtualenv
source my_virtualenv/bin/activate
```

## Install with pip

```sh
pip install madpy
```

## Install [madgraph from its GitHub](https://github.com/mg5amcnlo/mg5amcnlo.git)

```
git clone https://github.com/mg5amcnlo/mg5amcnlo.git
cd mg5amcnlo
git switch 3.x

rm -rf bin/*.py
```


### Download MadGraph 2.9.24 (to run MadDM v3.2, to be updated soon)
```
wget https://github.com/mg5amcnlo/mg5amcnlo/archive/refs/tags/v2.9.24.tar.gz
tar -xvf v2.9.24.tar.gz
cd mg5amcnlo-2.9.24
```

Run mg5 with

```
./bin/mg5_aMC
```

## Install MadDM v3.2

In order to install [MadDM v3.2](https://maddmhep.github.io)

First, run MG5 with and then the following command 

```
./bin/mg5_aMC
install maddm
install pythia
```

!!! important "Python3 compatibility"
    Up to now, MadDM doesn't have compatibility with Python3, so you need to have Python2.7 installed.

And run maddm with:

```
python2.7 bin/maddm.py
```

After that, you can follow the [tutorial to learn MadDM basic features](https://maddmhep.github.io)

### Run Simplified DM model scan


```
MadDM> import model eDMsimp_s_spin0
MadDM> define darkmatter xd
MadDM> generate direct
MadDM> output SCAN_example
MadDM> launch SCAN_example
```



# TODO:

- [ ] Update this guide when MadDM v3.3 is released.


## [Experimental] Run MadDM beta with Python3 compatibility

Clone the [MadDM repository](https://github.com/maddmhep/maddm)

```
git clone https://github.com/maddmhep/maddm.git
cd maddm
git switch rc/3.3
cp -R . ../mg5amcnlo-2.9.24/PLUGIN/maddm
cp -R maddm ../mg5amcnlo-2.9.24/bin/maddm.py
```

## Install LHAPDF
```sh
wget https://lhapdf.hepforge.org/downloads/?f=LHAPDF-6.X.Y.tar.gz -O LHAPDF-6.X.Y.tar.gz
# ^ or use a web browser to download, which will get the filename correct
tar xf LHAPDF-6.X.Y.tar.gz
cd LHAPDF-6.X.Y
## Changes 
export PYTHON_VERSION=3.10
export PYTHON=/opt/apps/python/3.10/bin/python3.10
./configure  --prefix=/opt/apps/python/3.10
make
make install
```

## Troubleshooting

find /opt/apps/python/3.10 -name "libpython3.10.so.1.0"
export LD_LIBRARY_PATH=/opt/apps/python/3.10/lib:$LD_LIBRARY_PATH
echo "/opt/apps/python/3.10/lib" | sudo tee /etc/ld.so.conf.d/python310.conf
sudo ldconfig



file /opt/modulefiles/lhapdf/6.5.5
``` /opt/modulefiles/lhapdf/6.5.5
#%Module1.0
prepend-path PATH /opt/apps/lhapdf/bin
prepend-path LD_LIBRARY_PATH /opt/apps/lhapdf/lib
prepend-path PYTHONPATH /opt/apps/lhapdf/lib/python3.10/site-packages
```


# MadGraph FAQ

- https://answers.launchpad.net/mg5amcnlo/+faq/2735

- https://answers.launchpad.net/mg5amcnlo/+faq/2186