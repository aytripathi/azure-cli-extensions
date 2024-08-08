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
    "vmware workload-network dns-service update",
)
class Update(AAZCommand):
    """Update a DNS service by id in a private cloud workload network.

    :example: Update a DNS service by ID in a workload network.
        az vmware workload-network dns-service update --resource-group group1 --private-cloud cloud1 --dns-service dnsService1 --display-name dnsService1 --dns-service-ip 5.5.5.5 --default-dns-zone defaultDnsZone1 --fqdn-zones fqdnZone1 --log-level INFO --revision 1
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.avs/privateclouds/{}/workloadnetworks/default/dnsservices/{}", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.dns_service = AAZStrArg(
            options=["-n", "--name", "--dns-service"],
            help="NSX DNS Service identifier. Generally the same as the DNS Service's display name",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._]+$",
            ),
        )
        _args_schema.private_cloud = AAZStrArg(
            options=["-c", "--private-cloud"],
            help="Name of the private cloud",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._]+$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.default_dns_zone = AAZStrArg(
            options=["--default-dns-zone"],
            arg_group="Properties",
            help="Default DNS zone of the DNS Service.",
            nullable=True,
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Display name of the DNS Service.",
            nullable=True,
        )
        _args_schema.dns_service_ip = AAZStrArg(
            options=["--dns-service-ip"],
            arg_group="Properties",
            help="DNS service IP of the DNS Service.",
            nullable=True,
        )
        _args_schema.fqdn_zones = AAZListArg(
            options=["--fqdn-zones"],
            arg_group="Properties",
            help="FQDN zones of the DNS Service.",
            nullable=True,
        )
        _args_schema.log_level = AAZStrArg(
            options=["--log-level"],
            arg_group="Properties",
            help="DNS Service log level.",
            nullable=True,
            enum={"DEBUG": "DEBUG", "ERROR": "ERROR", "FATAL": "FATAL", "INFO": "INFO", "WARNING": "WARNING"},
        )
        _args_schema.revision = AAZIntArg(
            options=["--revision"],
            arg_group="Properties",
            help="NSX revision number.",
            nullable=True,
        )

        fqdn_zones = cls._args_schema.fqdn_zones
        fqdn_zones.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.WorkloadNetworksGetDnsService(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.WorkloadNetworksCreateDnsService(ctx=self.ctx)()
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

    class WorkloadNetworksGetDnsService(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/workloadNetworks/default/dnsServices/{dnsServiceId}",
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
                    "dnsServiceId", self.ctx.args.dns_service,
                    required=True,
                ),
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud,
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
            _UpdateHelper._build_schema_workload_network_dns_service_read(cls._schema_on_200)

            return cls._schema_on_200

    class WorkloadNetworksCreateDnsService(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}/workloadNetworks/default/dnsServices/{dnsServiceId}",
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
                    "dnsServiceId", self.ctx.args.dns_service,
                    required=True,
                ),
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud,
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
            _UpdateHelper._build_schema_workload_network_dns_service_read(cls._schema_on_200_201)

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
                properties.set_prop("defaultDnsZone", AAZStrType, ".default_dns_zone")
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("dnsServiceIp", AAZStrType, ".dns_service_ip")
                properties.set_prop("fqdnZones", AAZListType, ".fqdn_zones")
                properties.set_prop("logLevel", AAZStrType, ".log_level")
                properties.set_prop("revision", AAZIntType, ".revision")

            fqdn_zones = _builder.get(".properties.fqdnZones")
            if fqdn_zones is not None:
                fqdn_zones.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_workload_network_dns_service_read = None

    @classmethod
    def _build_schema_workload_network_dns_service_read(cls, _schema):
        if cls._schema_workload_network_dns_service_read is not None:
            _schema.id = cls._schema_workload_network_dns_service_read.id
            _schema.name = cls._schema_workload_network_dns_service_read.name
            _schema.properties = cls._schema_workload_network_dns_service_read.properties
            _schema.system_data = cls._schema_workload_network_dns_service_read.system_data
            _schema.type = cls._schema_workload_network_dns_service_read.type
            return

        cls._schema_workload_network_dns_service_read = _schema_workload_network_dns_service_read = AAZObjectType()

        workload_network_dns_service_read = _schema_workload_network_dns_service_read
        workload_network_dns_service_read.id = AAZStrType(
            flags={"read_only": True},
        )
        workload_network_dns_service_read.name = AAZStrType(
            flags={"read_only": True},
        )
        workload_network_dns_service_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        workload_network_dns_service_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        workload_network_dns_service_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_workload_network_dns_service_read.properties
        properties.default_dns_zone = AAZStrType(
            serialized_name="defaultDnsZone",
        )
        properties.display_name = AAZStrType(
            serialized_name="displayName",
        )
        properties.dns_service_ip = AAZStrType(
            serialized_name="dnsServiceIp",
        )
        properties.fqdn_zones = AAZListType(
            serialized_name="fqdnZones",
        )
        properties.log_level = AAZStrType(
            serialized_name="logLevel",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.revision = AAZIntType()
        properties.status = AAZStrType()

        fqdn_zones = _schema_workload_network_dns_service_read.properties.fqdn_zones
        fqdn_zones.Element = AAZStrType()

        system_data = _schema_workload_network_dns_service_read.system_data
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

        _schema.id = cls._schema_workload_network_dns_service_read.id
        _schema.name = cls._schema_workload_network_dns_service_read.name
        _schema.properties = cls._schema_workload_network_dns_service_read.properties
        _schema.system_data = cls._schema_workload_network_dns_service_read.system_data
        _schema.type = cls._schema_workload_network_dns_service_read.type


__all__ = ["Update"]
