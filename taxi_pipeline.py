"""Template for building a `dlt` pipeline to ingest data from a REST API."""

import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
def taxi_pipeline_rest_api_source():
    """Define dlt resources from REST API endpoints."""
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
        },
        "resources": [
            {
                "name": "trips",
                "endpoint": {
                    "path": "",
                    "paginator": {
                        "type": "page_number",
                        "total_path": None,
                        "base_page": 1,
                        "page_param": "page",
                        "stop_after_empty_page": True,
                    },
                },
            },
        ],
        "resource_defaults": {
            "write_disposition": "append",
        },
    }

    yield from rest_api_resources(config)


taxi_pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    refresh="drop_sources",
    progress="log",
    dev_mode=True,
)


if __name__ == "__main__":
    load_info = taxi_pipeline.run(taxi_pipeline_rest_api_source())
    print(load_info)  # noqa: T201
