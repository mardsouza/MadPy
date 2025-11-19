from dataclasses import dataclass
import pandas as pd 

import tarfile
import os
import subprocess
from subprocess import Popen, PIPE, CalledProcessError
from pathlib import Path
import sys

MADGRAPH_PATH = f"../mg5amcnlo"
sys.path.append(MADGRAPH_PATH)

MG5_LATEST = '3.6.3'



# def get_mg5(version: str = MG5_LATEST, output_dir: str | None =  None):
#     '''Get the latest version of MG5 and saves it to the disk'''
    
#     if output_dir is None:
#         output_dir = os.getcwd()

#     file_name = f'MG5_aMC_v{version}.tar.gz'
#     mg5_url = f"http://launchpad.net/madgraph5/3.0/3.6.x/+download/{file_name}"

#     # wget.download(mg5_url, out = output_dir)
#     print(f'Downloaded at {output_dir}/{file_name}')


def untar_file(file: str, output_dir: str | None =  None):

    '''Alias to untar some tar.gz file to a output_dir folder'''

    if output_dir is None:
        output_dir = os.getcwd()

    subprocess.run(
        ["tar", "-xzfv", file, "-C", output_dir],
        check=True
    )

    print('All done!')
    

def madpy_generate_script(process: str = "p p > t t~ j",
                          model: str = "sm",
                          masses: dict | None = None,
                          coupling: dict | None = None,
                          decays: dict | None = None,
                          pt_cut: dict | None = None,
                          madspin: bool = True,
                          number_events: int = 1000,
                          process_name: str = "new_process",
                          workdir_path: str = "../workdir",
                          coupled_scan: bool = True,
                          draw_diagrams: bool = True):
    
    workdir_process = f"{workdir_path}/{process_name}"
    Path(f"{workdir_process}/diagrams").mkdir(parents=True, exist_ok=True)

    ## First part of  the script
    mg5_script = f"""\
import model sm
import model {model}
generate {process}
output {workdir_process} -f
display diagrams {workdir_process}/diagrams
launch {workdir_process}"""
    
    if masses:
        for particle, mass in masses.items():
            mg5_script += "\n\t" + f"""set mass {particle} {mass}"""
            
    if coupling:
        for coup, value in coupling.items():
            mg5_script += "\n\t" + f"""set DMINPUTS {coup} {value}"""
    
    if decays:
        for decay, value in decays.items():
            mg5_script += "\n\t" + f"""set width {decay} {value}"""
    
    if pt_cut:
        for pt, cut in pt_cut.items():
            mg5_script += "\n\t" + f"""set {pt} {cut}"""
    
    # if madspin:
    #     mg5_script += "\n\t" + f"""madspin=ON"""
    
    # else:
    #     mg5_script += "\n\t" + f"""madspin=OFF"""
        
    # Set number of events
    
    # Set Energy Beam

    # mg5_script += "\n\t" + f"""set run_card bwcutoff = 150"""
    # mg5_script += "\n\t" + f"""set run_card ebeam1 = 1500"""
    # mg5_script += "\n\t" + f"""set run_card ebeam2 = 1500"""
    # mg5_script += "\n\t" + f"""set run_card lpp1 = 0"""
    # mg5_script += "\n\t" + f"""set run_card lpp2 = 0"""
    # mg5_script += "\n\t" + f"""set nevents {number_events}"""
    # mg5_script += "\n\t" + f"""set run_card pdfset = NNPDF31_lo_as_0118"""
    #mg5_script += "\n\t" + f"""set run_card pta = 60"""      # minimum pt for the photons 
    #mg5_script += "\n\t" + f"""set run_card ptamax = 1000"""   # maximum pt for the photons 
    # set scale

    # if madspin:
    #     mg5_script += "\n\t" + f"""madspin=ON"""
    
    # else:
    #     mg5_script += "\n\t" + f"""madspin=OFF"""
    
    
    with open(process_name + ".mg5", "w") as script_file:
        # Write the string into the .mg5 file
        script_file.write(mg5_script)
        
    return mg5_script, process_name


def madpy_run(process_name: str, mg5_script_folder_path: str, mg5_bin: str = "mg5_aMC", madgraph_path = MADGRAPH_PATH):
    '''This will call MG5 and run the created script'''
    
    mg5_executable = f"{madgraph_path}/bin/{mg5_bin}"
    mg5_script_complete_path = mg5_script_folder_path + "/" + process_name + ".mg5"
    
    with open(f"{process_name}.log", "w") as script_log_file:
        subprocess.run([mg5_executable, mg5_script_complete_path], stdout=script_log_file)



# Convert EPS to PDF using ghostscript
def convert_eps_to_pdf(eps_file, pdf_file=None):
    """
    Convert an EPS file to PDF using ghostscript.
    
    Args:
        eps_file (str): Path to the input EPS file
        pdf_file (str): Path to the output PDF file (optional)
                       If not provided, uses same name as eps_file with .pdf extension
    """
    if pdf_file is None:
        pdf_file = Path(eps_file).stem + '.pdf'
    
    # Ghostscript command for EPS to PDF conversion
    cmd = [
        'gs',
        '-q',                          # Quiet mode
        '-dNOPAUSE',                  # Don't pause after each page
        '-dBATCH',                    # Batch mode (exit after processing)
        '-dSAFER',                    # Safer mode
        '-sDEVICE=pdfwrite',          # Output device
        f'-sOutputFile={pdf_file}',   # Output file
        '-dEPSCrop',                  # Crop to EPS bounding box
        eps_file                      # Input file
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"Successfully converted {eps_file} to {pdf_file}")
        return pdf_file
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e.stderr.decode()}")
        return None
    except FileNotFoundError:
        print("Ghostscript not found. Please install it:")
        print("  Ubuntu/Debian: sudo apt-get install ghostscript")
        print("  macOS: brew install ghostscript")
        print("  Windows: Download from https://www.ghostscript.com/download/gsdnld.html")
        return None
