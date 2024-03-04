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
    "networkfabric device run-ro",
)
class RunRo(AAZCommand):
    """Run the RO Command on the Network Device.
    """

    _aaz_info = {
        "version": "2024-02-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networkdevices/{}/runrocommand", "2024-02-15-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the Network Device.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.ro_command = AAZStrArg(
            options=["--ro-command"],
            arg_group="Body",
            help="Specify the command.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.NetworkDevicesRunRoCommand(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetworkDevicesRunRoCommand(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkDevices/{networkDeviceName}/runRoCommand",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkDeviceName", self.ctx.args.resource_name,
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
                    "api-version", "2024-02-15-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("command", AAZStrType, ".ro_command")

            return self.serialize_content(_content_value)

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
            _schema_on_200.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            _schema_on_200.error = AAZObjectType()
            _RunRoHelper._build_schema_error_detail_read(_schema_on_200.error)
            _schema_on_200.output_url = AAZStrType(
                serialized_name="outputUrl",
            )

            return cls._schema_on_200


class _RunRoHelper:
    """Helper class for RunRo"""

    _schema_error_detail_read = None

    @classmethod
    def _build_schema_error_detail_read(cls, _schema):
        if cls._schema_error_detail_read is not None:
            _schema.additional_info = cls._schema_error_detail_read.additional_info
            _schema.code = cls._schema_error_detail_read.code
            _schema.details = cls._schema_error_detail_read.details
            _schema.message = cls._schema_error_detail_read.message
            _schema.target = cls._schema_error_detail_read.target
            return

        cls._schema_error_detail_read = _schema_error_detail_read = AAZObjectType()

        error_detail_read = _schema_error_detail_read
        error_detail_read.additional_info = AAZListType(
            serialized_name="additionalInfo",
            flags={"read_only": True},
        )
        error_detail_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_detail_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.target = AAZStrType(
            flags={"read_only": True},
        )

        additional_info = _schema_error_detail_read.additional_info
        additional_info.Element = AAZObjectType()

        _element = _schema_error_detail_read.additional_info.Element
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_detail_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_detail_read(details.Element)

        _schema.additional_info = cls._schema_error_detail_read.additional_info
        _schema.code = cls._schema_error_detail_read.code
        _schema.details = cls._schema_error_detail_read.details
        _schema.message = cls._schema_error_detail_read.message
        _schema.target = cls._schema_error_detail_read.target


__all__ = ["RunRo"]
