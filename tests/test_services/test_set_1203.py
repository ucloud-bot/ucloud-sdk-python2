# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
import pytest
import logging
from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)
scenario = utest.Scenario(1203)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_1203(client, variables):
    scenario.initial(variables)
    scenario.variables["Protocol"] = "redis"
    scenario.variables["Type"] = "double"
    scenario.variables["Name"] = "distributed_redis"
    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CheckUMemSpaceAllowanceResponse"),
    ],
    action="CheckUMemSpaceAllowance",
)
def check_umem_space_allowance_00(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Size": 16,
        "Region": variables.get("Region"),
        "Count": 1,
    }
    try:
        resp = client.invoke("CheckUMemSpaceAllowance", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUMemSpace",
)
def create_umem_space_01(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Type": variables.get("Type"),
        "Size": 16,
        "Region": variables.get("Region"),
        "Quantity": 1,
        "Protocol": variables.get("Protocol"),
        "Name": variables.get("Name"),
        "ChargeType": "Month",
    }
    try:
        resp = client.umem().create_umem_space(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["Space_Id"] = utest.value_at_path(resp, "SpaceId")
    return resp


@scenario.step(
    max_retries=30,
    retry_interval=10,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.State", "Running"),
    ],
    action="DescribeUMem",
)
def describe_umem_02(client, variables):
    d = {
        "ResourceId": variables.get("Space_Id"),
        "Region": variables.get("Region"),
        "Protocol": variables.get("Protocol"),
        "Offset": 0,
        "Limit": 1000,
    }
    try:
        resp = client.invoke("DescribeUMem", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "ModifyUMemSpaceNameResponse"),
    ],
    action="ModifyUMemSpaceName",
)
def modify_umem_space_name_03(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "SpaceId": variables.get("Space_Id"),
        "Region": variables.get("Region"),
        "Name": "Rename_FBS",
    }
    try:
        resp = client.umem().modify_umem_space_name(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.State", "Running"),
    ],
    action="DescribeUMem",
)
def describe_umem_04(client, variables):
    d = {
        "ResourceId": variables.get("Space_Id"),
        "Region": variables.get("Region"),
        "Protocol": variables.get("Protocol"),
        "Offset": 0,
        "Limit": 1000,
    }
    try:
        resp = client.invoke("DescribeUMem", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetUMemSpaceStateResponse"),
    ],
    action="GetUMemSpaceState",
)
def get_umem_space_state_05(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "SpaceId": variables.get("Space_Id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.umem().get_umem_space_state(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=20,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ResizeUMemSpace",
)
def resize_umem_space_06(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "SpaceId": variables.get("Space_Id"),
        "Size": 17,
        "Region": variables.get("Region"),
    }
    try:
        resp = client.umem().resize_umem_space(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=40,
    retry_interval=10,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "DataSet.0.State", "Running"),
    ],
    action="DescribeUMem",
)
def describe_umem_07(client, variables):
    d = {
        "ResourceId": variables.get("Space_Id"),
        "Region": variables.get("Region"),
        "Protocol": variables.get("Protocol"),
        "Offset": 0,
        "Limit": 1000,
    }
    try:
        resp = client.invoke("DescribeUMem", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=10,
    startup_delay=10,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteUMemSpaceResponse"),
    ],
    action="DeleteUMemSpace",
)
def delete_umem_space_08(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "SpaceId": variables.get("Space_Id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.umem().delete_umem_space(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=30,
    retry_interval=10,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUMemResponse"),
        ("object_not_contains", "DataSet", variables.get("Space_Id")),
    ],
    action="DescribeUMem",
)
def describe_umem_09(client, variables):
    d = {
        "ResourceId": variables.get("Space_Id"),
        "Region": variables.get("Region"),
        "Protocol": variables.get("Protocol"),
        "Offset": 0,
        "Limit": 1000,
    }
    try:
        resp = client.invoke("DescribeUMem", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp
