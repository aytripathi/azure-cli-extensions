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
    "communication email domain sender-username update",
)
class Update(AAZCommand):
    """Update a new SenderUsername resource under the parent Domains resource or update an existing SenderUsername resource.

    :example: Update a sender username with display name
        az communication email domain sender-username update --domain-name DomainName --email-service-name ResourceName -g ResourceGroup --sender-username SenderUsername --display-name DisplayName
    """

    _aaz_info = {
        "version": "2023-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.communication/emailservices/{}/domains/{}/senderusernames/{}", "2023-04-01-preview"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.domain_name = AAZStrArg(
            options=["--domain-name"],
            help="The name of the Domains resource.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                max_length=253,
                min_length=1,
            ),
        )
        _args_schema.email_service_name = AAZStrArg(
            options=["--email-service-name"],
            help="The name of the EmailService resource.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]+$",
                max_length=63,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.sender_username = AAZStrArg(
            options=["-n", "--name", "--sender-username"],
            help="The valid sender Username.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                max_length=253,
                min_length=1,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="The display name for the senderUsername.",
            nullable=True,
        )
        _args_schema.username = AAZStrArg(
            options=["--username"],
            arg_group="Properties",
            help="A sender senderUsername to be used when sending emails.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SenderUsernamesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.SenderUsernamesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SenderUsernamesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Communication/emailServices/{emailServiceName}/domains/{domainName}/senderUsernames/{senderUsername}",
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
                    "domainName", self.ctx.args.domain_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "emailServiceName", self.ctx.args.email_service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "senderUsername", self.ctx.args.sender_username,
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
                    "api-version", "2023-04-01-preview",
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
            _UpdateHelper._build_schema_sender_username_resource_read(cls._schema_on_200)

            return cls._schema_on_200

    class SenderUsernamesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Communication/emailServices/{emailServiceName}/domains/{domainName}/senderUsernames/{senderUsername}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "domainName", self.ctx.args.domain_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "emailServiceName", self.ctx.args.email_service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "senderUsername", self.ctx.args.sender_username,
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
                    "api-version", "2023-04-01-preview",
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
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_sender_username_resource_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("username", AAZStrType, ".username", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_sender_username_resource_read = None

    @classmethod
    def _build_schema_sender_username_resource_read(cls, _schema):
        if cls._schema_sender_username_resource_read is not None:
            _schema.id = cls._schema_sender_username_resource_read.id
            _schema.name = cls._schema_sender_username_resource_read.name
            _schema.properties = cls._schema_sender_username_resource_read.properties
            _schema.system_data = cls._schema_sender_username_resource_read.system_data
            _schema.type = cls._schema_sender_username_resource_read.type
            return

        cls._schema_sender_username_resource_read = _schema_sender_username_resource_read = AAZObjectType()

        sender_username_resource_read = _schema_sender_username_resource_read
        sender_username_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )
        sender_username_resource_read.name = AAZStrType(
            flags={"read_only": True},
        )
        sender_username_resource_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        sender_username_resource_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        sender_username_resource_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_sender_username_resource_read.properties
        properties.data_location = AAZStrType(
            serialized_name="dataLocation",
            flags={"read_only": True},
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.username = AAZStrType(
            flags={"required": True},
        )

        system_data = _schema_sender_username_resource_read.system_data
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

        _schema.id = cls._schema_sender_username_resource_read.id
        _schema.name = cls._schema_sender_username_resource_read.name
        _schema.properties = cls._schema_sender_username_resource_read.properties
        _schema.system_data = cls._schema_sender_username_resource_read.system_data
        _schema.type = cls._schema_sender_username_resource_read.type


__all__ = ["Update"]
