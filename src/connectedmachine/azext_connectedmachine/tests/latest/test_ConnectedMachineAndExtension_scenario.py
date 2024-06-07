# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_extension_create
from .example_steps import step_extension_list
from .example_steps import step_extension_show
from .example_steps import step_extension_update
from .example_steps import step_upgrade_extension
from .example_steps import step_extension_delete
from .example_steps import step_delete
from .. import (
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))

class ConnectedMachineAndExtensionScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_machineextension')
    def test_machine_and_extension(self):
        self.kwargs.update({
            'machine': 'testmachine',
            'rg': 'ytongtest',
            'location': 'centraluseuap',
            'customScriptName': 'custom-test',
        })

        self.cmd('az connectedmachine show -n {machine} -g {rg}', checks=[
            self.check('name', '{machine}'),
            self.check('resourceGroup', '{rg}')
        ])

        self.cmd('az connectedmachine list -g {rg}', checks=[
            self.check('length(@)', 1)
        ])

        self.cmd('az connectedmachine extension create '
                '--name "{customScriptName}" '
                '--location "{location}" '
                '--type "CustomScriptExtension" '
                '--publisher "Microsoft.Compute" '
                '--type-handler-version "1.10.10" '
                '--machine-name "{machine}" '
                '--resource-group "{rg}" '
                '--settings "{{\\"commandToExecute\\":\\"powershell.exe ls\\"}}"',
                checks=[
                    self.check('name', '{customScriptName}'),
                    self.check('properties.enableAutomaticUpgrade', True),
                    self.check('properties.typeHandlerVersion', '1.10.10'),
        ])

        self.cmd('az connectedmachine install-patches '
                '--resource-group "{rg}" '
                '--name "{machine}" '
                '--maximum-duration "PT4H" '
                '--reboot-setting "IfRequired" '
                '--windows-parameters "{{\\"classificationsToInclude\\":[\\"Critical\\", \\"Security\\"]}}"',
                checks=[
                    self.check('status', 'Succeeded')
        ])

        self.cmd('az connectedmachine assess-patches '
                '--resource-group "{rg}" '
                '--name "{machine}"',
                checks=[
                    self.check('status', 'Succeeded')
        ])

        self.cmd('az connectedmachine extension list '
                '--machine-name {machine} -g {rg}', 
                checks=[
                    # self.check('length(@)', 1)
        ])

        self.cmd('az connectedmachine extension show '
                '--name {customScriptName} '
                '--machine-name "{machine}" '
                '--resource-group "{rg}"',
                checks=[
                    self.check('name', '{customScriptName}'),
                    self.check('properties.typeHandlerVersion', '1.10.10')
        ])

        self.cmd('az connectedmachine extension image show '
                '--publisher "Microsoft.Compute" '
                '--extension-type "CustomScriptExtension" '
                '--location "{location}" '
                '--version "1.10.10"',
                checks=[
                    self.check('version', '1.10.10'),
                    self.check('publisher', 'microsoft.compute'),
                    self.check('extensionType', 'customscriptextension')
        ])

        self.cmd('az connectedmachine extension image list '
                '--publisher "Microsoft.Compute" '
                '--extension-type "CustomScriptExtension" '
                '--location "{location}"',
                checks=[
        ])

        self.cmd('az connectedmachine upgrade-extension '
                '--extension-targets "{{\\"Microsoft.Compute.CustomScriptExtension\\":{{\\"targetVersion\\":\\"1.10.12\\"}}}}" '
                '--machine-name "{machine}" '
                '--resource-group "{rg}"',
                checks=[])

        self.cmd('az connectedmachine extension update '
                '--name "{customScriptName}" '
                '--enable-automatic-upgrade false '
                '--settings "{{\\"commandToExecute\\":\\"dir\\"}}" '
                '--machine-name "{machine}" '
                '--resource-group "{rg}"',
                checks=[
                    self.check('name', '{customScriptName}'),
                    self.check('properties.enableAutomaticUpgrade', False),
                    self.check('properties.provisioningState', 'Succeeded'),
                    self.check('properties.settings.commandToExecute', 'dir'),
                    self.check('properties.typeHandlerVersion', '1.10.12')
        ]) 

        self.cmd('az connectedmachine extension delete -y '
                '--name "{customScriptName}" '
                '--machine-name "{machine}" '
                '--resource-group "{rg}"',
                checks=[])

        self.cmd('az connectedmachine delete -y '
                '--name "{machine}" '
                '--resource-group "{rg}"',
                checks=[])
