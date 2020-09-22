# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
from ucloud.core.typesystem import schema, fields


class UDBBackupSetSchema(schema.ResponseSchema):
    """UDBBackupSet - DescribeUDBBackup"""

    fields = {
        "BackupEndTime": fields.Int(required=False, load_from="BackupEndTime"),
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "ErrorInfo": fields.Str(required=False, load_from="ErrorInfo"),
        "State": fields.Str(required=False, load_from="State"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDBSlaveInstanceSetSchema(schema.ResponseSchema):
    """UDBSlaveInstanceSet - DescribeUDBSlaveInstance"""

    fields = {
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "BackupBeginTime": fields.Int(
            required=False, load_from="BackupBeginTime"
        ),
        "BackupBlacklist": fields.Str(
            required=False, load_from="BackupBlacklist"
        ),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "BackupDuration": fields.Int(
            required=False, load_from="BackupDuration"
        ),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "ClusterRole": fields.Str(required=False, load_from="ClusterRole"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "InstanceTypeId": fields.Int(
            required=False, load_from="InstanceTypeId"
        ),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Role": fields.Str(required=False, load_from="Role"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "SystemFileSize": fields.Float(
            required=False, load_from="SystemFileSize"
        ),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDBInstanceSetSchema(schema.ResponseSchema):
    """UDBInstanceSet - DescribeUDBInstance"""

    fields = {
        "AdminUser": fields.Str(required=False, load_from="AdminUser"),
        "BackupBeginTime": fields.Int(
            required=False, load_from="BackupBeginTime"
        ),
        "BackupBlacklist": fields.Str(
            required=False, load_from="BackupBlacklist"
        ),
        "BackupCount": fields.Int(required=False, load_from="BackupCount"),
        "BackupDate": fields.Str(required=False, load_from="BackupDate"),
        "BackupDuration": fields.Int(
            required=False, load_from="BackupDuration"
        ),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "CluserRole": fields.Str(required=False, load_from="CluserRole"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "DataFileSize": fields.Float(required=False, load_from="DataFileSize"),
        "DataSet": fields.List(UDBSlaveInstanceSetSchema()),
        "DiskSpace": fields.Int(required=False, load_from="DiskSpace"),
        "DiskUsedSize": fields.Float(required=False, load_from="DiskUsedSize"),
        "ExpiredTime": fields.Int(required=False, load_from="ExpiredTime"),
        "InstanceMode": fields.Str(required=False, load_from="InstanceMode"),
        "InstanceType": fields.Str(required=False, load_from="InstanceType"),
        "InstanceTypeId": fields.Int(
            required=False, load_from="InstanceTypeId"
        ),
        "LogFileSize": fields.Float(required=False, load_from="LogFileSize"),
        "MemoryLimit": fields.Int(required=False, load_from="MemoryLimit"),
        "ModifyTime": fields.Int(required=False, load_from="ModifyTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ParamGroupId": fields.Int(required=False, load_from="ParamGroupId"),
        "Port": fields.Int(required=False, load_from="Port"),
        "Role": fields.Str(required=False, load_from="Role"),
        "SSDType": fields.Str(required=False, load_from="SSDType"),
        "SrcDBId": fields.Str(required=False, load_from="SrcDBId"),
        "State": fields.Str(required=False, load_from="State"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "SystemFileSize": fields.Float(
            required=False, load_from="SystemFileSize"
        ),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "UseSSD": fields.Bool(required=False, load_from="UseSSD"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VirtualIP": fields.Str(required=False, load_from="VirtualIP"),
        "VirtualIPMac": fields.Str(required=False, load_from="VirtualIPMac"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDBInstanceBinlogSetSchema(schema.ResponseSchema):
    """UDBInstanceBinlogSet - DescribeUDBInstanceBinlog"""

    fields = {
        "BeginTime": fields.Int(required=False, load_from="BeginTime"),
        "EndTime": fields.Int(required=False, load_from="EndTime"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Size": fields.Int(required=False, load_from="Size"),
    }


class UDBInstancePriceSetSchema(schema.ResponseSchema):
    """UDBInstancePriceSet - DescribeUDBInstancePrice"""

    fields = {
        "ChargeType": fields.Str(required=False, load_from="ChargeType"),
        "Price": fields.Int(required=False, load_from="Price"),
    }


class LogPackageDataSetSchema(schema.ResponseSchema):
    """LogPackageDataSet - DescribeUDBLogPackage"""

    fields = {
        "BackupId": fields.Int(required=False, load_from="BackupId"),
        "BackupName": fields.Str(required=False, load_from="BackupName"),
        "BackupSize": fields.Int(required=False, load_from="BackupSize"),
        "BackupTime": fields.Int(required=False, load_from="BackupTime"),
        "BackupType": fields.Int(required=False, load_from="BackupType"),
        "BackupZone": fields.Str(required=False, load_from="BackupZone"),
        "DBId": fields.Str(required=False, load_from="DBId"),
        "DBName": fields.Str(required=False, load_from="DBName"),
        "State": fields.Str(required=False, load_from="State"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDBParamMemberSetSchema(schema.ResponseSchema):
    """UDBParamMemberSet - DescribeUDBParamGroup"""

    fields = {
        "AllowedVal": fields.Str(required=False, load_from="AllowedVal"),
        "ApplyType": fields.Int(required=False, load_from="ApplyType"),
        "FormatType": fields.Int(required=False, load_from="FormatType"),
        "Key": fields.Str(required=False, load_from="Key"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "Value": fields.Str(required=False, load_from="Value"),
        "ValueType": fields.Int(required=False, load_from="ValueType"),
    }


class UDBParamGroupSetSchema(schema.ResponseSchema):
    """UDBParamGroupSet - DescribeUDBParamGroup"""

    fields = {
        "DBTypeId": fields.Str(required=False, load_from="DBTypeId"),
        "Description": fields.Str(required=False, load_from="Description"),
        "GroupId": fields.Int(required=False, load_from="GroupId"),
        "GroupName": fields.Str(required=False, load_from="GroupName"),
        "Modifiable": fields.Bool(required=False, load_from="Modifiable"),
        "ParamMember": fields.List(UDBParamMemberSetSchema()),
        "RegionFlag": fields.Bool(required=False, load_from="RegionFlag"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class UDBTypeSetSchema(schema.ResponseSchema):
    """UDBTypeSet - DescribeUDBType"""

    fields = {"DBTypeId": fields.Str(required=False, load_from="DBTypeId")}
