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
    "networkfabric externalnetwork create",
)
class Create(AAZCommand):
    """Create a External Network resource

    :example: Create a External Network with option B properties
        az networkfabric externalnetwork create --resource-group "example-rg" --l3domain "example-l3domain" --resource-name "example-externalNetwork" --peering-option "OptionB" --option-b-properties "{routeTargets:{exportIpv4RouteTargets:['65046:10039'],exportIpv6RouteTargets:['65046:10039'],importIpv4RouteTargets:['65046:10039'],importIpv6RouteTargets:['65046:10039']}}" --import-route-policy "{importIpv4RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy',importIpv6RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy'}" --export-route-policy "{exportIpv4RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy',exportIpv6RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy'}"

    :example: Create a External Network with option A properties
        az networkfabric externalnetwork create --resource-group "example-rg" --l3domain "example-l3domain" --resource-name "example-externalNetwork" --peering-option "OptionA" --option-a-properties "{peerASN:65234,vlanId:501,mtu:1500,primaryIpv4Prefix:'172.23.1.0/31',secondaryIpv4Prefix:'172.23.1.2/31',bfdConfiguration:{multiplier:5,intervalInMilliSeconds:300}}" --import-route-policy "{importIpv4RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy',importIpv6RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy'}" --export-route-policy "{exportIpv4RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy',exportIpv6RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy'}"

    :example: Help text for sub parameters under the specific parent can be viewed by using the shorthand syntax '??'. See https://github.com/Azure/azure-cli/tree/dev/doc/shorthand_syntax.md for more about shorthand syntax.
        az networkfabric externalnetwork create --option-a-properties "??"
    """

    _aaz_info = {
        "version": "2023-06-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/l3isolationdomains/{}/externalnetworks/{}", "2023-06-15"],
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
            help="Name of the External Network.",
            required=True,
        )
        _args_schema.l3_isolation_domain_name = AAZStrArg(
            options=["--l3domain", "--l3-isolation-domain-name"],
            help="Name of the L3 Isolation Domain.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.annotation = AAZStrArg(
            options=["--annotation"],
            arg_group="Properties",
            help="Description for underlying resource.",
        )
        _args_schema.export_route_policy = AAZObjectArg(
            options=["--export-route-policy"],
            arg_group="Properties",
            help="Export Route Policy either IPv4 or IPv6.",
        )
        _args_schema.export_route_policy_id = AAZResourceIdArg(
            options=["--export-route-policy-id"],
            arg_group="Properties",
            help="ARM Resource ID of the RoutePolicy. This is used for the backward compatibility.",
        )
        _args_schema.import_route_policy = AAZObjectArg(
            options=["--import-route-policy"],
            arg_group="Properties",
            help="Import Route Policy either IPv4 or IPv6.",
        )
        _args_schema.import_route_policy_id = AAZResourceIdArg(
            options=["--import-route-policy-id"],
            arg_group="Properties",
            help="ARM Resource ID of the RoutePolicy. This is used for the backward compatibility.",
        )
        _args_schema.nni_id = AAZResourceIdArg(
            options=["--nni-id"],
            arg_group="Properties",
            help="ARM Resource ID of the networkToNetworkInterconnectId of the ExternalNetwork resource.",
        )
        _args_schema.option_a_properties = AAZObjectArg(
            options=["--option-a-properties"],
            arg_group="Properties",
            help="option A properties object.",
        )
        _args_schema.option_b_properties = AAZObjectArg(
            options=["--option-b-properties"],
            arg_group="Properties",
            help="option B properties object.",
        )
        _args_schema.peering_option = AAZStrArg(
            options=["--peering-option"],
            arg_group="Properties",
            help="Peering option list.",
            required=True,
            enum={"OptionA": "OptionA", "OptionB": "OptionB"},
        )

        export_route_policy = cls._args_schema.export_route_policy
        export_route_policy.export_ipv4_route_policy_id = AAZResourceIdArg(
            options=["export-ipv4-route-policy-id"],
            help="ARM resource ID of RoutePolicy.",
        )
        export_route_policy.export_ipv6_route_policy_id = AAZResourceIdArg(
            options=["export-ipv6-route-policy-id"],
            help="ARM resource ID of RoutePolicy.",
        )

        import_route_policy = cls._args_schema.import_route_policy
        import_route_policy.import_ipv4_route_policy_id = AAZResourceIdArg(
            options=["import-ipv4-route-policy-id"],
            help="ARM resource ID of RoutePolicy.",
        )
        import_route_policy.import_ipv6_route_policy_id = AAZResourceIdArg(
            options=["import-ipv6-route-policy-id"],
            help="ARM resource ID of RoutePolicy.",
        )

        option_a_properties = cls._args_schema.option_a_properties
        option_a_properties.bfd_configuration = AAZObjectArg(
            options=["bfd-configuration"],
            help="BFD configuration properties.",
        )
        option_a_properties.egress_acl_id = AAZResourceIdArg(
            options=["egress-acl-id"],
            help="Egress Acl ARM resource ID.",
        )
        option_a_properties.ingress_acl_id = AAZResourceIdArg(
            options=["ingress-acl-id"],
            help="Ingress Acl ARM resource ID.",
        )
        option_a_properties.mtu = AAZIntArg(
            options=["mtu"],
            help="MTU to use for option A peering. The value should be between 64 to 9200. Default Value is 1500. Example: 1650",
            fmt=AAZIntArgFormat(
                maximum=9200,
                minimum=64,
            ),
        )
        option_a_properties.peer_asn = AAZIntArg(
            options=["peer-asn"],
            help="Peer ASN number. The value should be between 1 to 4294967295. Example: 28.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=1,
            ),
        )
        option_a_properties.primary_ipv4_prefix = AAZStrArg(
            options=["primary-ipv4-prefix"],
            help="IPv4 Address Prefix. Example: 172.23.1.0/31.",
        )
        option_a_properties.primary_ipv6_prefix = AAZStrArg(
            options=["primary-ipv6-prefix"],
            help="IPv6 Address Prefix. Example: 3FFE:FFFF:0:CD30::a1/127",
            nullable=True,
        )
        option_a_properties.secondary_ipv4_prefix = AAZStrArg(
            options=["secondary-ipv4-prefix"],
            help="Secondary IPv4 Address Prefix. Example: 172.23.1.2/31.",
        )
        option_a_properties.secondary_ipv6_prefix = AAZStrArg(
            options=["secondary-ipv6-prefix"],
            help="Secondary IPv6 Address Prefix. Example: 3FFE:FFFF:0:CD30::a4/127",
            nullable=True,
        )
        option_a_properties.vlan_id = AAZIntArg(
            options=["vlan-id"],
            help="Vlan identifier. The value should be between 501 to 4094. Example : 501",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=4094,
                minimum=501,
            ),
        )

        bfd_configuration = cls._args_schema.option_a_properties.bfd_configuration
        bfd_configuration.interval_in_milli_seconds = AAZIntArg(
            options=["interval-in-milli-seconds"],
            help="Interval in milliseconds. Default Value is 300. Example: 300.",
        )
        bfd_configuration.multiplier = AAZIntArg(
            options=["multiplier"],
            help="Multiplier for the Bfd Configuration. Default Value is 5. Example: 5.",
        )

        option_b_properties = cls._args_schema.option_b_properties
        option_b_properties.export_route_targets = AAZListArg(
            options=["export-route-targets"],
            help="RouteTargets to be applied. This is used for the backward compatibility.",
        )
        option_b_properties.import_route_targets = AAZListArg(
            options=["import-route-targets"],
            help="RouteTargets to be applied. This is used for the backward compatibility.",
        )
        option_b_properties.route_targets = AAZObjectArg(
            options=["route-targets"],
            help="RouteTargets to be applied.",
        )

        export_route_targets = cls._args_schema.option_b_properties.export_route_targets
        export_route_targets.Element = AAZStrArg()

        import_route_targets = cls._args_schema.option_b_properties.import_route_targets
        import_route_targets.Element = AAZStrArg()

        route_targets = cls._args_schema.option_b_properties.route_targets
        route_targets.export_ipv4_route_targets = AAZListArg(
            options=["export-ipv4-route-targets"],
            help="Route Targets to be applied for outgoing routes into CE.",
        )
        route_targets.export_ipv6_route_targets = AAZListArg(
            options=["export-ipv6-route-targets"],
            help="Route Targets to be applied for outgoing routes from CE.",
        )
        route_targets.import_ipv4_route_targets = AAZListArg(
            options=["import-ipv4-route-targets"],
            help="Route Targets to be applied for incoming routes into CE.",
        )
        route_targets.import_ipv6_route_targets = AAZListArg(
            options=["import-ipv6-route-targets"],
            help="Route Targets to be applied for incoming routes from CE.",
        )

        export_ipv4_route_targets = cls._args_schema.option_b_properties.route_targets.export_ipv4_route_targets
        export_ipv4_route_targets.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        export_ipv6_route_targets = cls._args_schema.option_b_properties.route_targets.export_ipv6_route_targets
        export_ipv6_route_targets.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        import_ipv4_route_targets = cls._args_schema.option_b_properties.route_targets.import_ipv4_route_targets
        import_ipv4_route_targets.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        import_ipv6_route_targets = cls._args_schema.option_b_properties.route_targets.import_ipv6_route_targets
        import_ipv6_route_targets.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ExternalNetworksCreate(ctx=self.ctx)()
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

    class ExternalNetworksCreate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}/externalNetworks/{externalNetworkName}",
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
                    "externalNetworkName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "l3IsolationDomainName", self.ctx.args.l3_isolation_domain_name,
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
                    "api-version", "2023-06-15",
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
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("annotation", AAZStrType, ".annotation")
                properties.set_prop("exportRoutePolicy", AAZObjectType, ".export_route_policy")
                properties.set_prop("exportRoutePolicyId", AAZStrType, ".export_route_policy_id")
                properties.set_prop("importRoutePolicy", AAZObjectType, ".import_route_policy")
                properties.set_prop("importRoutePolicyId", AAZStrType, ".import_route_policy_id")
                properties.set_prop("networkToNetworkInterconnectId", AAZStrType, ".nni_id")
                properties.set_prop("optionAProperties", AAZObjectType, ".option_a_properties")
                properties.set_prop("optionBProperties", AAZObjectType, ".option_b_properties")
                properties.set_prop("peeringOption", AAZStrType, ".peering_option", typ_kwargs={"flags": {"required": True}})

            export_route_policy = _builder.get(".properties.exportRoutePolicy")
            if export_route_policy is not None:
                export_route_policy.set_prop("exportIpv4RoutePolicyId", AAZStrType, ".export_ipv4_route_policy_id")
                export_route_policy.set_prop("exportIpv6RoutePolicyId", AAZStrType, ".export_ipv6_route_policy_id")

            import_route_policy = _builder.get(".properties.importRoutePolicy")
            if import_route_policy is not None:
                import_route_policy.set_prop("importIpv4RoutePolicyId", AAZStrType, ".import_ipv4_route_policy_id")
                import_route_policy.set_prop("importIpv6RoutePolicyId", AAZStrType, ".import_ipv6_route_policy_id")

            option_a_properties = _builder.get(".properties.optionAProperties")
            if option_a_properties is not None:
                option_a_properties.set_prop("bfdConfiguration", AAZObjectType, ".bfd_configuration")
                option_a_properties.set_prop("egressAclId", AAZStrType, ".egress_acl_id")
                option_a_properties.set_prop("ingressAclId", AAZStrType, ".ingress_acl_id")
                option_a_properties.set_prop("mtu", AAZIntType, ".mtu")
                option_a_properties.set_prop("peerASN", AAZIntType, ".peer_asn", typ_kwargs={"flags": {"required": True}})
                option_a_properties.set_prop("primaryIpv4Prefix", AAZStrType, ".primary_ipv4_prefix")
                option_a_properties.set_prop("primaryIpv6Prefix", AAZStrType, ".primary_ipv6_prefix", typ_kwargs={"nullable": True})
                option_a_properties.set_prop("secondaryIpv4Prefix", AAZStrType, ".secondary_ipv4_prefix")
                option_a_properties.set_prop("secondaryIpv6Prefix", AAZStrType, ".secondary_ipv6_prefix", typ_kwargs={"nullable": True})
                option_a_properties.set_prop("vlanId", AAZIntType, ".vlan_id", typ_kwargs={"flags": {"required": True}})

            bfd_configuration = _builder.get(".properties.optionAProperties.bfdConfiguration")
            if bfd_configuration is not None:
                bfd_configuration.set_prop("intervalInMilliSeconds", AAZIntType, ".interval_in_milli_seconds")
                bfd_configuration.set_prop("multiplier", AAZIntType, ".multiplier")

            option_b_properties = _builder.get(".properties.optionBProperties")
            if option_b_properties is not None:
                option_b_properties.set_prop("exportRouteTargets", AAZListType, ".export_route_targets")
                option_b_properties.set_prop("importRouteTargets", AAZListType, ".import_route_targets")
                option_b_properties.set_prop("routeTargets", AAZObjectType, ".route_targets")

            export_route_targets = _builder.get(".properties.optionBProperties.exportRouteTargets")
            if export_route_targets is not None:
                export_route_targets.set_elements(AAZStrType, ".")

            import_route_targets = _builder.get(".properties.optionBProperties.importRouteTargets")
            if import_route_targets is not None:
                import_route_targets.set_elements(AAZStrType, ".")

            route_targets = _builder.get(".properties.optionBProperties.routeTargets")
            if route_targets is not None:
                route_targets.set_prop("exportIpv4RouteTargets", AAZListType, ".export_ipv4_route_targets")
                route_targets.set_prop("exportIpv6RouteTargets", AAZListType, ".export_ipv6_route_targets")
                route_targets.set_prop("importIpv4RouteTargets", AAZListType, ".import_ipv4_route_targets")
                route_targets.set_prop("importIpv6RouteTargets", AAZListType, ".import_ipv6_route_targets")

            export_ipv4_route_targets = _builder.get(".properties.optionBProperties.routeTargets.exportIpv4RouteTargets")
            if export_ipv4_route_targets is not None:
                export_ipv4_route_targets.set_elements(AAZStrType, ".")

            export_ipv6_route_targets = _builder.get(".properties.optionBProperties.routeTargets.exportIpv6RouteTargets")
            if export_ipv6_route_targets is not None:
                export_ipv6_route_targets.set_elements(AAZStrType, ".")

            import_ipv4_route_targets = _builder.get(".properties.optionBProperties.routeTargets.importIpv4RouteTargets")
            if import_ipv4_route_targets is not None:
                import_ipv4_route_targets.set_elements(AAZStrType, ".")

            import_ipv6_route_targets = _builder.get(".properties.optionBProperties.routeTargets.importIpv6RouteTargets")
            if import_ipv6_route_targets is not None:
                import_ipv6_route_targets.set_elements(AAZStrType, ".")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.annotation = AAZStrType()
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.export_route_policy = AAZObjectType(
                serialized_name="exportRoutePolicy",
            )
            properties.export_route_policy_id = AAZStrType(
                serialized_name="exportRoutePolicyId",
            )
            properties.import_route_policy = AAZObjectType(
                serialized_name="importRoutePolicy",
            )
            properties.import_route_policy_id = AAZStrType(
                serialized_name="importRoutePolicyId",
            )
            properties.network_to_network_interconnect_id = AAZStrType(
                serialized_name="networkToNetworkInterconnectId",
            )
            properties.option_a_properties = AAZObjectType(
                serialized_name="optionAProperties",
            )
            properties.option_b_properties = AAZObjectType(
                serialized_name="optionBProperties",
            )
            properties.peering_option = AAZStrType(
                serialized_name="peeringOption",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            export_route_policy = cls._schema_on_200_201.properties.export_route_policy
            export_route_policy.export_ipv4_route_policy_id = AAZStrType(
                serialized_name="exportIpv4RoutePolicyId",
            )
            export_route_policy.export_ipv6_route_policy_id = AAZStrType(
                serialized_name="exportIpv6RoutePolicyId",
            )

            import_route_policy = cls._schema_on_200_201.properties.import_route_policy
            import_route_policy.import_ipv4_route_policy_id = AAZStrType(
                serialized_name="importIpv4RoutePolicyId",
            )
            import_route_policy.import_ipv6_route_policy_id = AAZStrType(
                serialized_name="importIpv6RoutePolicyId",
            )

            option_a_properties = cls._schema_on_200_201.properties.option_a_properties
            option_a_properties.bfd_configuration = AAZObjectType(
                serialized_name="bfdConfiguration",
            )
            option_a_properties.egress_acl_id = AAZStrType(
                serialized_name="egressAclId",
            )
            option_a_properties.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"read_only": True},
            )
            option_a_properties.ingress_acl_id = AAZStrType(
                serialized_name="ingressAclId",
            )
            option_a_properties.mtu = AAZIntType()
            option_a_properties.peer_asn = AAZIntType(
                serialized_name="peerASN",
                flags={"required": True},
            )
            option_a_properties.primary_ipv4_prefix = AAZStrType(
                serialized_name="primaryIpv4Prefix",
            )
            option_a_properties.primary_ipv6_prefix = AAZStrType(
                serialized_name="primaryIpv6Prefix",
                nullable=True,
            )
            option_a_properties.secondary_ipv4_prefix = AAZStrType(
                serialized_name="secondaryIpv4Prefix",
            )
            option_a_properties.secondary_ipv6_prefix = AAZStrType(
                serialized_name="secondaryIpv6Prefix",
                nullable=True,
            )
            option_a_properties.vlan_id = AAZIntType(
                serialized_name="vlanId",
                flags={"required": True},
            )

            bfd_configuration = cls._schema_on_200_201.properties.option_a_properties.bfd_configuration
            bfd_configuration.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            bfd_configuration.interval_in_milli_seconds = AAZIntType(
                serialized_name="intervalInMilliSeconds",
            )
            bfd_configuration.multiplier = AAZIntType()

            option_b_properties = cls._schema_on_200_201.properties.option_b_properties
            option_b_properties.export_route_targets = AAZListType(
                serialized_name="exportRouteTargets",
            )
            option_b_properties.import_route_targets = AAZListType(
                serialized_name="importRouteTargets",
            )
            option_b_properties.route_targets = AAZObjectType(
                serialized_name="routeTargets",
            )

            export_route_targets = cls._schema_on_200_201.properties.option_b_properties.export_route_targets
            export_route_targets.Element = AAZStrType()

            import_route_targets = cls._schema_on_200_201.properties.option_b_properties.import_route_targets
            import_route_targets.Element = AAZStrType()

            route_targets = cls._schema_on_200_201.properties.option_b_properties.route_targets
            route_targets.export_ipv4_route_targets = AAZListType(
                serialized_name="exportIpv4RouteTargets",
            )
            route_targets.export_ipv6_route_targets = AAZListType(
                serialized_name="exportIpv6RouteTargets",
            )
            route_targets.import_ipv4_route_targets = AAZListType(
                serialized_name="importIpv4RouteTargets",
            )
            route_targets.import_ipv6_route_targets = AAZListType(
                serialized_name="importIpv6RouteTargets",
            )

            export_ipv4_route_targets = cls._schema_on_200_201.properties.option_b_properties.route_targets.export_ipv4_route_targets
            export_ipv4_route_targets.Element = AAZStrType()

            export_ipv6_route_targets = cls._schema_on_200_201.properties.option_b_properties.route_targets.export_ipv6_route_targets
            export_ipv6_route_targets.Element = AAZStrType()

            import_ipv4_route_targets = cls._schema_on_200_201.properties.option_b_properties.route_targets.import_ipv4_route_targets
            import_ipv4_route_targets.Element = AAZStrType()

            import_ipv6_route_targets = cls._schema_on_200_201.properties.option_b_properties.route_targets.import_ipv6_route_targets
            import_ipv6_route_targets.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
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

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
