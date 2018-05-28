#!/usr/bin/env python
import os
import requests
import json
from config import USER, PASS, ENV_ID, CONFIG_ID, COL_ID
from watson_developer_cloud import DiscoveryV1
from pprint import pprint
import sys
if len(sys.argv) > 1:
    if sys.argv[1] == 'upload':
        mode = 'upload'
    elif sys.argv[1] == 'json':
        mode = 'json'
    else:
        mode = 'all'
else:
    mode = 'all'

#pprint(vars(DiscoveryV1))
discovery = DiscoveryV1(
    version='2018-03-05',
    username=USER,
    password=PASS,
    url='https://gateway.watsonplatform.net/discovery/api'
)

#parameters
parse = True
env_id = ENV_ID
config_id = CONFIG_ID
col_id = COL_ID

environments = discovery.list_environments()
#print(json.dumps(environments, indent=2))

#single file test
#with open(os.path.join(os.getcwd(), 'docs', 'test.html')) as fileinfo:
    #print(json.dumps(discovery.test_configuration_in_environment(environment_id=env_id, configuration_id=config_id, file=fileinfo), indent=2))

for fileName in os.listdir("docs/."):
    if fileName.endswith(".pdf") or fileName.endswith(".html"):
        try:
            with open('docs/'+fileName, 'rb') as file:
                try:
                    #with open('json%s.txt'%(fileName), 'w') as f:
                        #json.dump(discovery.test_configuration_in_environment(environment_id=env_id, configuration_id=config_id, file=file, step='enrichments_output'),f,ensure_ascii=True)
                    #upload docs
                    if mode == 'all' or mode == 'upload':
                        add_doc = json.dumps(discovery.add_document(environment_id=env_id, configuration_id=config_id, collection_id=col_id, file=file))
                        upload = json.loads(add_doc)
                        #print(upload)
                        document_id = upload['document_id']
                        document_status = upload['status']
                        print('Document ID: ', document_id, ' document status: ', document_status)
                    #result = json.dumps(discovery.test_configuration_in_environment(environment_id=env_id, configuration_id=config_id, file=file, step='enrich'), indent=2)
                    if mode == 'all' or mode == 'json':
                        query_docs = json.dumps(discovery.query(environment_id=env_id, configuration_id=config_id, collection_id=col_id))
                        query = json.loads(query_docs)
                        for doc in query['results']:
                            filename_api = doc['extracted_metadata']['filename']
                            #print("filename from api: ", filename_api)
                            if filename_api == fileName:
                                with open('json/json%s.json'%(fileName), 'w') as f:
                                    json.dump(doc, f, ensure_ascii=True)
                                    print('%s saved as json'%(fileName))
                            else:
                                pass
                    #with open('json%s.txt'%(fileName), 'w') as f:
                        #json.dump(, f, ensure_ascii=False)
                except Exception as e:
                    print(e.message)
                    print('Errored document name: ', fileName)
        except Exception as e:
            print(e.message)
            print('Unable to open document: ', fileName)
        #print(fileName)
    else:
        print('Not a PDF/html: ', fileName)
