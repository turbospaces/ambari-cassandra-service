"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os

from resource_management.core.resources.packaging import Package

"""
	We'll use this function if we need to install any package before the 
	installation of Cassandra. It's not the case, but maybe in the future is useful.
	
	Old code
	
	if params.host_sys_prepped:
	return

	# This code come from:
	# https://github.com/apache/ambari/tree/trunk/ambari-server/src/main/resources/stacks/HDP/2.0.6/hooks/before-INSTALL/scripts
	# ambari/ambari-server/src/main/resources/stacks/HDP/2.0.6/hooks/before-INSTALL/scripts/
	
	packages = ['unzip', 'curl']
	Package(packages,
		retry_on_repo_unavailability=params.agent_stack_retry_on_unavailability,
		retry_count=params.agent_stack_retry_count)
"""
def install_packages():
    #import params
    return