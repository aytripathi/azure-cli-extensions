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
    "nginx deployment configuration wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/nginx.nginxplus/nginxdeployments/{}/configurations/{}", "2023-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.configuration_name = AAZStrArg(
            options=["-n", "--name", "--configuration-name"],
            help="The name of configuration, only 'default' is supported value due to the singleton of Nginx conf",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.deployment_name = AAZStrArg(
            options=["--deployment-name"],
            help="The name of targeted Nginx deployment",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-z0-9A-Z][a-z0-9A-Z-]{0,28}[a-z0-9A-Z]|[a-z0-9A-Z])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ConfigurationsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class ConfigurationsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/configurations/{configurationName}",
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
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2023-09-01",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.files = AAZListType()
            properties.package = AAZObjectType()
            properties.protected_files = AAZListType(
                serialized_name="protectedFiles",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.root_file = AAZStrType(
                serialized_name="rootFile",
            )

            files = cls._schema_on_200.properties.files
            files.Element = AAZObjectType()
            _WaitHelper._build_schema_nginx_configuration_file_read(files.Element)

            package = cls._schema_on_200.properties.package
            package.data = AAZStrType()
            package.protected_files = AAZListType(
                serialized_name="protectedFiles",
            )

            protected_files = cls._schema_on_200.properties.package.protected_files
            protected_files.Element = AAZStrType()

            protected_files = cls._schema_on_200.properties.protected_files
            protected_files.Element = AAZObjectType()
            _WaitHelper._build_schema_nginx_configuration_file_read(protected_files.Element)

            system_data = cls._schema_on_200.system_data
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


class _WaitHelper:
    """Helper class for Wait"""

    _schema_nginx_configuration_file_read = None

    @classmethod
    def _build_schema_nginx_configuration_file_read(cls, _schema):
        if cls._schema_nginx_configuration_file_read is not None:
            _schema.content = cls._schema_nginx_configuration_file_read.content
            _schema.virtual_path = cls._schema_nginx_configuration_file_read.virtual_path
            return

        cls._schema_nginx_configuration_file_read = _schema_nginx_configuration_file_read = AAZObjectType()

        nginx_configuration_file_read = _schema_nginx_configuration_file_read
        nginx_configuration_file_read.content = AAZStrType()
        nginx_configuration_file_read.virtual_path = AAZStrType(
            serialized_name="virtualPath",
        )

        _schema.content = cls._schema_nginx_configuration_file_read.content
        _schema.virtual_path = cls._schema_nginx_configuration_file_read.virtual_path


__all__ = ["Wait"]
