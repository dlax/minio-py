# -*- coding: utf-8 -*-
# MinIO Python Library for Amazon S3 Compatible Cloud Storage, (C) 2020 MinIO, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# IamEc2MetaData will call AWS metadata service to retrieve credentials
#
# The default AWS metadata service can be found at:
#   -> 169.254.169.254/latest/meta-data/iam/security-credentials
#
# If you wish to retieve credentials from a different place you can provide 
# the 'endpoint' paramater to the IamEc2MetaData credentials object

from minio.credentials import IamEc2MetaData

# Initialize Minio with IamEc2MetaData default credentials object
client = Minio('s3.amazonaws.com', 
               credentials=IamEc2MetaData())

# Initialize Minio with IamEc2MetaData custom 

client = Minio('s3.amazonaws.com', 
               credentials=IamEc2MetaData(endpoint='custom.endpoint'))