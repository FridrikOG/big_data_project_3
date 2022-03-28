from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import pathlib
import pandas as pd
bucket = "ru"

print("Current path ", pathlib.Path().resolve())


def writeFileToInflux():
    client = InfluxDBClient(url="http://localhost:8086",
                            token="1udCMOFcFml-OEM-k9lHBbHLZFXzHjV8oTSqLeQ0GO5H7Y2ls6gSVRHOXxKe51I1w-cc09YZMYiu5QLsVL-AnA==", org="RU")

    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()
    fileURI = 'data/maindata2.csv'

    write_api.write(bucket=bucket, record=fileURI)

    print(query_api._get_query_options())
    # ## using Table structure
    tables = query_api.query('from(bucket:"ru") |> range(start: -10m)')

    for table in tables:
        print(table)
        for row in table.records:
            print(row.values)


def main():
    print("In main")
    writeFileToInflux()


main()
