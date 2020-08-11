# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class CheckPermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Oam', '2017-01-01', 'CheckPermission')
		self.set_method('POST')

	def get_Resource(self):
		return self.get_query_params().get('Resource')

	def set_Resource(self,Resource):
		self.add_query_param('Resource',Resource)

	def get_ActionField(self):
		return self.get_query_params().get('ActionField')

	def set_ActionField(self,ActionField):
		self.add_query_param('ActionField',ActionField)

	def get_AliUid(self):
		return self.get_query_params().get('AliUid')

	def set_AliUid(self,AliUid):
		self.add_query_param('AliUid',AliUid)