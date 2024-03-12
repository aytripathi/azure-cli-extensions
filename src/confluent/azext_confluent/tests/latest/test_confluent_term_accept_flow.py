# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from unittest import mock
import time

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from azure.cli.testsdk.scenario_tests import AllowLargeResponse

from .test_confluent_scenario import mock_jwt_decode, mock_list_role_assignments


class TestTermAcceptFlow(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_term_accept_basic_flow', location='eastus2euap')
    @AllowLargeResponse()
    def test_term_accept_basic_flow(self, resource_group):

        self.kwargs.update({
            'rg': resource_group,
            'offerId': 'confluent-cloud-azure-stag',
            'planId': 'confluent-cloud-azure-payg-stag',
            'publisherId': 'confluentinc',
            'namespace': 'Microsoft.Confluent',
            'organizationName': 'cliTestOrg-1'
        })

        self.cmd('az confluent offer-detail show '
                 '--publisher-id {publisherId} '
                 '--offer-id {offerId}')

        self.cmd('az term accept '
                 '--product "{offerId}" '
                 '--plan "{planId}" '
                 '--publisher "{publisherId}"')

        self.cmd('provider register -n {namespace} ')
        result = self.cmd('provider show -n {namespace}').get_output_in_json()
        while result['registrationState'] != 'Registered':
            time.sleep(5)
            result = self.cmd('provider show -n {namespace}').get_output_in_json()

        with mock.patch('jwt.decode', mock_jwt_decode):
            with mock.patch('azure.cli.command_modules.role.custom.list_role_assignments', mock_list_role_assignments):
                self.cmd('az confluent organization create '
                         '--location "eastus2euap" '
                         '--offer-id "{offerId}" '
                         '--plan-id "{planId}" '
                         '--plan-name "Confluent Cloud - Pay as you Go" '
                         '--publisher-id "{publisherId}" '
                         '--term-unit "P1M" '
                         '--tags environment="Dev" '
                         '--name "{organizationName}" '
                         '--resource-group "{rg}"')
