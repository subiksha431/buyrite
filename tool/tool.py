from buyrite.utils.logging import Logger
import boto3
import botocore.exceptions 

logger = Logger.build_logger()

class CognitoUtils:

    def pool_creation(self, poolName):
        
        logger.info("Creating cognito pool[%s]", poolName)
        
        created_user_pool_Id = "tbd"
        created_client_Id = "tbd"
        create_user_pool_response = {}
        
        client = boto3.client("cognito-idp")
        
        try:
            
            response = client.create_user_pool(
                PoolName=poolName,
                Policies={
                    'PasswordPolicy': {
                        'MinimumLength': 8,
                        'RequireUppercase': True,
                        'RequireLowercase': True,
                        'RequireNumbers': True,
                        'RequireSymbols': True
                    }
                },
                AutoVerifiedAttributes=["email"],
                Schema=[{"Name": "email", "Required": True}],
            )
            
            created_user_pool_Id = response["UserPool"]["Id"]
           
            logger.info("Adding custom attributes [role] to pool-id[%s]",created_user_pool_Id)
            
            response = client.add_custom_attributes(
                UserPoolId=created_user_pool_Id,
                CustomAttributes=[
                    {"Name": "id", "AttributeDataType": "String"},
                    {"Name": "role", "AttributeDataType": "String"},
                    {"Name": "first_name", "AttributeDataType": "String"},
                    {"Name": "last_name", "AttributeDataType": "String"},
                    {"Name": "department", "AttributeDataType": "String"},
                    {"Name": "created_at", "AttributeDataType": "String"},
                    {"Name": "created_by", "AttributeDataType": "String"},
                    {"Name": "last_updated_by", "AttributeDataType": "String"},
                    {"Name": "last_updated_at", "AttributeDataType": "String"},
                ],
            )

            #logger.debug("Adding app client")
            
            # See here for options
            # https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool
            
            response = client.create_user_pool_client(
                UserPoolId=created_user_pool_Id,
                ClientName=poolName + "-client",
                ReadAttributes=["email","custom:role","custom:first_name","custom:last_name","custom:department","custom:id","custom:created_at","custom:created_by","custom:last_updated_by","custom:last_updated_at"],
                WriteAttributes=["email","custom:role","custom:first_name","custom:last_name","custom:department","custom:id","custom:created_at","custom:created_by","custom:last_updated_by","custom:last_updated_at"],
                ExplicitAuthFlows=["USER_PASSWORD_AUTH"],
                SupportedIdentityProviders=["COGNITO"]
            )
            
            created_client_Id = response["UserPoolClient"]["ClientId"]
            
            logger.debug("created cognito pool[%s] with id[%s] and client-id[%s]",
                poolName,
                created_user_pool_Id,
                created_client_Id,
            )

            create_user_pool_response["userPoolId"] = created_user_pool_Id
            create_user_pool_response["clientId"] = created_client_Id
            create_user_pool_response["userPoolName"] = poolName
            
            logger.info("Created cognito items[%s].", str(create_user_pool_response))

        except Exception as e:
            
            logger.error("failed creating user-pool [{%s}] with error[%s] ", poolName, e)
            
            if created_user_pool_Id != "tbd":
                client.delete_user_pool(UserPoolId=created_user_pool_Id)

            raise Exception("Failed creating user-pool [{}] with error[{}] ",poolName, str(e)
            )

        return create_user_pool_response


    def createUserLogin(self,poolId,clientId, user_id, password, id,role,first_name,last_name, department, created_at,created_by,last_updated_by,last_updated_at):
        userCreationResult = False
        logger.debug("Creating user[%s] with role[%s] on app-client[%s] with firstName[%s] ",
        user_id,role,clientId,first_name)

        client = boto3.client('cognito-idp')
        try:
            client.sign_up(
                ClientId = clientId,
                Username = user_id,
                Password = password,
                UserAttributes=[
                    {'Name': 'email', 'Value': user_id},
                    {'Name':'custom:id', 'Value': id},
                    {'Name':'custom:role', 'Value': role},
                    {'Name':'custom:department', 'Value': department},
                    {'Name':'custom:first_name', 'Value': first_name},
                    {'Name':'custom:last_name', 'Value': last_name},
                    {'Name':'custom:created_at', 'Value': created_at},
                    {'Name':'custom:created_by', 'Value': created_by},
                    {'Name':'custom:last_updated_by', 'Value': last_updated_by},
                    {'Name':'custom:last_updated_at', 'Value': last_updated_at}
                ]
                
            )
            logger.debug("User [%s] created, now trying to confirm it.",user_id)
            userCreationResult = True
        except client.exceptions.InvalidPasswordException as ipe:
            userCreationResult = 401
            #raise Exception("Passowrd is did not conform to the standards.")
        except client.exceptions.UsernameExistsException as uee:
            userCreationResult = 409
            #raise Exception("User[{}] already[{}] exists.".format(uee,userName))
        except Exception as exception:
            raise Exception("Unknown error[{}]while creating user[{}].".format(exception,user_id))

        return userCreationResult
