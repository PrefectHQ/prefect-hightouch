import pytest
from httpx import HTTPStatusError, Response

from prefect_hightouch.api_client.models import (
    ListSyncOrderBy,
    Sync,
    SyncRun,
    TriggerRunCustomInput,
    TriggerRunInput,
    TriggerRunOutput,
)
from prefect_hightouch.exceptions import (
    TERMINAL_STATUS_EXCEPTIONS,
    HightouchSyncRunTimedOut,
)
from prefect_hightouch.syncs import trigger_sync_run_and_wait_for_completion
from prefect_hightouch.syncs.generated import (
    get_sync,
    list_sync,
    list_sync_runs,
    trigger_run,
    trigger_run_custom,
)


@pytest.fixture()
def sync_data_json():
    return {
        "id": 123,
        "slug": "slug",
        "workspaceId": 1234,
        "createdAt": "2022-10-28T16:48:58.123Z",
        "updatedAt": "2022-10-28T17:36:55.123Z",
        "destinationId": 12345,
        "modelId": 123456,
        "configuration": {
            "mode": "all",
            "path": "test.csv",
            "fileType": "csv",
            "mappings": [],
            "delimiter": ",",
            "configVersion": 0,
            "includeHeader": False,
            "autoSyncColumns": True,
        },
        "schedule": None,
        "status": "success",
        "disabled": False,
        "lastRunAt": "2022-10-28T16:49:02.123Z",
        "referencedColumns": [],
        "primaryKey": "DATE",
    }


async def test_list_sync(hightouch_credentials, sync_data_json, respx_mock):
    respx_mock.get(
        "https://api.hightouch.com/api/v1/syncs?limit=1&orderBy=createdAt"
    ).mock(
        return_value=Response(
            200,
            json={"data": [sync_data_json]},
        )
    )
    actual = await list_sync.fn(
        hightouch_credentials, limit=1, order_by=ListSyncOrderBy.CREATEDAT
    )
    assert isinstance(actual, list)
    assert len(actual) == 1
    assert isinstance(actual[0], Sync)
    assert actual[0].id == "123"


async def test_list_sync_error(hightouch_credentials, respx_mock):
    respx_mock.get(
        "https://api.hightouch.com/api/v1/syncs?limit=1&orderBy=createdAt"
    ).mock(return_value=Response(401))
    with pytest.raises(HTTPStatusError, match="Client error '401 Unauthorized'"):
        await list_sync.fn(
            hightouch_credentials, limit=1, order_by=ListSyncOrderBy.CREATEDAT
        )


async def test_get_sync(hightouch_credentials, sync_data_json, respx_mock):
    respx_mock.get("https://api.hightouch.com/api/v1/syncs/123").mock(
        return_value=Response(200, json=sync_data_json)
    )
    actual = await get_sync.fn(
        hightouch_credentials,
        sync_id=123,
    )
    assert isinstance(actual, Sync)
    assert actual.id == "123"


async def test_get_sync_error(hightouch_credentials, respx_mock):
    respx_mock.get("https://api.hightouch.com/api/v1/syncs/000").mock(
        return_value=Response(404)
    )
    with pytest.raises(HTTPStatusError, match="Client error '404 Not Found'"):
        await get_sync.fn(hightouch_credentials, "000")


async def test_list_sync_runs(hightouch_credentials, respx_mock):
    respx_mock.get(
        "https://api.hightouch.com/api/v1/syncs/123/runs?limit=1&orderBy=createdAt"
    ).mock(
        return_value=Response(
            200,
            json={
                "data": [
                    {
                        "id": 123456789,
                        "createdAt": "2022-10-28T16:49:02.226Z",
                        "startedAt": "2022-10-28T16:49:02.491Z",
                        "finishedAt": "2022-10-28T16:49:04.261Z",
                        "querySize": 3,
                        "status": "success",
                        "completionRatio": 1,
                        "plannedRows": {
                            "addedCount": 3,
                            "changedCount": 0,
                            "removedCount": 0,
                        },
                        "successfulRows": {
                            "addedCount": 0,
                            "changedCount": 0,
                            "removedCount": 0,
                        },
                        "failedRows": {
                            "addedCount": 0,
                            "changedCount": 0,
                            "removedCount": 0,
                        },
                        "error": None,
                    }
                ]
            },
        )
    )
    actual = await list_sync_runs.fn(
        hightouch_credentials, sync_id=123, limit=1, order_by=ListSyncOrderBy.CREATEDAT
    )
    assert isinstance(actual, list)
    assert len(actual) == 1
    assert isinstance(actual[0], SyncRun)
    assert actual[0].id == "123456789"
    assert actual[0].query_size == 3


