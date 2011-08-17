import time

now = time.time()

defaulturi = {
    'submit' :  { 'uri': '/crabinterface/crab/task/',
                  'map':  {
                            "RequestType"       : {"default": "Analysis",       "config": None,                     "type": 'StringType',  "required": True },
                            "Group"             : {"default": "Analysis",       "config": 'User.group',             "type": 'StringType',  "required": True },
                            "Team"              : {"default": "Analysis",       "config": 'User.group',             "type": 'StringType',  "required": True },
                            "Requestor"         : {"default": None,             "config": None,                     "type": 'StringType',  "required": True },
                            "Username"          : {"default": None,             "config": None,                     "type": 'StringType',  "required": True },
                            "RequestName"       : {"default": None,             "config": None,                     "type": 'StringType',  "required": True },
                            "RequestorDN"       : {"default": None,             "config": None,                     "type": 'StringType',  "required": True },
                            "SaveLogs"          : {"default": False,            "config": 'General.saveLogs',       "type": 'BooleanType', "required": True },
                            "asyncDest"         : {"default": None,             "config": 'Site.storageSite',       "type": 'StringType',  "required": True },
                            "PublishDataName"   : {"default": str(int(now)),    "config": 'Data.publishDataName',   "type": 'StringType',  "required": True },
                            "ProcessingVersion" : {"default": "v1",             "config": 'Data.processingVersion', "type": 'StringType',  "required": True },
                            "DbsUrl"            : {"default": "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet", "config": 'Data.dbsUrl', "type": 'StringType',  "required": True },
                            "SiteWhitelist"     : {"default": None,             "config": 'Site.whitelist',         "type": 'ListType',    "required": False},
                            "SiteBlacklist"     : {"default": None,             "config": 'Site.blacklist',         "type": 'ListType',    "required": False},
                            "RunWhitelist"      : {"default": None,             "config": 'Data.runWhitelist',      "type": 'ListType',    "required": False},
                            "RunBlacklist"      : {"default": None,             "config": 'Data.runBlacklist',      "type": 'ListType',    "required": False},
                            "BlockWhitelist"    : {"default": None,             "config": 'Data.blockWhitelist',    "type": 'ListType',    "required": False},
                            "BlockBlacklist"    : {"default": None,             "config": 'Data.blockBlacklist',    "type": 'ListType',    "required": False},
                            "JobSplitAlgo"      : {"default": None,             "config": 'Data.splitting',         "type": 'StringType',  "required": False}
                            #"JobSplitArgs"      : {"default": None,             "config": 'Data.filesPerJob',       "type": IntType,    "required": False},
                            #"JobSplitArgs"      : {"default": None,             "config": 'Data.eventPerJob',       "type": IntType,    "required": False},
                          }
                },
    'get-log'     : {'uri': '/crabinterface/crab/log/'},
    'get-output'  : {'uri': '/crabinterface/crab/data/'},
    'reg_user'    : {'uri': '/crabinterface/crab/user/'},
    'server_info' : {'uri': '/crabinterface/crab/info/'},
    'status'      : {'uri': '/crabinterface/crab/task/'},
    'upload'      : {'uri': '/crabinterface/crab/uploadUserSandbox'},
    'report'      : {'uri': '/crabinterface/crab/goodLumis/'},
    'get_client_mapping': {'uri': '/crabinterface/crab/requestmapping'},
    'get-errors'  : {'uri': '/crabinterface/crab/jobErrors/'}
}
