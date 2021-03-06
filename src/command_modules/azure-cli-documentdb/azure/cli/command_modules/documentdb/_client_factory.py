# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def cf_documentdb(**_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azure.mgmt.documentdb import DocumentDB
    return get_mgmt_service_client(DocumentDB)
