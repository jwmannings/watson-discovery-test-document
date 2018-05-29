# Watson Discovery Document Test
## Overview
This is a simple script to upload and check documents against a Watson Discovery collection. This will check the documents, upload them, find them in the collection and then save the html/json output returned from the processing. This enables you to assess the document without having to use the online viewer.

Development note 28/5/18: viewer.py file added, this has been updated to work with this application. Full credit to [Ashwin Nanjappa]https://github.com/ashwin) for the original code.

Note: documents have been excluded in the demo besides from standard documents taken from freely avaliable resources (listed below).

## Set up environment
Firstly a file named 'config.py' will need to be created in the main file. This is important as it holds all of the parameters of the API.

'config.py' format:

      USER = '<username>'
      PASS = '<password>'
      ENV_ID = '<environment_id>'
      CONFIG_ID = '<configuration_id>'
      COL_ID = '<collection_id>'

The environment, configuration, and collection ID's are all taken from the Watson Discovery tooling.

### To set the local environment up:
Install [Anaconda](https://www.anaconda.com/download/#download) for your system.

Create the conda environment:
  conda create -n LLB python

Enter the environment:
'activate LLB'
 OR
'C:\Users\<username>\AppData\Local\Continuum\Anaconda3\Scripts\activate LLB'
note: where <username> is your local computer username.

## Needed environmental variables
Install the following within the anaconda virtual environment:
    conda install requests
    pip install --upgrade "watson-developer-cloud>=1.3.0"
    pip install jsonWidget
    pip install ipykernal
    pip install PyQt5

Note: PyQt5 is for the json viewer.


## Instructions for running
To run the script:
    python main.py        (runs both the upload and json transform)
    python main.py upload     (runs just the upload of documents)
    python main.py json     (runs just the json transform of documents)

It is recommended to run the 'upload' script first, wait until all documents are processed (check the visual Discovery tooling) and then run the 'json' script when complete.

To edit access details modify the 'config.py' file where the API keys and user access is stored.

To run the viewer (located in the json folder) run:
    python viewer.py <documentname>

To use the viewer, you can visually click through it all alternatively search for categories in the top bar.

## Constraints
- This script is only designed to ingest and upload PDF and HTML documents, all other documents in the target directory will be ignored.
- This script has error handling built in to pass errors and continue batch uploading even if uploads fail for any reason.
- Keep in mind the documents do take a moment to process, so you may have to run the script once, confirm the documents are uploaded on the visual tool and then run it again to save the json file (it won't save json until Watson has processed it).

### example document links
Document_1: [example](https://19of32x2yl33s8o4xza0gf14-wpengine.netdna-ssl.com/wp-content/uploads/Exhibit-A-SAMPLE-CONTRACT.pdf)
Document_2: [example](https://www.sdcwa.org/sites/default/files/files/business-opps/ProfessionalServiceContract.pdf)
Document_3: [example](https://www.myescambia.com/sites/myescambia.com/files/pages/2012/Oct/Uniform%20Contract%20Format/I_%20BRIDGES%20DOCKS%20AND%20BOAT%20RAMPS.pdf)
