# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "storage-mover job-run list",
)
class List(AAZCommand):
    """Lists all Job Runs in a Job Definition.

    :example: job-run list
        az storage-mover job-run list -g {rg} --job-definition-name {job_definition} --project-name {project_name} --storage-mover-name {mover_name}
    """

    _aaz_info = {
        "version": "2024-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.storagemover/storagemovers/{}/projects/{}/jobdefinitions/{}/jobruns", "2024-07-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.job_definition_name = AAZStrArg(
            options=["--job-definition-name"],
            help="The name of the Job Definition resource.",
            required=True,
        )
        _args_schema.project_name = AAZStrArg(
            options=["--project-name"],
            help="The name of the Project resource.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.storage_mover_name = AAZStrArg(
            options=["--storage-mover-name"],
            help="The name of the Storage Mover resource.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.JobRunsList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class JobRunsList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageMover/storageMovers/{storageMoverName}/projects/{projectName}/jobDefinitions/{jobDefinitionName}/jobRuns",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "jobDefinitionName", self.ctx.args.job_definition_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "projectName", self.ctx.args.project_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "storageMoverName", self.ctx.args.storage_mover_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.agent_name = AAZStrType(
                serialized_name="agentName",
                flags={"read_only": True},
            )
            properties.agent_resource_id = AAZStrType(
                serialized_name="agentResourceId",
                flags={"read_only": True},
            )
            properties.bytes_excluded = AAZIntType(
                serialized_name="bytesExcluded",
                flags={"read_only": True},
            )
            properties.bytes_failed = AAZIntType(
                serialized_name="bytesFailed",
                flags={"read_only": True},
            )
            properties.bytes_no_transfer_needed = AAZIntType(
                serialized_name="bytesNoTransferNeeded",
                flags={"read_only": True},
            )
            properties.bytes_scanned = AAZIntType(
                serialized_name="bytesScanned",
                flags={"read_only": True},
            )
            properties.bytes_transferred = AAZIntType(
                serialized_name="bytesTransferred",
                flags={"read_only": True},
            )
            properties.bytes_unsupported = AAZIntType(
                serialized_name="bytesUnsupported",
                flags={"read_only": True},
            )
            properties.error = AAZObjectType(
                flags={"read_only": True},
            )
            properties.execution_end_time = AAZStrType(
                serialized_name="executionEndTime",
                flags={"read_only": True},
            )
            properties.execution_start_time = AAZStrType(
                serialized_name="executionStartTime",
                flags={"read_only": True},
            )
            properties.items_excluded = AAZIntType(
                serialized_name="itemsExcluded",
                flags={"read_only": True},
            )
            properties.items_failed = AAZIntType(
                serialized_name="itemsFailed",
                flags={"read_only": True},
            )
            properties.items_no_transfer_needed = AAZIntType(
                serialized_name="itemsNoTransferNeeded",
                flags={"read_only": True},
            )
            properties.items_scanned = AAZIntType(
                serialized_name="itemsScanned",
                flags={"read_only": True},
            )
            properties.items_transferred = AAZIntType(
                serialized_name="itemsTransferred",
                flags={"read_only": True},
            )
            properties.items_unsupported = AAZIntType(
                serialized_name="itemsUnsupported",
                flags={"read_only": True},
            )
            properties.job_definition_properties = AAZObjectType(
                serialized_name="jobDefinitionProperties",
                flags={"read_only": True},
            )
            properties.last_status_update = AAZStrType(
                serialized_name="lastStatusUpdate",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.scan_status = AAZStrType(
                serialized_name="scanStatus",
                flags={"read_only": True},
            )
            properties.source_name = AAZStrType(
                serialized_name="sourceName",
                flags={"read_only": True},
            )
            properties.source_properties = AAZObjectType(
                serialized_name="sourceProperties",
                flags={"read_only": True},
            )
            properties.source_resource_id = AAZStrType(
                serialized_name="sourceResourceId",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.target_name = AAZStrType(
                serialized_name="targetName",
                flags={"read_only": True},
            )
            properties.target_properties = AAZObjectType(
                serialized_name="targetProperties",
                flags={"read_only": True},
            )
            properties.target_resource_id = AAZStrType(
                serialized_name="targetResourceId",
                flags={"read_only": True},
            )

            error = cls._schema_on_200.value.Element.properties.error
            error.code = AAZStrType()
            error.message = AAZStrType()
            error.target = AAZStrType()

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
