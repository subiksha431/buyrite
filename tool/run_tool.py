#######################F<FOR_LOCAL_RUNS_ONLY>######################################
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
#######################F</FOR_LOCAL_RUNS_ONLY>######################################

from buyrite.utils.logging import Logger
from tool import  CognitoUtils
from buyrite.utils import datautils


cognitoUtils = CognitoUtils()
logger = Logger.build_logger()

def pool_creation():
    poolName = "buyrite-user-pool"
    logger.info("Passing pool-name[%s] to be created.",poolName)
    cognitoUtils.pool_creation(poolName)
    # Created cognito items[{'userPoolId': 'us-east-2_kyScV4Qkh', 'clientId': '7j3kc4gta69e24ggshprjceeh9', 'userPoolName': 'dev-buyrite-user-pool'}]

def test_user_creation():

    #qa
    poolId = "us-east-2_hafNP761R"
    appClientID = "7bspd3i604qa4aiklja7qobiii"

    date = str(datautils.get_date())
    guid = datautils.new_guid()
    
    user_id = "vignesh@buyrite.com"
    password = "Password@123"
    role = "admin"
    first_name ="vignesh"
    last_name = "kootaiveetu"
    department = "IT"
    created_at = date
    created_by = "vignesh@corpworx.com"
    last_updated_by = "vignesh@corpworx.com"
    last_updated_at = date
    id = guid
    cognitoUtils.createUserLogin(poolId,appClientID,user_id, password, id,role,first_name,last_name, department, created_at,created_by,last_updated_by,last_updated_at)

if __name__ == "__main__":
    test_user_creation()