from dataclasses import dataclass
import pandas as pd 
import wget
import tarfile
import os
import subprocess


MG5_LATEST = '3.6.3'


SM_particle_data_dict = {
    "PID": [11, -11, 13, -13, 22, 12, -12, 14, -14, 16, -16, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 21, 23, 24, -24],
    "Name": [
        "Electron", "Positron", "Muon", "Anti-Muon", "Photon",
        "Electron Neutrino", "Electron Anti-Neutrino", "Muon Neutrino", "Muon Anti-Neutrino",
        "Tau Neutrino", "Tau Anti-Neutrino", "Down Quark", "Anti-Down Quark",
        "Up Quark", "Anti-Up Quark", "Strange Quark", "Anti-Strange Quark",
        "Charm Quark", "Anti-Charm Quark", "Bottom Quark", "Anti-Bottom Quark",
        "Gluon", "Z Boson", "W+ Boson", "W- Boson"
    ],
    "Symbol": [
        "e-", "e+", "mu-", "mu+", "a",
        "ve", "ve~", "vm", "vm~",
        "vt", "vt~", "d", "d~",
        "u", "u~", "s", "s~",
        "c", "c~", "b", "b~",
        "g", "z", "w+", "w-"
    ]
}

# Simple Dataframe with SM particle data
SM_PARTICLE_DataFrame = pd.DataFrame(SM_particle_data_dict)


def get_mg5(version: str = MG5_LATEST, output_dir: str | None =  None):
    '''Get the latest version of MG5 and saves it to the disk'''
    
    if output_dir is None:
        output_dir = os.getcwd()

    file_name = f'MG5_aMC_v{version}.tar.gz'
    mg5_url = f"http://launchpad.net/madgraph5/3.0/3.6.x/+download/{file_name}"

    wget.download(mg5_url, out = output_dir)
    print(f'Downloaded at {output_dir}/{file_name}')


def untar_file(file: str, output_dir: str | None =  None):

    '''Alias to untar some tar.gz file to a output_dir folder'''

    if output_dir is None:
        output_dir = os.getcwd()

    subprocess.run(
        ["tar", "-xzfv", file, "-C", output_dir],
        check=True
    )

    print('All done!')