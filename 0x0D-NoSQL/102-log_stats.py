#!/usr/bin/env python3
"""script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    collection = MongoClient().logs.nginx
    docs_num = collection.count_documents({})
    get_num = collection.count_documents({"method": "GET"})
    post_num = collection.count_documents({"method": "POST"})
    put_num = collection.count_documents({"method": "PUT"})
    patch_num = collection.count_documents({"method": "PATCH"})
    delete_num = collection.count_documents({"method": "DELETE"})
    status_num = collection.count_documents({"path": "/status"})
    ips = collection.aggregate([
        {"$group": {"_id": "$ip", "ip_num": {"$sum": 1}}},
        {"$sort": {"ip_num": -1}},
        {"$limit": 10}
    ])

    print(f"{docs_num} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_num}")
    print(f"\tmethod POST: {post_num}")
    print(f"\tmethod PUT: {put_num}")
    print(f"\tmethod PATCH: {patch_num}")
    print(f"\tmethod DELETE: {delete_num}")
    print(f"{status_num} status check")
    print("IPs:")
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('ip_num')}")
