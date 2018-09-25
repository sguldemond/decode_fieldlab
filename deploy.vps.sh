#!/bin/bash
git add .
git commit -m "development"
git push origin development

# scp -r server ssh decodeams@oscity.nl:~/decode_docker/decode_fieldlab/server
# scp -r server ubuntu@185.54.115.75:~/