async def test_list_sync_runs_error(hightouch_credentials, respx_mock):
    respx_mock.get(
        "https://api.hightouch.com/api/v1/syncs/123/runs?limit=1&orderBy=createdAt"
    ).mock(return_value=Response(401))
    with pytest.raises(HTTPStatusError, match="Client error '401 Unauthorized'"):
        await list_sync_runs.fn(
            hightouch_credentials,
            sync_id=123,
            limit=1,
            order_by=ListSyncOrderBy.CREATEDAT,
        )


async def test_trigger_run(hightouch_credentials, respx_mock):
    respx_mock.post("https://api.hightouch.com/api/v1/syncs/123/trigger").mock(
        return_value=Response(200, json={"id": "123"})
    )
    actual = await trigger_run.fn(
        hightouch_credentials, 123, json_body=TriggerRunInput(full_resync=False)
    )
    assert isinstance(actual, TriggerRunOutput)
    assert actual.id == "123"


async def test_trigger_run_error(hightouch_credentials, respx_mock):
    respx_mock.post("https://api.hightouch.com/api/v1/syncs/123/trigger").mock(
        return_value=Response(401)
    )
    with pytest.raises(HTTPStatusError, match="Client error '401 Unauthorized'"):
        await trigger_run.fn(
            hightouch_credentials, 123, json_body=TriggerRunInput(full_resync=False)
        )


async def test_trigger_run_custom(hightouch_credentials, respx_mock):
    respx_mock.post("https://api.hightouch.com/api/v1/syncs/trigger").mock(
        return_value=Response(200, json={"id": "123"})
    )
    actual = await trigger_run_custom.fn(
        hightouch_credentials,
        json_body=TriggerRunCustomInput(
            sync_slug="weather-database-to-google-cloud-storage-yhzkq",
            full_resync=False,
        ),
    )
    assert isinstance(actual, TriggerRunOutput)
    assert actual.id == "123"


async def test_trigger_run_custom_error(hightouch_credentials, respx_mock):
    respx_mock.post("https://api.hightouch.com/api/v1/syncs/trigger").mock(
        return_value=Response(401)
    )
    with pytest.raises(HTTPStatusError, match="Client error '401 Unauthorized'"):
        await trigger_run_custom.fn(
            hightouch_credentials,
            json_body=TriggerRunCustomInput(
                sync_slug="weather-database-to-google-cloud-storage-yhzkq",
                full_resync=False,
            ),
        )


async def test_trigger_sync_run_and_wait_for_completion(
    hightouch_credentials, sync_data_json, respx_mock
):
    respx_mock.post("https://api.hightouch.com/api/v1/syncs/123/trigger").mock(
        return_value=Response(200, json={"id": "123"})
    )
    respx_mock.get("https://api.hightouch.com/api/v1/syncs/123").mock(
        return_value=Response(200, json=sync_data_json)
    )
    actual = await trigger_sync_run_and_wait_for_completion(
        hightouch_credentials,
        full_resync=False,
        sync_id="123",
    )
    assert isinstance(actual, Sync)
    assert actual.id == "123"
    assert actual.slug == "slug"


@pytest.mark.parametrize(
    "status", ["queued", "pending", "querying", "processing", "reporting"]
)
async def test_trigger_sync_run_and_wait_for_completion_timeout(
    hightouch_credentials, sync_data_json, status, respx_mock
):
    sync_data_json["status"] = status

    respx_mock.post("https://api.hightouch.com/api/v1/syncs/123/trigger").mock(
        return_value=Response(200, json={"id": "123"})
    )
    respx_mock.get("https://api.hightouch.com/api/v1/syncs/123").mock(
        return_value=Response(200, json=sync_data_json)
    )
    with pytest.raises(HightouchSyncRunTimedOut, match="Max wait time of 2 seconds"):
        await trigger_sync_run_and_wait_for_completion(
            hightouch_credentials,
            full_resync=False,
            sync_id="123",
            max_wait_seconds=2,
            poll_frequency_seconds=1,
        )


@pytest.mark.parametrize("status", TERMINAL_STATUS_EXCEPTIONS.keys())
async def test_trigger_sync_run_and_wait_for_completion_failed(
    hightouch_credentials,
    sync_data_json,
    status,
    respx_mock,
):
    sync_data_json["status"] = status.value
    if status == "success":
        pytest.skip()

    respx_mock.post("https://api.hightouch.com/api/v1/syncs/123/trigger").mock(
        return_value=Response(200, json={"id": "123"})
    )
    respx_mock.get("https://api.hightouch.com/api/v1/syncs/123").mock(
        return_value=Response(200, json=sync_data_json)
    )
    match = f"unsuccessful with {status.value!r} status"
    with pytest.raises(TERMINAL_STATUS_EXCEPTIONS[status], match=match):
        await trigger_sync_run_and_wait_for_completion(
            hightouch_credentials,
            full_resync=True,
            sync_id="123",
        )
