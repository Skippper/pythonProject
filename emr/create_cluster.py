from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkemr.request.v20160408.CreateClusterV2Request import CreateClusterV2Request

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

request = CreateClusterV2Request()
request.set_accept_format('json')

request.set_Name("emr_openapi_demo")
request.set_ZoneId("cn-beijing")
request.set_EmrVer("EMR-3.23.0")
request.set_ClusterType("HADOOP")
request.set_HostGroups([
  {
    "HostGroupName": "master_group",
    "HostGroupType": "MASTER",
    "ChargeType": "PostPaid",
    "NodeCount": 2,
    "InstanceType": "ecs.g5.xlarge",
    "DiskType": "CLOUD_EFFICIENCY",
    "DiskCapacity": 80,
    "DiskCount": 1,
    "SysDiskType": "CLOUD_ESSD",
    "SysDiskCapacity": 120,
    "VSwitchId": "vsw-bp11t4amri1iuj*****"
  },
  {
    "HostGroupName": "core_group",
    "HostGroupType": "CORE",
    "ChargeType": "PostPaid",
    "NodeCount": 2,
    "InstanceType": "ecs.g5.2xlarge",
    "DiskType": "CLOUD_EFFICIENCY",
    "DiskCapacity": 80,
    "DiskCount": 4,
    "SysDiskType": "CLOUD_ESSD",
    "SysDiskCapacity": 120,
    "VSwitchId": "vsw-bp11t4amri1iuj*****"
  },
  {
    "HostGroupName": "task_group",
    "HostGroupType": "TASK",
    "ChargeType": "PostPaid",
    "NodeCount": 2,
    "InstanceType": "ecs.c5.xlarge",
    "DiskType": "CLOUD_EFFICIENCY",
    "DiskCapacity": 80,
    "DiskCount": 4,
    "SysDiskType": "CLOUD_ESSD",
    "SysDiskCapacity": 120,
    "VSwitchId": "vsw-bp11t4amri1iuj*****"
  }
])
request.set_SecurityGroupId("sg-bp13cqwumhn7x*****")
request.set_IsOpenPublicIp(True)
request.set_SecurityGroupName("newgroup")
request.set_ChargeType("PostPaid")
request.set_VpcId("vpc-bp1gjl3y9fezuk*****")
request.set_VSwitchId("vsw-bp11t4amri1iuj*****")
request.set_NetType("vpc")
request.set_UserDefinedEmrEcsRole("AliyunEmrEcsDefaultRole")
request.set_HighAvailabilityEnable(True)
request.set_IoOptimized(True)
request.set_SshEnable(True)
request.set_MasterPwd("EMRtest12345!")
request.set_DepositType("HALF_MANAGED")
request.set_MachineType("ECS")
request.set_Configs([
  {
    "ServiceName": "YARN",
    "FileName": "yarn-site",
    "ConfigKey": "yarn_nodemanager_heapsize",
    "ConfigValue": "1234"
  },
  {
    "ServiceName": "HIVE",
    "FileName": "hive-site",
    "ConfigKey": "hive.metastore.warehouse.dir",
    "ConfigValue": "/user/hive/warehouse_emr"
  }
])

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))